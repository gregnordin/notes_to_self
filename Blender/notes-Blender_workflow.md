# Purpose

Document my Blender workflow as I develop it. In particular, keep this file updated to show my latest workflow so it is easy to reproduce.

# Set up

## Overview

Put python code in one or more text files external to Blender and execute them from within Blender by executing one main external text file that may import from other python modules (individual external files). The Blender file and external python files should all be in the same directory.

## Blender

See Blender documentation for your operating system to install Blender.

Blender: how ot use an external editor - [Blender docs - Use an External Editor](https://docs.blender.org/api/current/info_tips_and_tricks.html#use-an-external-editor)

## Install and set up VS Code

See VS Code documentation for how to install.

Set up VS Code to for Blender code autocomplete:

- Follow [Using Microsoft Visual Studio Code as external IDE for writing Blender scripts/add-ons](https://b3d.interplanety.org/en/using-microsoft-visual-studio-code-as-external-ide-for-writing-blender-scripts-add-ons/) "How to enable the autocomplete for Blender API in Visual Studio Code" using [Korchy/blender_autocomplete](https://github.com/Korchy/blender_autocomplete).


# Workflow

- Blender file with all objects and materials deleted but with stub python code to read and execute external python file.
    - To create blender file, create a new file and save it with some name, `my_file.blend`.
    - In Blender: 
        - Position mouse over 3D View window. 
        - Type `a`, which selects all objects (the Light, Cube, and Camera). 
        - Type `x` and hit return to delete all objects.
        - Click the `Scripting` tab to be in the scripting workspace.
        - At the top of the central window, click `+ New` to create a new text window.
        - Paste the following python code into the text window:

                import bpy
                import os
                
                filename = os.path.join(os.path.dirname(bpy.data.filepath), "my_file.py")
                exec(compile(open(filename).read(), filename, 'exec'))
            
    - In VS Code:
        - Create new python file `my_file.py` in the same directory as `my_file.blend`.
        - Paste following code into python file:

                import bpy
                from math import pi
                
                # Add blender file directory to the python path
                import sys
                blender_file_path = str(bpy.path.abspath("//"))
                if blender_file_path not in sys.path:
                    sys.path.append(blender_file_path)
                # print()
                # print(sys.path)

        - You can now import code from any python modules in the same directory and write code in this file that Blender will execute. If you have set up VS Code properly, you will have Blender code completions, which is extremely useful.
    - To execute external python code in `my_file.py` in Blender:
        - Click the `Scripting` tab to be in the scripting workspace.
        - With mouse anywhere in the python text window, type `option p`, which executes the code in the python text window, which in turn executes the external python file.
- Execute external python file to try some Blender effect and determine what needs to change in the code to try next.
- Do not re-execute changed code in the same Blender file. Also, do not save the Blender file you just used.
- Instead, re-open original blender file and try new external python code again. You could possibly select all objects manually and the materials and delete them before running the modified external python code, but this seems to still build up different object and material names.

# How-to's

- To create Camera, Light, and material(s), use info in [Blender 3D — How to create and render a scene in Blender using Python API, by Armindo Cachada | Jun 7, 2021](https://spltech.co.uk/blender-3d%E2%80%8A-%E2%80%8Ahow-to-create-and-render-a-scene-in-blender-using-python-api/).