# Install latest version of `fenicsx`

Problem: my conda installation on my Apple Silicon macbook pro is for Intel x86 architecture and I need `fenicsx` to run natively on Apple Silicon. 

## What architecture python is running?

How to tell which architecture python is running on ([How to get architecture of running Python interpreter on MacOS with Apple Silicon?](https://stackoverflow.com/questions/71548156/how-to-get-architecture-of-running-python-interpreter-on-macos-with-apple-silico)):

    python -c "import platform; print(platform.processor())"
      The output is as following:
      On an M1/M2 Mac --> arm
      On an older Mac --> i386

## Install `fenicsx` - 1/9/24

Create fenicsx environment. This will use the latest python version available.

    conda create -n fenicsx-env
    conda activate fenicsx-env
    python3 -c "import platform; print(platform.processor())"
        arm

Install packages for Apple Silicon:

    conda install --override-channels -c conda-forge/osx-arm64 -c conda-forge/noarch fenics-dolfinx mpich pyvista
    
    which python
        /Users/nordin/opt/miniconda3/envs/fenicsx-env/bin/python
    python --version
        Python 3.12.1



## Install `fenicsx` - 1/9/24 - OLD & WRONG

Create python 3.11 arm64 (Apple Silicon) environment:

    CONDA_SUBDIR=osx-arm64 conda create -n py311_arm python=3.11 -c conda-forge --override-channels
    
    conda activate py311_arm
    python -c "import platform; print(platform.processor())"
        arm

With `py311_arm` activated, create fenicsx environment:

    conda create -n fenicsx-env
    conda activate fenicsx-env
    python3 -c "import platform; print(platform.processor())"
        arm

Install packages for Apple Silicon:

    conda install --override-channels -c conda-forge/osx-arm64 -c conda-forge/noarch fenics-dolfinx mpich pyvista
    
    which python
        /Users/nordin/opt/miniconda3/envs/fenicsx-env/bin/python
    python --version
        Python 3.12.1

