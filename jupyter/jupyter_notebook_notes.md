[toc]

# Working with notebooks

## Keyboard shortcuts

### Command mode

- A to insert a new cell above the current cell, B to insert a new cell below.
- M to change the current cell to Markdown, Y to change it back to code
- D + D (press the key twice) to delete the current cell
- Select Multiple Cells:
    - Shift + J or Shift + Down selects the next sell in a downwards direction. You can also select sells in an upwards direction by using Shift + K or Shift + Up.
    - Once cells are selected, you can then delete / copy / cut / paste / run them as a batch. This is helpful when you need to move parts of a notebook.
    - You can also use Shift + M to merge multiple cells.


### Editing mode

- Shift + Tab will show you the Docstring (documentation) for the the object you have just typed in a code cell - you can keep pressing this short cut to cycle through a few modes of documentation
- Ctrl + Shift + - will split the current cell into two from where your cursor is.
- Esc + F Find and replace on your code but not the outputs.
- Esc + O Toggle cell output.
- Jupyter supports mutiple cursors, similar to Sublime Text. Simply click and drag your mouse while holding down Alt
- package.some_function_or_class_name?
    - Shows docstring
- package.some_function_or_class_name??
    - Shows code
- \*int*?
    - Shows all objects in current namespace that has "int" in their name. Useful if you can't quite remember the whole object name
    - Example:
            <pre>import numpy as np
        np.\*array*?</pre>
- %%quickref - shows a summary of these things

From [28 Jupyter Notebook tips, tricks and shortcuts - Oct. 12, 2016](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)

# Install new python kernel

- Crate new virual environment using conda or `python -m venv ...`
- Activate new virtual environment
- Install desired packages for the virtual environment
- Install ipykernel & add kernel to jupyter venv I use to serve jupyter notebooks, `jupyter_py37`
    - `pip install ipykernel`
    - `$ python -m ipykernel install --prefix=/Users/nordin/opt/miniconda3/envs/jupyter_py37 --name 'name_of_virtual_environment'`
- a


# How to navigate up the directory structure &rarr; symlink

[Is it possible to navigate to a parent directory in the jupyter tree?](https://stackoverflow.com/questions/38282336/is-it-possible-to-navigate-to-a-parent-directory-in-the-jupyter-tree)  
[How to Create and Use Symbolic Links (aka Symlinks) on a Mac](https://www.howtogeek.com/297721/how-to-create-and-use-symbolic-links-aka-symlinks-on-a-mac/)  

You can specify either a path to a directory or file:

    ln -s /path/to/original /path/to/link
    
The -s here tells the ln command to create a symbolic link. If you want to create a hard link, you’d omit the -s. Most of the time symbolic links are the better choice, so don’t create a hard link unless you have a specific reason for doing so.


# Noteworthy notebook items

## Getting help for objects

Show docstring:

    <object>?
    
Show source code:

    <object>??
    

## Magics

List available magics

    %lsmagic
    
    
Time how long things take

    # Time one-line command
    %time <command>
    
    # Time commands in an input cell
    %%time
    <commands for cell>
    
    # Time multiple executions of the same command(s)
    %timeit <command>
    # or
    %%timeit
    <commands>
    
Share data between notebooks

    # Write data from one notebook to a file
    import numpy as np
    table = np.random.random((10,100))
    %store table
    
    # In another notebook read data from file
    %store -r table
    
Show docstring for a command

    %pdoc <code>
    # or
    ?<code>
    
Latex - show rendered latex in an input cell

    %%latex
    <latex commands over multiple lines>
    
Watermark

    !pip install watermark
    
    %reload_ext watermark
    %watermark


# Working with `conda` environments

>See my notes in `/Users/nordin/Documents/Projects/2016_Projects/160320_map_gpx_files_folium/notes.md` under 4/10/16.

Each conda environment needs to be a valid jupyter kernel. To see what conda environments are installed, execute `conda env list` or `conda info --envs`.

<span style="background-color:lightgreen;">Always work from the root conda environment.</span> Install new jupyter kernels in the root environment. Also always start `jupyter notebook` from the root environment. Each conda environment installed as a jupyter kernel becomes a selectable kernel from within jupyter notebook. 

## How to make a conda environment a valid jupyter kernel

### Easy way

Install Damian Avilla's [`nb_conda_kernels`](https://github.com/Anaconda-Server/nb_conda_kernels), which automatically creates KernelSpecs for each conda environment. Make sure `ipykernel` is installed in every conda environment you want to be available as a jupyter kernel.

### Extremely manual method

From my old (4/10/16) notes:

- In `~/.ipython/kernels` create new directory, `python3folium`.
- Copy the kernel.json file from `~/ipython/kernels/python3`. Change "display_name" to "Python 3 folium" and in "argv" change path to "/Users/nordin/anaconda/envs/py35folium/bin/python"
- Restart jupyter notebook
- Either:
    - Make a new notebook by selecting New -> Python 3 folium
    - Open an existing notebook
        - In Edit menu select Edit Notebook Metadata
        - In "kernelspec" change "name" to "python3folium" and "display_name" to "Python 3 folium"
        - Shutdown kernel and re-start. Do `import sys` and `sys.path` to confirm that new env is in the path

## How to check which kernel is being used in a jupyter notebook

In notebook do `import sys` and `sys.path`. This will print which python version is being used by the notebook.


---
# Resources

[Jupyter Notebook: Little-Known Tricks!](https://blog.3blades.io/jupyter-notebook-little-known-tricks-b0866a558017)

- Internal and external hyperlinks - <span style="background-color:lightpink;">very useful</span>
- Automatic module reload
- Run demos

[The Jupyter Notebook: 3 More Little-Known Tricks](https://blog.3blades.io/the-jupyter-notebook-3-more-little-known-tricks-34b75b6455a4)

- Change your notebook appearance and functionality: custom.js - <span style="background-color:lightpink;">very useful</span>
    - displaying line numbers by default
- Comment out large snippets AND maintain syntax highlighting!
- Write and execute functions in languages other than Python (example: Fortran)

[10 things you really should know about jupyter notebooks - Jakub Czakon](https://www.youtube.com/watch?v=FwUcJFSAfQw)

# Example notebooks

[A gallery of interesting Jupyter Notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks)
