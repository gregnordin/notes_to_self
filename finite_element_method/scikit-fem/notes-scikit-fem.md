# Purpose

Try latest `panel` version with jupyterlab.

# Info

- [scikit-fem](https://github.com/kinnala/scikit-fem?tab=readme-ov-file)

  - > `scikit-fem` is a pure Python 3.8+ library for performing [finite element assembly](https://en.wikipedia.org/wiki/Finite_element_method). Its main purpose is the transformation of bilinear forms into sparse matrices and linear forms into vectors.

  - Text of [paper](https://github.com/kinnala/scikit-fem/blob/master/paper/paper.md)
  - [List of examples](https://github.com/kinnala/scikit-fem/blob/master/docs/listofexamples.rst)

# Next

- Poisson equation with mixed boundary conditions.
- Rectangular shape computation region.
- Add spatially-dependent source function.
- Solve time-dependent diffusion case.

# Log

## Thu, 4/4/24

### Create environment

```
micromamba create -n scikit-fem python ipykernel
micromamba activate scikit-fem
pip install scikit-fem[all]
python -m ipykernel install --user --name scikit-fem --display-name="scikit-fem"
```

### Try Examples 1, 7, 13

Files: `ex01.py`, `ex07.py`, `ex13.py`

- Each file runs and produces output.
- I can look at the vtk output file from the first example, but was unable to produce output files for the other two examples &rarr; I need to understand the classes and their content and structure.

### Look at mesh and basis

- Create `meshes.ipynb` and look at `MeshTriP1` and `MeshQuad1` with first order elements.



