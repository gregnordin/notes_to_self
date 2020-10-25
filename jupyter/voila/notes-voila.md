
# Saturday, October 24, 2020

Last night I got voila to work on my macbook pro by doing the following:

    # Activate virtual environment from which I run all of my jupyter notebooks
    (base)
    $ conda activate jupyter_py37
    (jupyter_py37)
    
    # List available jupyter kernels
    $ jupyter kernelspec list
    Available kernels:
      javascript           /Users/nordin/Library/Jupyter/kernels/javascript
      python37             /Users/nordin/Library/Jupyter/kernels/python37
      python37664bitvenvvenveee4b1c6f4634df98f49896c9e14a830 /Users/nordin/Library/Jupyter/kernels/python37664bitvenvvenveee4b1c6f4634df98f49896c9e14a830
      3d_print_job_prep   /Users/nordin/opt/miniconda3/envs/jupyter_py37/share/jupyter/kernels/3d_print_job_prep
      anaconda_py37       /Users/nordin/opt/miniconda3/envs/jupyter_py37/share/jupyter/kernels/anaconda_py37
      gps_mapping         /Users/nordin/opt/miniconda3/envs/jupyter_py37/share/jupyter/kernels/gps_mapping
      python3             /Users/nordin/opt/miniconda3/envs/jupyter_py37/share/jupyter/kernels/python3
      spectra_and_tools   /Users/nordin/opt/miniconda3/envs/jupyter_py37/share/jupyter/kernels/spectra_and_tools
    (jupyter_py37)
    # Confirm that kernel '3D_print_job_prep' is available - this is the one that my jupyter notebooks use in which I have ipywidgets code
    
    # Install voila
    $ pip install voila
    
    # Start a notebook with ipywidgets using voila, the notebook is served at
    # http://localhost:8866/voila/render/<notebook>
    $ voila <path to notebook>
    
    $ Or start voila in a directory and it will show all notebooks in that directory
    $ voila
    
The notebook served by voila only shows the widget app and the markdown cells unless you use the flag `--strip_sources=False`. Also, if you need to see debug information, you can start voila with the `--debug` flag.

