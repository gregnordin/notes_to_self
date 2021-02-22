
# Sunday, October 25, 2020

## Goal

- Develop a workflow where I develop ipywidget apps in jupyter notebooks and then deploy using Voila to my laptop or to a server.

## Thoughts

- Possible Voila servers:
    - Home Raspberry Pi
    - Office Raspberry Pi
    - nordinvm.byu.edu
    - New BYU VM
    - Get a Digital Ocean VM
    
## Python virtual environment organization

### My laptop


### Set up on nordinvm.byu.edu

From my laptop:

    # If not on campus, connect to CAEDM VPN
    
    # Copy files from my laptop to nordinvm.byu.edu 
    # The -r flag means recursive so that all underlying files and directories are copied
    $ scp -r 200820_analyze_strobed_images/ nordin@nordinvm.byu.edu:"~/projects"
    
    # ssh to nordinvm.byu.edu
    $ ssh -i ~/.ssh/nordinvmbyu nordin@10.18.46.149
    
    # Create new virtual environment
    $ pyenv virtualenv 3.8.3 voila_opencv
    
    # Switch to new virtual environment
    $ pyenv shell voila_opencv
    
    # Upgrade pip
    $ pip install --upgrade pip
    
    # Install packages
    $ pip install matplotlib numpy jupyterlab opencv-contrib-python imutils pandas voila pytest scipy panel ipywidgets ipympl
    
    $ cd /home/nordin/projects/200820_analyze_strobed_images
    
    $ voila 201021_dev__linescans_for_all_defocus_values.ipynb
    
    



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

