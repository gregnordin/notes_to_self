# Purpose

Try latest `panel` version with jupyterlab.

# Info

- [scikit-fem](https://github.com/kinnala/scikit-fem?tab=readme-ov-file)

  - > `scikit-fem` is a pure Python 3.8+ library for performing [finite element assembly](https://en.wikipedia.org/wiki/Finite_element_method). Its main purpose is the transformation of bilinear forms into sparse matrices and linear forms into vectors.

  - Text of [paper](https://github.com/kinnala/scikit-fem/blob/master/paper/paper.md)
  - [List of examples](https://github.com/kinnala/scikit-fem/blob/master/docs/listofexamples.rst)

# Log

## Thu, 4/4/24

### Create environment

```
micromamba create -n scikit-fem python ipykernel
micromamba activate scikit-fem
pip install scikit-fem[all]
python -m ipykernel install --user --name scikit-fem --display-name="scikit-fem"
```





