r"""Heat equation.

The solutions of the heat equation

.. math::
    \frac{\partial T}{\partial t} = \kappa\Delta T
in various tensor-product domains consist of the sum of modes which
are tensor-products of the modes on the factor-domains (Carslaw &
Jaegar 1959, §5.6).

* Carslaw, H. S., & J. C. Jaeger (1959). Conduction of Heat in Solids (2nd ed.). Oxford University Press

For example, in the rectangle :math:`|x| < w_0, |y| < w_1`, with
homogeneous Dirichlet boundary conditions, the modes are products of a
cosine in each direction,

.. math::
    \exp \left[
      -\frac{\kappa\pi^2 t}{4}
      \left\{
        \left(\frac{2n_0 + 1}{w_0}\right)^2 +
        \left(\frac{2n_1 + 1}{w_1}\right)^2
      \right\}
    \right]
    \cos\frac{(2n_0 + 1)\pi x}{2w_0}
    \cos\frac{(2n_1 + 1)\pi y}{2w_1}
for :math:`n_0, n_1 = 0, 1, 2, \ldots`.

Here we simulate the decay of the fundamental, :math:`n_0 = n_1 = 0`,
discretizing time using the generalized ('theta method') trapezoidal
rule.

For a constant time-step, this leads to a linear algebraic problem at
each time with the same matrix but changing right-hand side.  This
motivates factoring the matrix; e.g. with `scipy.sparse.linalg.splu`.


"""

from math import ceil
from typing import Iterator, Tuple

import numpy as np
from scipy.sparse.linalg import splu

from skfem import *
from skfem.models.poisson import laplace, mass

import meshio

halfwidth = np.array([2.0, 3.0])
ncells = 2**3
diffusivity = 5.0

mesh = MeshQuad.init_tensor(
    np.linspace(-1, 1, 2 * ncells) * halfwidth[0],
    np.linspace(-1, 1, 2 * ncells * ceil(halfwidth[1] // halfwidth[0])) * halfwidth[1],
)

element = ElementQuad2()  # or ElementQuad1
basis = Basis(mesh, element)

L = diffusivity * asm(laplace, basis)
M = asm(mass, basis)

dt = 0.01
print("dt =", dt)
theta = 0.5  # Crank–Nicolson
L0, M0 = penalize(L, M, D=basis.get_dofs())
A = M0 + theta * L0 * dt
B = M0 - (1 - theta) * L0 * dt

backsolve = splu(A.T).solve  # .T as splu prefers CSC

u_init = np.cos(np.pi * basis.doflocs / 2 / halfwidth[:, None]).prod(0)


def exact(t: float) -> np.ndarray:
    return np.exp(-diffusivity * np.pi**2 * t / 4 * sum(halfwidth**-2)) * u_init


def evolve(t: float, u: np.ndarray) -> Iterator[Tuple[float, np.ndarray]]:
    while np.linalg.norm(u, np.inf) > 2**-3:
        t, u = t + dt, backsolve(B @ u)
        yield t, u


probe = basis.probes(np.zeros((mesh.dim(), 1)))

t, u = 0.0, u_init
times = [t]
field_over_time = [u]
while np.linalg.norm(u, np.inf) > 2**-3:
    t, u = next(evolve(t, u))
    times.append(t)
    field_over_time.append(u)
    u0 = {"skfem": (probe @ u)[0], "exact": (probe @ exact(t))[0]}
    print(
        "{:4.2f}, {:5.3f}, {:+7.4f}".format(t, u0["skfem"], u0["skfem"] - u0["exact"])
    )

# Convert mesh node 2D coordinates to 3D by adding zero z coordinate to each 2D coordinate
points = np.vstack((mesh.p, np.zeros(mesh.p.shape[1]))).T
# Create array containing node indices for each cell
cells = []
for i in range(mesh.t.shape[1]):
    cells.append([index for index in mesh.t[:, i]])
cells = np.array(cells)

with meshio.xdmf.TimeSeriesWriter("time_series_data.xdmf") as writer:
    writer.write_points_cells(points, [("quad", cells)])
    for t, u in zip(times, field_over_time):
        writer.write_data(t, point_data={"solution": u[: mesh.nvertices]})
