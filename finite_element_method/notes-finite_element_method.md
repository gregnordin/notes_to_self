# Purpose

Collect information about the finite element method and software implementation.

# FEM software

<span style="color:red; font-size:150%">&#x2605;</span> [Firedrake](https://www.firedrakeproject.org/index.html) - 2013 branched off of Fenics and is designed for user ease-of-use rather than ultimate flexibility. Recommended 4/21/24 by Patrick Ferrell from U. of Oxford.

[scikit-fem](https://github.com/kinnala/scikit-fem?tab=readme-ov-file) -  I tried this May-June 2024 and liked it.

- > `scikit-fem` is a pure Python 3.8+ library for performing [finite element assembly](https://en.wikipedia.org/wiki/Finite_element_method). Its main purpose is the transformation of bilinear forms into sparse matrices and linear forms into vectors.

- Text of [paper](https://github.com/kinnala/scikit-fem/blob/master/paper/paper.md)

- [List of examples](https://github.com/kinnala/scikit-fem/blob/master/docs/listofexamples.rst)

[FEniCSx/dolfinx](https://github.com/FEniCS/dolfinx) - I tried this Fall 2023 through April 2024 and found it difficult to learn due to jumble of old FEniCS material online and newer but very incomplete FEniCSx documentation.

[Nico Schloemer - Awesome Scientific Computing - Finite Elements section](https://github.com/nschloe/awesome-scientific-computing?tab=readme-ov-file#finite-elements) - good overview of free FEM software.

Some possible FEM codes to look into

- [SfePy: Simple Finite Elements in Python](https://sfepy.org/doc-devel/index.html)

  - > SfePy[1](https://github.com/sfepy/sfepy#fn1) is a software for solving systems of coupled partial differential equations (PDEs) by the finite element method in 1D, 2D and 3D. It can be viewed both as black-box PDE solver, and as a Python package which can be used for building custom applications. The word "simple" means that complex FEM problems can be coded very easily and rapidly.

  - > SfePy uses so called "problem definition files" (also referred to as "input files" or "problem description files"") that describe the partial differential equations (PDEs), boundary conditions, function spaces and other ingredients of the finite element (FE) formulation of a PDE-related problem

  - [Tutorial](https://sfepy.org/doc-devel/tutorial.html)

  - [Notes on solving PDEs by the Finite Element Method](https://sfepy.org/doc-devel/solving_pdes_by_fem.html#sec-solving-pdes-fem)

- [deal.ii](https://www.dealii.org/)

  - > **What it is:** A C++ software library supporting the creation of finite element codes and an open community of users and developers.
    >
    > **Mission:** To provide well-documented tools to build finite element codes for a broad variety of PDEs, from laptops to supercomputers.

- [pyamg](https://github.com/pyamg/pyamg)

  - a library of **Algebraic Multigrid (AMG)** solvers with a convenient Python interface

  - > AMG is a multilevel technique for solving large-scale linear systems with optimal or near-optimal efficiency. Unlike geometric multigrid, AMG requires little or no geometric information about the underlying problem and develops a sequence of coarser grids directly from the input matrix. This feature is especially important for problems discretized on unstructured meshes and irregular grids.

  - [Tutorial](https://github.com/pyamg/pyamg/wiki/Tutorial)





# Learning Resources

- [In-depth tutorial on FEM in a deal.ii code example](https://www.dealii.org/current/doxygen/deal.II/step_3.html) - **very good**.
- [Finite Element Method, youtube channel: Numerical Analysis by Julian Roth](https://www.youtube.com/watch?v=P4lBRuY7pC4) - good overview, 32 min but play at 2x.



# Other - finite volume method

[Clawpack](http://www.clawpack.org)

> a collection of finite volume methods for linear and nonlinear hyperbolic systems of conservation laws. Clawpack employs high-resolution Godunov-type methods with limiters in a general framework applicable to many kinds of waves. Clawpack is written in Fortran and Python.

[FiPy: A Finite Volume PDE Solver Using Python](https://www.ctcms.nist.gov/fipy/index.html)

> [*FiPy*](https://www.ctcms.nist.gov/fipy/documentation/glossary.html#term-fipy) is an object oriented, partial differential equation (PDE) solver, written in [Python](https://www.ctcms.nist.gov/cgi-bin/redirect.py?url=http://www.python.org/), based on a standard finite volume (FV) approach.





















