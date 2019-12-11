# Mon, 7/29/19

## Try voila

[voila](https://github.com/QuantStack/voila)

### Install

Install into the conda env, `py37`, that I use for all of my jupyter lab and notebook work.

    (py37)
    $ conda install -c conda-forge voila
        The following NEW packages will be INSTALLED:
    
          jupyter_server     conda-forge/osx-64::jupyter_server-0.1.0-py37_0
          jupyterlab_pygmen~ conda-forge/noarch::jupyterlab_pygments-0.1.0-py_0
          voila              conda-forge/noarch::voila-0.1.8-py_0
            
        The following packages will be UPDATED:
        
          ca-certificates    pkgs/main::ca-certificates-2019.5.15-0 --> conda-forge::ca-certificates-2019.6.16-hecc5488_0
          certifi               pkgs/main::certifi-2019.6.16-py37_0 --> conda-forge::certifi-2019.6.16-py37_1
          jupyter_client     pkgs/main/osx-64::jupyter_client-5.2.~ --> conda-forge/noarch::jupyter_client-5.3.1-py_0
          nbconvert          pkgs/main/osx-64::nbconvert-5.4.1-py3~ --> conda-forge/noarch::nbconvert-5.5.0-py_0
          pygments           pkgs/main/osx-64::pygments-2.3.1-py37~ --> conda-forge/noarch::pygments-2.4.2-py_0
        
        The following packages will be SUPERSEDED by a higher-priority channel:
        
          openssl              pkgs/main::openssl-1.1.1c-h1de35cc_1 --> conda-forge::openssl-1.1.1c-h01d97ff_0

### Try it out

    (py37)
    $ voila 190729_try_ipywidgets.ipynb
        jupyter_client.kernelspec.NoSuchKernel: No such kernel named conda-env-py37-py
        ERROR:tornado.access:500 GET / (::1) 27.54ms
        WARNING:tornado.access:404 GET /static/base/images/favicon.ico (::1) 0.65ms
        ^C[Voila] Stopping...

The problem is that the `py37` conda env is automatically added to Jupyter's list of kernels and voila can't see it. Solution: Add conda env as a Jupyter kernel in the normal way as in the answer to this stackoverflow question: [Conda environments not showing up in Jupyter Notebook](https://stackoverflow.com/questions/39604271/conda-environments-not-showing-up-in-jupyter-notebook).

    (py37)
    $ python -m ipykernel install --user --name py37 --display-name "py37-use_this_one"
        Installed kernelspec py37 in /Users/nordin/Library/Jupyter/kernels/py37

Now change the notebook's kernel to `py37-use_this_one`.

    (py37)
    $ voila 190729_try_ipywidgets.ipynb
        [Voila] Voila is running at:
        http://localhost:8866/
        [Voila] Kernel started: 7b7663b9-f750-4a37-9ce4-5c42c753b170
        [Voila] Executing notebook with kernel:

Now it works!

### Problem

It only worked the first time I used it. After shutting down voila from the command line  with `cntrl-C`, I can't get voila to work again. 

UPDATE: Oops, I was trying to run another notebook that didn't have the proper kernel set:

    $ voila 190729_gaussian_beam_interactive.ipynb
        jupyter_client.kernelspec.NoSuchKernel: No such kernel named conda-env-py37-py
        ERROR:tornado.general:Could not open static file '/base/images/favicon.ico'
        ERROR:tornado.general:Could not open static file '/style/style.min.css'
        ERROR:tornado.access:500 GET / (::1) 70.67ms

### How to shutdown

I use `cntrl-C` on the command line, after which the browser window to which voila is connected becomes unresponsive and just needs to be closed.

