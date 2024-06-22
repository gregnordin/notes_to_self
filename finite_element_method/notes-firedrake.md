# Purpose

Document installation and use of Firedrake FEM software.

# Installation

##  6/21/24

### Initial install-fix problem

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

### Make alias

Add the following to `.bash_profile`:

```
alias activate_firedrake='. /Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/bin/activate'
```

### Execute tests

```
activate_firedrake
which python
	/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/bin/python
python --version
	Python 3.11.9
cd /Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/firedrake/

pytest tests/regression/ -k "poisson_strong or stokes_mini or dg_advection"
================================================================ test session starts =================================================================
platform darwin -- Python 3.11.9, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/firedrake
configfile: setup.cfg
plugins: mpi-0.1, anyio-4.4.0, nbval-0.11.0, xdist-3.6.1
collected 3561 items / 3534 deselected / 2 skipped / 27 selected

tests/regression/test_dg_advection.py .F.F                                                                                                     [ 14%]
tests/regression/test_poisson_strong_bcs.py ................F                                                                                  [ 77%]
tests/regression/test_poisson_strong_bcs_nitsche.py ....                                                                                       [ 92%]
tests/regression/test_stokes_mini.py ..                                                                                                        [100%]

====================================================================== FAILURES ======================================================================
___________________________________________________ test_dg_advection_icosahedral_sphere_parallel ____________________________________________________

args = (), kwargs = {}

    def parallel_callback(*args, **kwargs):
>       subprocess.run(cmd, check=True)

../pytest-mpi/pytest_mpi.py:192:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

input = None, capture_output = False, timeout = None, check = True
popenargs = (['mpiexec', '-n', '1', '-genv', '_PYTEST_MPI_CHILD_PROCESS', '1', ...],), kwargs = {}
process = <Popen: returncode: 1 args: ['mpiexec', '-n', '1', '-genv', '_PYTEST_MPI_CHI...>, stdout = None, stderr = None, retcode = 1

    def run(*popenargs,
            input=None, capture_output=False, timeout=None, check=False, **kwargs):
        """Run command with arguments and return a CompletedProcess instance.

        The returned instance will have attributes args, returncode, stdout and
        stderr. By default, stdout and stderr are not captured, and those attributes
        will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them,
        or pass capture_output=True to capture both.

        If check is True and the exit code was non-zero, it raises a
        CalledProcessError. The CalledProcessError object will have the return code
        in the returncode attribute, and output & stderr attributes if those streams
        were captured.

        If timeout is given, and the process takes too long, a TimeoutExpired
        exception will be raised.

        There is an optional argument "input", allowing you to
        pass bytes or a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it will be used internally.

        By default, all communication is in bytes, and therefore any "input" should
        be bytes, and the stdout and stderr will be bytes. If in text mode, any
        "input" should be a string, and stdout and stderr will be strings decoded
        according to locale encoding, or by "encoding" if set. Text mode is
        triggered by setting any of text, encoding, errors or universal_newlines.

        The other arguments are the same as for the Popen constructor.
        """
        if input is not None:
            if kwargs.get('stdin') is not None:
                raise ValueError('stdin and input arguments may not both be used.')
            kwargs['stdin'] = PIPE

        if capture_output:
            if kwargs.get('stdout') is not None or kwargs.get('stderr') is not None:
                raise ValueError('stdout and stderr arguments may not be used '
                                 'with capture_output.')
            kwargs['stdout'] = PIPE
            kwargs['stderr'] = PIPE

        with Popen(*popenargs, **kwargs) as process:
            try:
                stdout, stderr = process.communicate(input, timeout=timeout)
            except TimeoutExpired as exc:
                process.kill()
                if _mswindows:
                    # Windows accumulates the output in a single blocking
                    # read() call run on child threads, with the timeout
                    # being done in a join() on those threads.  communicate()
                    # _after_ kill() is required to collect that and add it
                    # to the exception.
                    exc.stdout, exc.stderr = process.communicate()
                else:
                    # POSIX _communicate already populated the output so
                    # far into the TimeoutExpired exception.
                    process.wait()
                raise
            except:  # Including KeyboardInterrupt, communicate handled that.
                process.kill()
                # We don't call process.wait() as .__exit__ does that for us.
                raise
            retcode = process.poll()
            if check and retcode:
>               raise CalledProcessError(retcode, process.args,
                                         output=stdout, stderr=stderr)
E               subprocess.CalledProcessError: Command '['mpiexec', '-n', '1', '-genv', '_PYTEST_MPI_CHILD_PROCESS', '1', 'python', '-m', 'pytest', '--runxfail', '-s', '-q', '/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/firedrake/tests/regression/test_dg_advection.py::test_dg_advection_icosahedral_sphere_parallel', ':', '-n', '2', 'python', '-m', 'pytest', '--runxfail', '-s', '-q', '/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/firedrake/tests/regression/test_dg_advection.py::test_dg_advection_icosahedral_sphere_parallel', '--tb=no', '--no-summary', '--no-header', '--disable-warnings', '--show-capture=no']' returned non-zero exit status 1.

/Users/nordin/micromamba/envs/py311/lib/python3.11/subprocess.py:571: CalledProcessError
---------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------
FFF
1 failed, 1 warning in 4.13s

1 failed, 1 warning in 4.13s

=================================== FAILURES ===================================
________________ test_dg_advection_icosahedral_sphere_parallel _________________

    @pytest.mark.parallel(nprocs=3)
    def test_dg_advection_icosahedral_sphere_parallel():
>       run_test(UnitIcosahedralSphereMesh(refinement_level=3))

tests/regression/test_dg_advection.py:74:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

mesh = Mesh(VectorElement(FiniteElement('Lagrange', Cell(triangle, 3), 1), dim=3), 0)

    def run_test(mesh):
        x = SpatialCoordinate(mesh)
        mesh.init_cell_orientations(x)

        V = FunctionSpace(mesh, "DG", 0)
        M = VectorFunctionSpace(mesh, "CG", 1)

        # advecting velocity
        u0 = as_vector((-x[1]*(1 - x[2]*x[2]), x[0]*(1 - x[2]*x[2]), Constant(0)))
        u = Function(M).interpolate(u0)

        dt = (pi/3) * 0.006
        Dt = Constant(dt)

        phi = TestFunction(V)
        D = TrialFunction(V)

        n = FacetNormal(mesh)

        un = 0.5 * (dot(u, n) + abs(dot(u, n)))

        a_mass = inner(D, phi) * dx
        a_int = inner(-u*D, grad(phi))*dx
        a_flux = inner(un('+')*D('+') - un('-')*D('-'), jump(phi))*dS
        arhs = a_mass - Dt * (a_int + a_flux)

        dD1 = Function(V)
        D1 = Function(V)

        D0 = conditional(le(real(x[0]), 0), 1, 0.0)
        D = Function(V).interpolate(D0)

        t = 0.0
        T = 10*dt

        problem = LinearVariationalProblem(a_mass, action(arhs, D1), dD1)
        solver = LinearVariationalSolver(problem, solver_parameters={'ksp_type': 'cg'})

        L2_0 = norm(D)
        Dbar_0 = assemble(D*dx)
        while t < (T - dt/2):
            D1.assign(D)
            solver.solve()
            D1.assign(dD1)

            solver.solve()
            D1.assign(0.75*D + 0.25*dD1)
            solver.solve()
            D.assign((1.0/3.0)*D + (2.0/3.0)*dD1)

            t += dt

        L2_T = norm(D)
        Dbar_T = assemble(D*dx)

        # L2 norm decreases
        assert L2_T < L2_0

        # Mass conserved
>       assert np.allclose(Dbar_T, Dbar_0)
E       assert False
E        +  where False = <function allclose at 0x10bb59b70>(np.float64(0.00010694428099914108), np.float64(6.314952848718281))
E        +    where <function allclose at 0x10bb59b70> = np.allclose

tests/regression/test_dg_advection.py:65: AssertionError
=============================== warnings summary ===============================
../fiat/FIAT/__init__.py:5
  /Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/fiat/FIAT/__init__.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    import pkg_resources

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED tests/regression/test_dg_advection.py::test_dg_advection_icosahedral_sphere_parallel
1 failed, 1 warning in 4.13s
WARNING! There are options you set that were not used!
WARNING! could be spelling mistake, etc!
There are 3 unused database options. They are:
Option left: name:--runxfail (no value) source: command line
Option left: name:-q value: /Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/firedrake/tests/regression/test_dg_advection.py::test_dg_advection_icosahedral_sphere_parallel source: command line
Option left: name:-s (no value) source: command line
---------------------------------------------------------------- Captured stderr call ----------------------------------------------------------------
firedrake:WARNING OMP_NUM_THREADS is not set or is set to a value greater than 1, we suggest setting OMP_NUM_THREADS=1 to improve performance
______________________________________________________ test_dg_advection_cubed_sphere_parallel _______________________________________________________

args = (), kwargs = {}

    def parallel_callback(*args, **kwargs):
>       subprocess.run(cmd, check=True)

../pytest-mpi/pytest_mpi.py:192:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

input = None, capture_output = False, timeout = None, check = True
popenargs = (['mpiexec', '-n', '1', '-genv', '_PYTEST_MPI_CHILD_PROCESS', '1', ...],), kwargs = {}
process = <Popen: returncode: 15 args: ['mpiexec', '-n', '1', '-genv', '_PYTEST_MPI_CH...>, stdout = None, stderr = None, retcode = 15

    def run(*popenargs,
            input=None, capture_output=False, timeout=None, check=False, **kwargs):
        """Run command with arguments and return a CompletedProcess instance.

        The returned instance will have attributes args, returncode, stdout and
        stderr. By default, stdout and stderr are not captured, and those attributes
        will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them,
        or pass capture_output=True to capture both.

        If check is True and the exit code was non-zero, it raises a
        CalledProcessError. The CalledProcessError object will have the return code
        in the returncode attribute, and output & stderr attributes if those streams
        were captured.

        If timeout is given, and the process takes too long, a TimeoutExpired
        exception will be raised.

        There is an optional argument "input", allowing you to
        pass bytes or a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it will be used internally.

        By default, all communication is in bytes, and therefore any "input" should
        be bytes, and the stdout and stderr will be bytes. If in text mode, any
        "input" should be a string, and stdout and stderr will be strings decoded
        according to locale encoding, or by "encoding" if set. Text mode is
        triggered by setting any of text, encoding, errors or universal_newlines.

        The other arguments are the same as for the Popen constructor.
        """
        if input is not None:
            if kwargs.get('stdin') is not None:
                raise ValueError('stdin and input arguments may not both be used.')
            kwargs['stdin'] = PIPE

        if capture_output:
            if kwargs.get('stdout') is not None or kwargs.get('stderr') is not None:
                raise ValueError('stdout and stderr arguments may not be used '
                                 'with capture_output.')
            kwargs['stdout'] = PIPE
            kwargs['stderr'] = PIPE

        with Popen(*popenargs, **kwargs) as process:
            try:
                stdout, stderr = process.communicate(input, timeout=timeout)
            except TimeoutExpired as exc:
                process.kill()
                if _mswindows:
                    # Windows accumulates the output in a single blocking
                    # read() call run on child threads, with the timeout
                    # being done in a join() on those threads.  communicate()
                    # _after_ kill() is required to collect that and add it
                    # to the exception.
                    exc.stdout, exc.stderr = process.communicate()
                else:
                    # POSIX _communicate already populated the output so
                    # far into the TimeoutExpired exception.
                    process.wait()
                raise
            except:  # Including KeyboardInterrupt, communicate handled that.
                process.kill()
                # We don't call process.wait() as .__exit__ does that for us.
                raise
            retcode = process.poll()
            if check and retcode:
>               raise CalledProcessError(retcode, process.args,
                                         output=stdout, stderr=stderr)
E               subprocess.CalledProcessError: Command '['mpiexec', '-n', '1', '-genv', '_PYTEST_MPI_CHILD_PROCESS', '1', 'python', '-m', 'pytest', '--runxfail', '-s', '-q', '/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/firedrake/tests/regression/test_dg_advection.py::test_dg_advection_cubed_sphere_parallel', ':', '-n', '2', 'python', '-m', 'pytest', '--runxfail', '-s', '-q', '/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/firedrake/tests/regression/test_dg_advection.py::test_dg_advection_cubed_sphere_parallel', '--tb=no', '--no-summary', '--no-header', '--disable-warnings', '--show-capture=no']' returned non-zero exit status 15.

/Users/nordin/micromamba/envs/py311/lib/python3.11/subprocess.py:571: CalledProcessError
---------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------

===================================================================================
=   BAD TERMINATION OF ONE OF YOUR APPLICATION PROCESSES
=   PID 66594 RUNNING AT ECEns-MacBook-Pro-8.local
=   EXIT CODE: 6
=   CLEANING UP REMAINING PROCESSES
=   YOU CAN IGNORE THE BELOW CLEANUP MESSAGES
===================================================================================
YOUR APPLICATION TERMINATED WITH THE EXIT STRING: Terminated: 15 (signal 15)
This typically refers to a problem with your application.
Please see the FAQ page for debugging suggestions
---------------------------------------------------------------- Captured stderr call ----------------------------------------------------------------
firedrake:WARNING OMP_NUM_THREADS is not set or is set to a value greater than 1, we suggest setting OMP_NUM_THREADS=1 to improve performance
Fatal Python error: Aborted

Current thread 0x00000001f9d7bac0 (most recent call first):
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/firedrake/firedrake/variational_solver.py", line 324 in solve
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/firedrake/firedrake/adjoint_utils/variational_solver.py", line 89 in wrapper
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/firedrake/tests/regression/test_dg_advection.py", line 53 in run_test
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/firedrake/tests/regression/test_dg_advection.py", line 83 in test_dg_advection_cubed_sphere_parallel
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/_pytest/python.py", line 162 in pytest_pyfunc_call
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/_pytest/python.py", line 1632 in runtest
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/_pytest/runner.py", line 173 in pytest_runtest_call
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/_pytest/runner.py", line 241 in <lambda>
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/_pytest/runner.py", line 341 in from_call
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/_pytest/runner.py", line 240 in call_and_report
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/_pytest/runner.py", line 135 in runtestprotocol
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/_pytest/runner.py", line 116 in pytest_runtest_protocol
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/_pytest/main.py", line 364 in pytest_runtestloop
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/_pytest/main.py", line 339 in _main
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/_pytest/main.py", line 285 in wrap_session
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/_pytest/main.py", line 332 in pytest_cmdline_main
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_callers.py", line 103 in _multicall
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pluggy/_hooks.py", line 513 in __call__
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/_pytest/config/__init__.py", line 178 in main
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/_pytest/config/__init__.py", line 206 in console_main
  File "/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/lib/python3.11/site-packages/pytest/__main__.py", line 7 in <module>
  File "<frozen runpy>", line 88 in _run_code
  File "<frozen runpy>", line 198 in _run_module_as_main

Extension modules: mpi4py.MPI, zmq.backend.cython._zmq, tornado.speedups, petsc4py.PETSc, numpy._core._multiarray_umath, numpy._core._multiarray_tests, numpy.linalg._umath_linalg, pyop2.sparsity, scipy._lib._ccallback_c, scipy.special._ufuncs_cxx, scipy.special._cdflib, scipy.special._ufuncs, numpy.random._common, numpy.random.bit_generator, numpy.random._bounded_integers, numpy.random._mt19937, numpy.random.mtrand, numpy.random._philox, numpy.random._pcg64, numpy.random._sfc64, numpy.random._generator, charset_normalizer.md, scipy.special._specfun, scipy.special._comb, scipy.linalg._fblas, scipy.linalg._flapack, scipy.linalg.cython_lapack, scipy.linalg._cythonized_array_utils, scipy.linalg._solve_toeplitz, scipy.linalg._decomp_lu_cython, scipy.linalg._matfuncs_sqrtm_triu, scipy.linalg.cython_blas, scipy.linalg._matfuncs_expm, scipy.linalg._decomp_update, scipy.sparse._sparsetools, _csparsetools, scipy.sparse._csparsetools, scipy.sparse.linalg._dsolve._superlu, scipy.sparse.linalg._eigen.arpack._arpack, scipy.sparse.linalg._propack._spropack, scipy.sparse.linalg._propack._dpropack, scipy.sparse.linalg._propack._cpropack, scipy.sparse.linalg._propack._zpropack, scipy.sparse.csgraph._tools, scipy.sparse.csgraph._shortest_path, scipy.sparse.csgraph._traversal, scipy.sparse.csgraph._min_spanning_tree, scipy.sparse.csgraph._flow, scipy.sparse.csgraph._matching, scipy.sparse.csgraph._reordering, scipy.special._ellip_harm_2, symengine.lib.symengine_wrapper, firedrake.cython.dmcommon, firedrake.cython.extrusion_numbering, firedrake.cython.spatialindex, firedrake.cython.patchimpl, h5py._errors, h5py.defs, h5py._objects, h5py.h5, h5py.utils, h5py.h5t, h5py.h5s, h5py.h5ac, h5py.h5p, h5py.h5r, h5py._proxy, h5py._conv, h5py.h5z, h5py.h5a, h5py.h5d, h5py.h5ds, h5py.h5g, h5py.h5i, h5py.h5o, h5py.h5f, h5py.h5fd, h5py.h5pl, h5py.h5l, h5py._selector, firedrake.cython.hdf5interface, firedrake.cython.mgimpl, vtkmodules.vtkCommonCore, vtkmodules.vtkCommonMath, vtkmodules.vtkCommonTransforms, vtkmodules.vtkCommonDataModel, PIL._imaging, kiwisolver._cext (total: 88)
_______________________________________________________ test_poisson_analytic_linear_parallel ________________________________________________________

args = (), kwargs = {}

    def parallel_callback(*args, **kwargs):
>       subprocess.run(cmd, check=True)

../pytest-mpi/pytest_mpi.py:192:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

input = None, capture_output = False, timeout = None, check = True
popenargs = (['mpiexec', '-n', '1', '-genv', '_PYTEST_MPI_CHILD_PROCESS', '1', ...],), kwargs = {}
process = <Popen: returncode: 1 args: ['mpiexec', '-n', '1', '-genv', '_PYTEST_MPI_CHI...>, stdout = None, stderr = None, retcode = 1

    def run(*popenargs,
            input=None, capture_output=False, timeout=None, check=False, **kwargs):
        """Run command with arguments and return a CompletedProcess instance.

        The returned instance will have attributes args, returncode, stdout and
        stderr. By default, stdout and stderr are not captured, and those attributes
        will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them,
        or pass capture_output=True to capture both.

        If check is True and the exit code was non-zero, it raises a
        CalledProcessError. The CalledProcessError object will have the return code
        in the returncode attribute, and output & stderr attributes if those streams
        were captured.

        If timeout is given, and the process takes too long, a TimeoutExpired
        exception will be raised.

        There is an optional argument "input", allowing you to
        pass bytes or a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it will be used internally.

        By default, all communication is in bytes, and therefore any "input" should
        be bytes, and the stdout and stderr will be bytes. If in text mode, any
        "input" should be a string, and stdout and stderr will be strings decoded
        according to locale encoding, or by "encoding" if set. Text mode is
        triggered by setting any of text, encoding, errors or universal_newlines.

        The other arguments are the same as for the Popen constructor.
        """
        if input is not None:
            if kwargs.get('stdin') is not None:
                raise ValueError('stdin and input arguments may not both be used.')
            kwargs['stdin'] = PIPE

        if capture_output:
            if kwargs.get('stdout') is not None or kwargs.get('stderr') is not None:
                raise ValueError('stdout and stderr arguments may not be used '
                                 'with capture_output.')
            kwargs['stdout'] = PIPE
            kwargs['stderr'] = PIPE

        with Popen(*popenargs, **kwargs) as process:
            try:
                stdout, stderr = process.communicate(input, timeout=timeout)
            except TimeoutExpired as exc:
                process.kill()
                if _mswindows:
                    # Windows accumulates the output in a single blocking
                    # read() call run on child threads, with the timeout
                    # being done in a join() on those threads.  communicate()
                    # _after_ kill() is required to collect that and add it
                    # to the exception.
                    exc.stdout, exc.stderr = process.communicate()
                else:
                    # POSIX _communicate already populated the output so
                    # far into the TimeoutExpired exception.
                    process.wait()
                raise
            except:  # Including KeyboardInterrupt, communicate handled that.
                process.kill()
                # We don't call process.wait() as .__exit__ does that for us.
                raise
            retcode = process.poll()
            if check and retcode:
>               raise CalledProcessError(retcode, process.args,
                                         output=stdout, stderr=stderr)
E               subprocess.CalledProcessError: Command '['mpiexec', '-n', '1', '-genv', '_PYTEST_MPI_CHILD_PROCESS', '1', 'python', '-m', 'pytest', '--runxfail', '-s', '-q', '/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/firedrake/tests/regression/test_poisson_strong_bcs.py::test_poisson_analytic_linear_parallel', ':', '-n', '1', 'python', '-m', 'pytest', '--runxfail', '-s', '-q', '/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/firedrake/tests/regression/test_poisson_strong_bcs.py::test_poisson_analytic_linear_parallel', '--tb=no', '--no-summary', '--no-header', '--disable-warnings', '--show-capture=no']' returned non-zero exit status 1.

/Users/nordin/micromamba/envs/py311/lib/python3.11/subprocess.py:571: CalledProcessError
---------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------
[1] error: 12.124355652982139
F[0] error: 12.124355652982139
F
1 failed, 1 warning in 0.88s

=================================== FAILURES ===================================
____________________ test_poisson_analytic_linear_parallel _____________________

    @pytest.mark.parallel(nprocs=2)
    def test_poisson_analytic_linear_parallel():
        from mpi4py import MPI
        error = run_test_linear(1, 1)
        print('[%d]' % MPI.COMM_WORLD.rank, 'error:', error)
>       assert error < 5e-6
E       assert 12.124355652982139 < 5e-06

tests/regression/test_poisson_strong_bcs.py:92: AssertionError
=============================== warnings summary ===============================
../fiat/FIAT/__init__.py:5
  /Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/fiat/FIAT/__init__.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    import pkg_resources

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED tests/regression/test_poisson_strong_bcs.py::test_poisson_analytic_linear_parallel
1 failed, 1 warning in 0.88s
WARNING! There are options you set that were not used!
WARNING! could be spelling mistake, etc!
There are 3 unused database options. They are:
Option left: name:--runxfail (no value) source: command line
Option left: name:-q value: /Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/firedrake/tests/regression/test_poisson_strong_bcs.py::test_poisson_analytic_linear_parallel source: command line
Option left: name:-s (no value) source: command line
---------------------------------------------------------------- Captured stderr call ----------------------------------------------------------------
firedrake:WARNING OMP_NUM_THREADS is not set or is set to a value greater than 1, we suggest setting OMP_NUM_THREADS=1 to improve performance
================================================================== warnings summary ==================================================================
../fiat/FIAT/__init__.py:5
  /Users/nordin/Documents/Projects/notes_to_self/finite_element_method/firedrake/src/fiat/FIAT/__init__.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    import pkg_resources

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================================================== short test summary info ===============================================================
FAILED tests/regression/test_dg_advection.py::test_dg_advection_icosahedral_sphere_parallel - subprocess.CalledProcessError: Command '['mpiexec', '-n', '1', '-genv', '_PYTEST_MPI_CHILD_PROCESS', '1', 'python', '-m', 'pytest', '--runxfail',...
FAILED tests/regression/test_dg_advection.py::test_dg_advection_cubed_sphere_parallel - subprocess.CalledProcessError: Command '['mpiexec', '-n', '1', '-genv', '_PYTEST_MPI_CHILD_PROCESS', '1', 'python', '-m', 'pytest', '--runxfail',...
FAILED tests/regression/test_poisson_strong_bcs.py::test_poisson_analytic_linear_parallel - subprocess.CalledProcessError: Command '['mpiexec', '-n', '1', '-genv', '_PYTEST_MPI_CHILD_PROCESS', '1', 'python', '-m', 'pytest', '--runxfail',...
=================================== 3 failed, 24 passed, 2 skipped, 3534 deselected, 1 warning in 69.31s (0:01:09) ===================================
WARNING! There are options you set that were not used!
WARNING! could be spelling mistake, etc!
There is one unused database option. It is:
Option left: name:-k value: poisson_strong or stokes_mini or dg_advection source: command line
```

### Install as Jupyter kernel

```
pip install ipykernel
  Requirement already satisfied: ipykernel in ./lib/python3.11/site-packages (6.29.4)
  Requirement already satisfied: appnope in ./lib/python3.11/site-packages (from ipykernel) (0.1.4)
  Requirement already satisfied: comm>=0.1.1 in ./lib/python3.11/site-packages (from ipykernel) (0.2.2)
  Requirement already satisfied: debugpy>=1.6.5 in ./lib/python3.11/site-packages (from ipykernel) (1.8.1)
  Requirement already satisfied: ipython>=7.23.1 in ./lib/python3.11/site-packages (from ipykernel) (8.25.0)
  Requirement already satisfied: jupyter-client>=6.1.12 in ./lib/python3.11/site-packages (from ipykernel) (8.6.2)
  Requirement already satisfied: jupyter-core!=5.0.*,>=4.12 in ./lib/python3.11/site-packages (from ipykernel) (5.7.2)
  Requirement already satisfied: matplotlib-inline>=0.1 in ./lib/python3.11/site-packages (from ipykernel) (0.1.7)
  Requirement already satisfied: nest-asyncio in ./lib/python3.11/site-packages (from ipykernel) (1.6.0)
  Requirement already satisfied: packaging in ./lib/python3.11/site-packages (from ipykernel) (24.1)
  Requirement already satisfied: psutil in ./lib/python3.11/site-packages (from ipykernel) (6.0.0)
  Requirement already satisfied: pyzmq>=24 in ./lib/python3.11/site-packages (from ipykernel) (26.0.3)
  Requirement already satisfied: tornado>=6.1 in ./lib/python3.11/site-packages (from ipykernel) (6.4.1)
  Requirement already satisfied: traitlets>=5.4.0 in ./lib/python3.11/site-packages (from ipykernel) (5.14.3)
  Requirement already satisfied: decorator in ./lib/python3.11/site-packages (from ipython>=7.23.1->ipykernel) (4.4.2)
  Requirement already satisfied: jedi>=0.16 in ./lib/python3.11/site-packages (from ipython>=7.23.1->ipykernel) (0.19.1)
  Requirement already satisfied: prompt-toolkit<3.1.0,>=3.0.41 in ./lib/python3.11/site-packages (from ipython>=7.23.1->ipykernel) (3.0.47)
  Requirement already satisfied: pygments>=2.4.0 in ./lib/python3.11/site-packages (from ipython>=7.23.1->ipykernel) (2.18.0)
  Requirement already satisfied: stack-data in ./lib/python3.11/site-packages (from ipython>=7.23.1->ipykernel) (0.6.3)
  Requirement already satisfied: typing-extensions>=4.6 in ./lib/python3.11/site-packages (from ipython>=7.23.1->ipykernel) (4.12.2)
  Requirement already satisfied: pexpect>4.3 in ./lib/python3.11/site-packages (from ipython>=7.23.1->ipykernel) (4.9.0)
  Requirement already satisfied: python-dateutil>=2.8.2 in ./lib/python3.11/site-packages (from jupyter-client>=6.1.12->ipykernel) (2.9.0.post0)
  Requirement already satisfied: platformdirs>=2.5 in ./lib/python3.11/site-packages (from jupyter-core!=5.0.*,>=4.12->ipykernel) (4.2.2)
  Requirement already satisfied: parso<0.9.0,>=0.8.3 in ./lib/python3.11/site-packages (from jedi>=0.16->ipython>=7.23.1->ipykernel) (0.8.4)
  Requirement already satisfied: ptyprocess>=0.5 in ./lib/python3.11/site-packages (from pexpect>4.3->ipython>=7.23.1->ipykernel) (0.7.0)
  Requirement already satisfied: wcwidth in ./lib/python3.11/site-packages (from prompt-toolkit<3.1.0,>=3.0.41->ipython>=7.23.1->ipykernel) (0.2.13)
  Requirement already satisfied: six>=1.5 in ./lib/python3.11/site-packages (from python-dateutil>=2.8.2->jupyter-client>=6.1.12->ipykernel) (1.16.0)
  Requirement already satisfied: executing>=1.2.0 in ./lib/python3.11/site-packages (from stack-data->ipython>=7.23.1->ipykernel) (2.0.1)
  Requirement already satisfied: asttokens>=2.1.0 in ./lib/python3.11/site-packages (from stack-data->ipython>=7.23.1->ipykernel) (2.4.1)
  Requirement already satisfied: pure-eval in ./lib/python3.11/site-packages (from stack-data->ipython>=7.23.1->ipykernel) (0.2.2)

python -m ipykernel install --user --name firedrake --display-name "firedrake"
	Installed kernelspec firedrake in /Users/nordin/Library/Jupyter/kernels/firedrake
```

### Fix problem with `netgen`

When I try `from netgen.occ import *` I get an error that `netgen` is not installed.

Follow [Install from source -> Build on Mac OS X](https://docu.ngsolve.org/latest/install/installmacnative.html). 

```
export NGROOT=/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/netgen
echo $NGROOT
	/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/netgen
cd $NGROOT
git clone --recurse-submodules https://github.com/NGSolve/ngsolve.git ngsolve-src
  Cloning into 'ngsolve-src'...
  remote: Enumerating objects: 80617, done.
  remote: Counting objects: 100% (3971/3971), done.
  remote: Compressing objects: 100% (849/849), done.
  remote: Total 80617 (delta 3205), reused 3668 (delta 3108), pack-reused 76646
  Receiving objects: 100% (80617/80617), 59.37 MiB | 2.22 MiB/s, done.
  Resolving deltas: 100% (61697/61697), done.
  Submodule 'external_dependencies/netgen' (https://github.com/NGSolve/netgen.git) registered for path 'external_dependencies/netgen'
  Cloning into '/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/netgen/ngsolve-src/external_dependencies/netgen'...
  remote: Enumerating objects: 29783, done.
  remote: Counting objects: 100% (8482/8482), done.
  remote: Compressing objects: 100% (2508/2508), done.
  remote: Total 29783 (delta 6433), reused 7885 (delta 5969), pack-reused 21301
  Receiving objects: 100% (29783/29783), 11.14 MiB | 5.13 MiB/s, done.
  Resolving deltas: 100% (23418/23418), done.
  Submodule path 'external_dependencies/netgen': checked out 'c2f42f2f16d67dfb4aa6e10e3085abeca6d45396'
  Submodule 'external_dependencies/pybind11' (https://github.com/ngsolve/pybind11.git) registered for path 'external_dependencies/netgen/external_dependencies/pybind11'
  Cloning into '/Users/nordin/Documents/Projects/notes_to_self/finite_element_method/netgen/ngsolve-src/external_dependencies/netgen/external_dependencies/pybind11'...
  remote: Enumerating objects: 20348, done.
  remote: Counting objects: 100% (538/538), done.
  remote: Compressing objects: 100% (353/353), done.
  remote: Total 20348 (delta 311), reused 318 (delta 151), pack-reused 19810
  Receiving objects: 100% (20348/20348), 9.38 MiB | 1.20 MiB/s, done.
  Resolving deltas: 100% (13999/13999), done.
  Submodule path 'external_dependencies/netgen/external_dependencies/pybind11': checked out '38bf7b174875c27c1ba98bdf5a9bf13d967f14d4'
```

