from pathlib import Path
import numpy as np
from skfem import *
from skfem.models.poisson import laplace, unit_load
from skfem.helpers import dot, grad

# Step 1: Create a mesh
mesh = MeshTri().refined(1)
print("__file__:    ", __file__)

mesh.save(Path(__file__).parent / "from_chatgpt_mixedBCs2.vtk")
# exit()

# Step 2: Define the element and basis
element = ElementTriP1()
basis = InteriorBasis(mesh, element)

# Step 3: Formulate the problem (LHS: Laplacian, RHS: source term)
A = asm(laplace, basis)
b = asm(unit_load, basis)


# Step 4: Identify boundary facets using mesh.facets_satisfying
@BilinearForm
def neumann(u, v, w):
    return dot(grad(u), w.n) * v


top = mesh.facets_satisfying(lambda x: np.isclose(x[1], 1.0))
bottom = mesh.facets_satisfying(lambda x: np.isclose(x[1], 0.0))
print(f"{top=}")
print(f"{bottom=}")


# Define a function representing the Neumann condition
def flux_function(x, normal):
    # Example: Constant flux across top and bottom
    return np.zeros_like(x[0])


# Assemble Neumann contributions on top and bottom boundaries
b += asm(neumann, basis, facets=top, fn=flux_function)
b += asm(neumann, basis, facets=bottom, fn=flux_function)

# Step 5: Apply Dirichlet boundary conditions on left and right boundaries
dirichlet_dofs = np.concatenate(
    (
        basis.get_dofs(lambda x: np.isclose(x[0], 0.0)).all(),  # Left boundary
        basis.get_dofs(lambda x: np.isclose(x[0], 1.0)).all(),  # Right boundary
    )
)
A, b = enforce(A, b, D=dirichlet_dofs)

# Step 6: Solve the linear system
u = solve(*condense(A, b, D=dirichlet_dofs))

# Solution plotting
from skfem.visuals.matplotlib import plot, show

plot(mesh, u, shading="gouraud")
show()
