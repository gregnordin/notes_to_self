# Purpose

Document installation and use of Firedrake FEM software.

# Installation

##  6/21/24

Create python 3.11 virtual environment.

```
conda env create -n py311 python=3.11
conda activate py311
which python
	/Users/nordin/micromamba/envs/py311/bin/python
python --version
	Python 3.11.9
curl -O https://raw.githubusercontent.com/firedrakeproject/firedrake/master/scripts/firedrake-install
python firedrake-install
```



**Change line 738 of `firedrake-install` from ` petsc_options.add("--with-zlib")` to `petsc_options.add("--with-zlib-dir=/opt/homebrew/opt/zlib")` and the installation was successful. This change was made to eliminate the following error**:

```
Successfully cloned repository loopy
Checking out branch main
Successfully checked out branch main
Updating submodules.
Successfully updated submodules.
Installing petsc/
Depending on your platform, PETSc may take an hour or more to build!
Traceback (most recent call last):
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake-install", line 1816, in <module>
    install("petsc/")
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake-install", line 1043, in install
    build_and_install_petsc()
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake-install", line 1155, in build_and_install_petsc
    check_call([python, "./configure", "PETSC_DIR={}".format(petsc_dir), "PETSC_ARCH={}".format(petsc_arch)] + petsc_options)
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake-install", line 672, in check_call
    log.debug(subprocess.check_output(arguments, stderr=subprocess.STDOUT, env=os.environ).decode())
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/nordin/micromamba/envs/py311/lib/python3.11/subprocess.py", line 466, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/nordin/micromamba/envs/py311/lib/python3.11/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/bin/python', './configure', 'PETSC_DIR=/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/petsc', 'PETSC_ARCH=default', '--download-mumps', '--with-fortran-bindings=0', '--with-debugging=0', '--with-zlib', '--download-metis', '--download-ptscotch', '--download-pastix', '--with-c2html=0', '--download-mpich', '--download-hdf5', '--download-pnetcdf', '--download-hypre', '--with-x=0', '--CFLAGS=-Wno-implicit-function-declaration', '--with-shared-libraries=1', '--download-superlu_dist', '--download-netcdf', "--download-openblas-make-options='USE_THREAD=0 USE_LOCKING=1 USE_OPENMP=0'", '--download-mpich-configure-arguments=--disable-opencl', '--download-suitesparse', '--download-hwloc', '--download-openblas', '--LDFLAGS=-Wl,-ld_classic', '--download-bison', '--download-hwloc-configure-arguments=--disable-opencl', '--download-scalapack']' returned non-zero exit status 1.


Install log saved in /Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake-install.log
```

Looking in `firedrake-install.log` we see that this non-zero exit status is from the following problem where `zlib` can't be found:

```
*********************************************************************************************
           UNABLE to CONFIGURE with GIVEN OPTIONS (see configure.log for details):
---------------------------------------------------------------------------------------------
  Unable to find zlib in default locations!
  Perhaps you can specify with --with-zlib-dir=<directory>
  If you do not want zlib, then give --with-zlib=0
  You might also consider using --download-zlib instead
*********************************************************************************************
```

