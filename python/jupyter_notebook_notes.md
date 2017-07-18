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


From [28 Jupyter Notebook tips, tricks and shortcuts - Oct. 12, 2016](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)


# Working with `conda` environments

>See my notes in `/Users/nordin/Documents/Projects/2016_Projects/160320_map_gpx_files_folium/notes.md` under 4/10/16.

Each conda environment needs to be a valid jupyter kernel. To see what conda environments are installed, execute `conda info --envs`.

<span style="background-color:lightgreen;">Always work from the root conda environment.</span> Install new jupyter kernels in the root environment. Also always start `jupyter notebook` from the root environment. Each conda environment installed as a jupyter kernel becomes a selectable kernel from within jupyter notebook. 

## How to make a conda environment a valid jupyter kernel

### Easy way

Install Damian Avilla's [nb_conda_kernels](https://github.com/Anaconda-Server/nb_conda_kernels), which automatically creates KernelSpecs for each conda environment.

### More involved method

From my old (4/10/16) notes:

- In `~/.ipython/kernels` create new directory, `python3folium`.
- Copy the kernel.json file from `~/ipython/kernels/python3`. Change "display_name" to "Python 3 folium" and in "argv" change path to "/Users/nordin/anaconda/envs/py35folium/bin/python"
- Restart jupyter notebook
- Either:
    - Make a new notebook by selecting New -> Python 3 folium
    - Open an existing notebook
        - In Edit menu select Edit Notebook Metadata
        - In "kernelspec" change "name" to "python3folium" and "display_name" to "Python 3 folium"
        - Shutdown kernel and re-start. Do `import os` and `sys.path` to confirm that new env is in the path

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

# Example notebooks

[A gallery of interesting Jupyter Notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks)
