# from skfem import *
from skfem import MeshTri, Basis, ElementTriP1, BilinearForm, LinearForm, enforce, solve
from skfem.helpers import dot, grad

# create 2D mesh and associated basis, both have default boundaries defined as "left", "right", "top", "bottom"
mesh = MeshTri().refined(4)
basis = Basis(mesh, ElementTriP1())


# Create left and right hand sides of weak formulation
@BilinearForm
def laplace(u, v, _):
    return dot(grad(u), grad(v))


@LinearForm
def rhs(v, _):
    return 0.0 * v


A = laplace.assemble(basis)
b = rhs.assemble(basis)

# Boundary conditions

# Create temporary array of nodes "u" and set boundary node values for desired Dirichlet BCs.
# In this case we want "left" to be 1.0 and "right" to be 0.0 (which it already is because of how we created "u")
u = basis.zeros()
u[basis.get_dofs("left")] = 1.0

# Add BCs to A and b.
# "x=u" sets the boundary values for the boundaries specified with "D=...".
# All boundaries not specified with "D=..." have Neumann BC equal to 0.
# If a desired flux is needed at a boundary, check out Example 24 that has a parabolic velocity flow at an inlet.
A, b = enforce(A, b, x=u, D=basis.get_dofs(["left", "right"]))

# solve the linear system
x = solve(A, b)

# plot using matplotlib
mesh.plot(x, shading="gouraud", colorbar=True).show()
# or, save to external file:
mesh.save("output_initial0_lefteq1.vtk", point_data={"solution": x})
