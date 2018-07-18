## Information

- See [Intra-Package References](https://docs.python.org/3.6/tutorial/modules.html#intra-package-references) for how to import from one module to another within a package. It's easy (relative import with `import .mycolors as mycolors` or absolute import with `import microfluidicdesign.mycolors as mycolors`)
- Good info at [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/). This makes things very clear.

## 3 Ways to import modules in a single-level package

Assumptions:

- Package directory contains only a single level of files (no sub-packages)
- Python file in which package will be included is in the same directory as the package directory
    - Alternatively, the package directory could be included in `PYTHONPATH` in the shell or be added to `sys.path` in the calling program or already be in the path

### No `__init__.py`

See `blank_init`:

    ├── pkg
    │   ├── a.py
    │   └── b.py
    └── tryit.py

tryit.py:

    # Method 1
    import pkg.a, pkg.b
    a2 = pkg.a.A2()
    b2 = pkg.b.B2()
    
    # Method 2
    from pkg.a import A1
    from pkg.b import B1
    a1 = A1()
    b1 = B1()
    


### Import modules in `__init__.py`

See `init_import_modules`:

    ├── pkg
    │   ├── __init__.py
    │   ├── a.py
    │   └── b.py
    └── tryit.py

`__init__.py`:
    
    import pkg.a
    import pkg.b

tryit.py:

    import pkg as pg
    
    a1 = pg.a.A1()
    a2 = pg.a.A2()
    b1 = pg.b.B1()
    b2 = pg.b.B2()


### Import items from modules in `__init__.py`

See `init_import_things_in_modules`:

    ├── pkg
    │   ├── __init__.py
    │   ├── a.py
    │   └── b.py
    └── tryit.py


`__init__.py`:
    
    from pkg.a import A1, A2
    from pkg.b import B1, B2

tryit.py:
        
    import pkg as pg
    
    a1 = pg.A1()
    a2 = pg.A2()
    b1 = pg.B1()
    b2 = pg.B2()

Alternative `__init__.py`:
    
    from .a import A1, A2
    from .b import B1, B2

This uses relative imports whereas the first one uses absolute imports.
