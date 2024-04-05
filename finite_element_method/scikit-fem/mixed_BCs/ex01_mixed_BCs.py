# from skfem import *
from skfem import MeshTri, Basis, ElementTriP1, BilinearForm, LinearForm, enforce, solve
from skfem.helpers import dot, grad

# create the mesh
mesh = MeshTri().refined(4)
# or, with your own points and elements:
# mesh = MeshTri(points, elements)

basis = Basis(mesh, ElementTriP1())


@BilinearForm
def laplace(u, v, _):
    return dot(grad(u), grad(v))


@LinearForm
def rhs(v, _):
    return 0.0 * v


A = laplace.assemble(basis)
b = rhs.assemble(basis)

# Boundary conditions
u = basis.zeros()
u[basis.get_dofs("left")] = 1.0
# u[basis.get_dofs("right")] = 1.0
A, b = enforce(A, b, x=u, D=mesh.boundary_nodes())

# solve the linear system
x = solve(A, b)

# plot using matplotlib
mesh.plot(x, shading="gouraud", colorbar=True).show()
# or, save to external file:
mesh.save("output_initial0_lefteq1.vtk", point_data={"solution": x})
