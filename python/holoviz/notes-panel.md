# Key information

## To set up a working `panel` installation with Jupyterlab

- Install `panel` in both the jupyterlab environment and the python kernel environment!

## To set up a working `panel` installation with python files

- Just install `panel` in the virtual environment that you are going to use.

---


# Tuesday, 1/11/22

## Run a python file with `panel`

To run a python file that uses `panel` (see [this link](https://panel.holoviz.org/getting_started/index.html#editor-server)):

    # Activate virtual environment in which panel is installed
    (base) 
    $ source ~/python_envs/panel_env/venv/bin/activate
    (panel) (base) 
    $ which panel
    /Users/nordin/python_envs/panel_env/venv/bin/panel

    # Run python file with panel serve
    (panel) (base) 
    $ panel serve python/holoviz/200626_stand_alone_1.py --show

Or, to make the panel app reload everytime the source file changes:

    $ panel serve python/holoviz/200626_stand_alone_1.py --show --autoreload
    

## Run `panel` in a Jupyterlab notebook

**NOTE: panel must be installed in both the jupyter lab environment and in the virtual environment being used as a jupyter kernel!!**

I was having a problem where `panel` elements in a jupyterlab notebook would not update the corresponding outputs. The problem was that `panel` was only installed in the virtual environment being used as a kernel, and wasn't installed in `jupyter_py39`. To fix it is simple:

    (jupyter_py39)
    $ pip install panel
        Successfully installed markdown-3.3.6 panel-0.12.6 param-1.12.0 pyct-0.4.8 pyviz-comms-2.1.0 tqdm-4.62.3