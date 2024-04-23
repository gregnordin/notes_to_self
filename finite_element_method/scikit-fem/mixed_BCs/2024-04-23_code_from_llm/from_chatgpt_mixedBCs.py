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

# Step 4: Identify boundary facets for Neumann conditions
top_facets = np.nonzero(mesh.facets_satisfying(lambda x: x[1] == 1.0))[0]
bottom_facets = np.nonzero(mesh.facets_satisfying(lambda x: x[1] == 0.0))[0]
print(f"{np.nonzero(mesh.facets_satisfying(lambda x: x[1] == 1.0))=}")
print(f"{np.nonzero(mesh.facets_satisfying(lambda x: x[1] == 0.0))=}")
print(f"{top_facets=}")
print(f"{bottom_facets=}")

# Neumann condition function g (flux value)
g = lambda x: np.zeros(x.shape[1])  # Modify this as per actual conditions

# Assemble Neumann contributions
neumann_dofs = basis.get_dofs(top_facets).all() | basis.get_dofs(bottom_facets).all()
b += asm(neumann, basis, facets=np.hstack([top_facets, bottom_facets]), fn=g)

# Step 5: Apply Dirichlet boundary conditions on left and right boundaries
D = basis.get_dofs()
dirichlet_dofs = np.hstack([D["left"].all(), D["right"].all()])
A, b = enforce(A, b, I=dirichlet_dofs)

# Step 6: Solve the linear system
u = solve(*condense(A, b, I=dirichlet_dofs))

# Solution plotting
from skfem.visuals.matplotlib import plot, show

plot(mesh, u, shading="gouraud")
show()
