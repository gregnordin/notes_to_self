# Info

## Manim




# Next

- Is manim able to animate sliced object reconstruction to explain stereolithographic 3D printing?

# Log

## Saturday 2021-08-07

Objective: determine whether I can use manim to create an animation showing sliced object reconstruction to explain stereolithographic 3D printing.

### Use manim docker container

[Instructions for running the docker image](https://pypi.org/project/manim/#docker).

    $ docker run -it --name my-manim-container -v "$(pwd):/manim" manimcommunity/manim /bin/bash
    # -it - interactive, terminal
    #  -v "$PWD":/home - connect the container's /home directory to the present working
                         directory from which the docker command is being run.

