December 11, 2019  
G. Nordin


# Purpose

Document how to set up a new python project that has a virtual environment and uses Visual Studio Code and Jupyterlab.

Computer: MacBook Pro with macOS Catalina 10.15.1.


# Set up virtual environment

Make new directory for project

    $ mkdir <directory name>
    $ cd <directory name>

## Create virtual environment
    
    # activate a conda environment on which to base new virtual environment
    $ source activate py37
    # Create new virtual environment
    (py37)
    $ python -m venv .venv --prompt "<virtual environment terminal display name>"
    (py37)
    $ conda deactivate
    # Activate new virtual environment
    $ source .venv/bin/activate
    <virtual environment terminal display name>
    $ pip install --upgrade pip
    <virtual environment terminal display name>
    $ pip list
    Package    Version
    ---------- -------
    pip        19.3.1
    setuptools 40.8.0
    
## Install needed packages
    
    $ pip install jupyterlab ipykernel pylint black <other desired packages>
    $ pip list
    Package               Version
    --------------------- ---------
    appdirs               1.4.3
    appnope               0.1.0
    astroid               2.3.3
    attrs                 19.3.0
    backcall              0.1.0
    black                 19.10b0
    Click                 7.0
    decorator             4.4.1
    ipykernel             5.1.3
    ipython               7.10.1
    ipython-genutils      0.2.0
    isort                 4.3.21
    jedi                  0.15.1
    jupyter-client        5.3.4
    jupyter-core          4.6.1
    lazy-object-proxy     1.4.3
    mccabe                0.6.1
    numpy                 1.17.4
    opencv-contrib-python 4.1.2.30
    parso                 0.5.1
    pathspec              0.6.0
    pexpect               4.7.0
    pickleshare           0.7.5
    Pillow                6.2.1
    pip                   19.3.1
    prompt-toolkit        3.0.2
    ptyprocess            0.6.0
    Pygments              2.5.2
    pylint                2.4.4
    python-dateutil       2.8.1
    pyzmq                 18.1.1
    regex                 2019.12.9
    setuptools            40.8.0
    six                   1.13.0
    toml                  0.10.0
    tornado               6.0.3
    traitlets             4.3.3
    typed-ast             1.4.0
    wcwidth               0.1.7
    wrapt                 1.11.2
    $ pip freeze > requirements.txt

# Set up VSCode

Open VSCode:

    # Make sure virtual environment is deactivated so it doesn't interfere with VSCode terminal
    $ deactivate
    $ code .
    
Make the virtual environment the active python installation:

- Go to bottom left of VSCode window
- Click on the Python version
- This brings up a pop up menu; select the `./.venv/bin/python` option

Note: this now gives VSCode access to `black` installed in this virtual environment. Also, it adds the line, `  "python.pythonPath": ".venv/bin/python",` to `./.vscode/settings.json`

Make sure that that `./.vscode/settings.json` looks like this:

    {
      "python.formatting.provider": "black",
      "python.formatting.blackArgs": ["--line-length=90"],
      "editor.formatOnSave": true,
      "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/.hg": true,
        "**/CVS": true,
        "**/.DS_Store": true,
        "**/*.pyc": true,
        "**/__pycache__": true
      },
      "python.pythonPath": ".venv/bin/python",
      "python.linting.pylintEnabled": true,
      "python.linting.enabled": true
    }

Add any of the above lines that aren't already in `./.vscode/settings.json`.

## VSCode terminal

- Any new terminal that gets opened in VSCode will automatically activate the virtual environment.
- Always close down your VSCode terminals before quitting VSCode. If you don't, when you start VSCode as above, these terminals will not automatically have the local virtual environment activated.


# Get JupyterLab working

## Kernels

From VSCode terminal, see what kernels you have and delete old ones as necessary. Note that since we are in a new VSCode terminal the virtual environment has automatically been activated:

    (3D print job prep) 
    $ jupyter kernelspec list
    Available kernels:
      python3               /Users/nordin/Documents/Projects/3D_printer_control_repos/3D_print_job_preparation/.venv/lib/python3.7/site-packages/ipykernel/resources
      cd-jl                 /Users/nordin/Library/Jupyter/kernels/cd-jl
      javascript            /Users/nordin/Library/Jupyter/kernels/javascript
      mr1_focus_analysis    /Users/nordin/Library/Jupyter/kernels/mr1_focus_analysis
      py36_anaconda_root    /Users/nordin/Library/Jupyter/kernels/py36_anaconda_root
      py37                  /Users/nordin/Library/Jupyter/kernels/py37


## Install Jupyterlab

From VSCode terminal:

    (3D print job prep) 
    $ jupyter --version
    jupyter core     : 4.6.1
    jupyter-notebook : not installed
    qtconsole        : not installed
    ipython          : 7.10.1
    ipykernel        : 5.1.3
    jupyter client   : 5.3.4
    jupyter lab      : not installed
    nbconvert        : not installed
    ipywidgets       : not installed
    nbformat         : not installed
    traitlets        : 4.3.3
    
    (3D print job prep) 
    $ pip install jupyterlab
    
    (3D print job prep) 
    $ jupyter --version
    jupyter core     : 4.6.1
    jupyter-notebook : 6.0.2
    qtconsole        : not installed
    ipython          : 7.10.1
    ipykernel        : 5.1.3
    jupyter client   : 5.3.4
    jupyter lab      : 1.2.4
    nbconvert        : 5.6.1
    ipywidgets       : 7.5.1
    nbformat         : 4.4.0
    traitlets        : 4.3.3

## Install TOC (table of contents) extension

[jupyterlab-toc](https://www.npmjs.com/package/@jupyterlab/toc)

From VSCode terminal:

    $ jupyter labextension install @jupyterlab/toc

## Install virtual environment as a new kernel

From VSCode terminal:

    (3D print job prep) 
    $ python -m ipykernel install --user --name=3D_print_job_preparation
    Installed kernelspec 3D_print_job_preparation in /Users/nordin/Library/Jupyter/kernels/3d_print_job_preparation
    (3D print job prep) 
    $ jupyter kernelspec list
    Available kernels:
      python3                     /Users/nordin/Documents/Projects/3D_printer_control_repos/3D_print_job_preparation/.venv/lib/python3.7/site-packages/ipykernel/resources
      3d_print_job_preparation    /Users/nordin/Library/Jupyter/kernels/3d_print_job_preparation
      cd-jl                       /Users/nordin/Library/Jupyter/kernels/cd-jl
      javascript                  /Users/nordin/Library/Jupyter/kernels/javascript
      mr1_focus_analysis          /Users/nordin/Library/Jupyter/kernels/mr1_focus_analysis
      py36_anaconda_root          /Users/nordin/Library/Jupyter/kernels/py36_anaconda_root
      py37                        /Users/nordin/Library/Jupyter/kernels/py37

## Test jupyterlab

From VSCode terminal:

    $ jupyter lab

Create notebook using `3d_print_job_preparation` kernel and execute:

    import cv2
    import numpy as np

and check versions:

    cv2.__version__
        '4.1.0'
    np.__version__
        '1.16.4'

Also, TOC works.

**&rarr; Success!**

