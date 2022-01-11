# Tuesday, 1/11/22

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
    
    
