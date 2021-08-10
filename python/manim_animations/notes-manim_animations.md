# Objective


Determine whether I can use manim to create an animation showing sliced object reconstruction to explain stereolithographic 3D printing.


# Info

## Manim

[Manim](https://docs.manim.community/en/stable/index.html)  
[Tutorials](https://docs.manim.community/en/stable/tutorials.html)  
[Manim - github](https://github.com/manimcommunity/manim)  
[Creating math animations in Python with Manim](https://gilberttanner.com/blog/creating-math-animations-in-python-with-manim)  
[Jupyter - manim magic - %%manim](https://docs.manim.community/en/stable/reference/manim.utils.ipython_magic.ManimMagic.html#manim.utils.ipython_magic.ManimMagic.manim)  


# Next

- Is manim able to animate sliced object reconstruction to explain stereolithographic 3D printing?

# Log

## Saturday 2021-08-07

&#9989; Objective: Try to get manim in a docker container to work with a simple example.

### Set up manim docker container

[Instructions for running the docker image](https://pypi.org/project/manim/#docker).  
Also see my notes at `notes_to_self/docker/notes-docker.md`.

    $ docker run -it -p 8891:8891 --name manim-container -v "$(pwd):/manim" manimcommunity/manim /bin/bash
    # -it - interactive, terminal
    #   -p 8891: 8891 - <host port>:<container port>, connect port 8891 in container to port
                       8891 on container's host
    #                  NOTE: jupyter usually runs on port 8888. If you use port 8888 here
                       for the host and are already running jupyter lab on the host, trying to 
                       connect to the container will be superceded by jupyter on the host.
                       Therefore I have chosen a different host port to map the container to.
    #  -v "$PWD":/manim - connect the container's /manim directory to the present working
                         directory from which the docker command is being run.


### Run Jupyter Lab from container

    manimuser@ba4698c8a060:~$ jupyter lab --ip='0.0.0.0' --port=8891 --no-browser --allow-root --notebook-dir=/manim

        To access the server, open this file in a browser:
            file:///manim/.local/share/jupyter/runtime/jpserver-7-open.html
        Or copy and paste one of these URLs:
            http://ba4698c8a060:8891/lab?token=6f331357f74d2a1888d81c2ba0482316a38e1d441c09db6a
         or http://127.0.0.1:8891/lab?token=6f331357f74d2a1888d81c2ba0482316a38e1d441c09db6a


### Run python file from docker command line from terminal

    manimuser@ba4698c8a060:~/210807_try_manim/manim_try1$ manim -ql manim_try1.py SquareToCircle
    
Note: this creates a `480p15` video (854 × 480 pixels, 15 frames per second). Use `-qm` to create a `720p30` video (1280 × 720 pixels, 30 frames per second).
    

## Monday 2021-08-09

### Objectives

- &#9989; Learn how to work with a 3D scene.
- Create "layer" rectangular slice.
- Stack "layers".

### `manim_try_3D.py`

- Get 3D scene to work.
- Animate transformation of cube into rectangular slice.

