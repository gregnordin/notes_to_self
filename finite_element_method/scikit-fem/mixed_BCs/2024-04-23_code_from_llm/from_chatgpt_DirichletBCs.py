# Changes from ChatGPT code:
# mesh.refine(3) -> mesh.refined(3)
# boundary_dofs = D["all"].all() -> boundary_dofs = D.all()

import numpy as np
from skfem import *
from skfem.models.poisson import laplace, unit_load

# Step 1: Create a mesh
mesh = MeshTri.init_symmetric()
mesh.refined(3)

# Step 2: Define the element and basis
element = ElementTriP1()
basis = InteriorBasis(mesh, element)

# Step 3: Formulate the problem (LHS: Laplacian, RHS: source term)
A = asm(laplace, basis)
b = asm(unit_load, basis)

# Step 4: Apply boundary conditions
D = basis.get_dofs()
boundary_dofs = D.all()
A, b = enforce(A, b, D=D)

# Step 5: Solve the linear system
u = solve(*condense(A, b, D=D))

# Solution plotting
from skfem.visuals.matplotlib import plot, show

plot(mesh, u, shading="gouraud")
show()
