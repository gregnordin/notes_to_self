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
    return 1.0 * v


A = laplace.assemble(basis)
b = rhs.assemble(basis)

# Dirichlet boundary conditions
A, b = enforce(A, b, D=mesh.boundary_nodes())

# solve the linear system
x = solve(A, b)

# plot using matplotlib
mesh.plot(x, shading="gouraud", colorbar=True).show()
# or, save to external file:
mesh.save("output.vtk", point_data={"solution": x})
