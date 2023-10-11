# Purpose: update code to current version.
# Code is from end of first chapter, "Quick overview of the finite element method"
# in [Introduction to Numerical Methods for Variational Problems by Hans Petter Langtangen and Kent-Andre Mardal]
# (https://github.com/hplgit/fem-book)

# STATUS: UNFINISHED!

# from dolfinx import *
from dolfinx import mesh
from dolfinx.fem import FunctionSpace
from dolfinx import fem
import ufl

mesh_ = mesh.RectangleMesh((-1, -1), (1, 1), nx=10, ny=10)
V = FunctionSpace(mesh_, ’P’, 2) # quadratic polynomials
# bc = DirichletBC(V, 0, ’on_boundary’)
bc = fem.dirichletbc()
u = ufl.TrialFunction(V)
v = ufl.TestFunction(V)
a = dot(grad(u), grad(v))*dx
L = f*v*dx
u = Function(V) # unknown FEM function to be computed
solve(a == L, u, bc)
vtkfile = File(’poisson.pvd’); vtkfile << u # store solution