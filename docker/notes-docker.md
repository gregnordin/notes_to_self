# Info

## Docker

[The Docker Handbook - 2021 Edition](https://www.freecodecamp.org/news/the-docker-handbook/)

## Running Jupyter Lab in container

[How to Run Python 3 and Jupyter Lab using an Anaconda Docker Container and VS Code](https://www.youtube.com/watch?v=cK7vgjOntqM) - outstanding. [U0-Introduction/B Environment Setup.ipynb](https://github.com/GonzagaCPSC322/U0-Introduction/blob/master/B%20Environment%20Setup.ipynb)  
[How to Run Jupyter Notebook on Docker- No more Python env and package update](https://towardsdatascience.com/how-to-run-jupyter-notebook-on-docker-7c9748ed209f) - very good.

[Docker Tutorial part 1 | Python in Docker | Jupyter in Docker](https://www.youtube.com/watch?v=At5alroIsic)  

# Next

- Document basic docker ideas
- Use a docker file to create container (or is it an image?)
- Create container with specific set of installed packages as well as jupyter (including ipywidgets, voila, bokeh, panel?)
- How put image where students can get it? Docker Hub?

# Log

## Wed 2020-06-23

### First objective &rarr; success!

Objective: run jupyter lab from docker container and access it from browser on my laptop.

Create container from image and start it running.

    $ docker run -i -t -p 8890:8890 -v "$PWD":/home --name anaconda3 continuumio/anaconda3
    # Notes:
    #   -i -t - interactive, terminal
    #   -p 8890:8890 - <host port>:<container port>, connect port 8890 in container to port
                       8890 on container's host
    #                  NOTE: jupyter usually runs on port 8888. If you use port 8888 here
                       for the host and are already running jupyter lab on the host, trying to 
                       connect to the container will be superceded by jupyter on the host.
                       Therefore I have chosen a different port for the container.
    #  -v "$PWD":/home - connect the container's /home directory to the present working
                         directory from which the docker command is being run.
    # --name anaconda3 - Give container the name 'anaconda3'.
    # continuumio/anaconda3 - image from which to build the container.
    
Start jupyter lab from within the container.

    root@293476a27c4d:/# jupyter lab --ip='0.0.0.0' --port=8890 --no-browser --allow-root --notebook-dir=/home
    # Note the last directive means to set the notebook directory to the container's home directory, which when we made the container we set to the directory from which `docker run` was issued.
    
Connect browser window from laptop to container running jupyter lab:

    # Copy and paste something that looks like the following into the browser url bar:
    http://127.0.0.1:8890/lab?token=73868eb4de7a3c47e9c6a6d61d7aa35b99a29291a7285728
    # Browser window will connect and now you are in business!
    
Exit jupyter lab:

    # Press ^C twice from the command line
        
Stop the container:

    # From the command line:
    root@293476a27c4d:/# exit
    
The container is stopped in its current state. To start it again from this state:
    
    # Start container named anaconda3
    $ docker start anaconda3

    # Connect command line to container 
    $ docker attach anaconda3
    
Some other useful docker commands:
    
    # List all running
    $ docker ps
    # List all running and exited containers
    $ docker ps -a