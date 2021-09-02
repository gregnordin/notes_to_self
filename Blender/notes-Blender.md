{{TOC}}

# Information

[What is a .blend1 file and why do you (not) need them?](https://cgcookie.com/articles/what-is-a-blend1-file-and-do-you-really-need-them)

# Basics

[How to Use Blender without a Middle Mouse Button or a Scroll Wheel](https://www.blenderhut.com/use-blender-without-middle-mouse-button-or-scroll-wheel/)  
&nbsp;&nbsp;&nbsp;&nbsp;Edit &rarr; Preferences &rarr; Input &rarr; click `Emulate 3 Button Mouse`

## Viewport navigation

[Viewport Navigation - Blender 2.80 Fundamentals](https://www.youtube.com/watch?v=ILqOWe3zAbk&list=PLa1F2ddGya_-UvuAqHAksYnB0qL9yWDO6&index=2)

### Selecting 

- Select - click object
- Unselect - click empty space
- a - select all
- option-a - deselect all
- x - delete whatever is selected

### Navigation

- Use tiny buttons along right upper edge of main window or XYZ stick axes
- Zoom in and out - click on tiny magnifier icon and move trackpad finger up or down OR cmd and 2 fingers on trackpad
- Rotate - option with 1 finger on trackpad OR 2 fingers unclicked on track pad
- Move - shift-option with 1 finger clicked on mousepad
- Recenter on selected object(s) - View menu &rarr; Frame Selected

## Interface

[Interface Overview - Blender 2.80 Fundamentals](https://www.youtube.com/watch?v=8XyIYRW_2xk&list=PLa1F2ddGya_-UvuAqHAksYnB0qL9yWDO6&index=3)

- Strip along bottom of window says what mouse keys will do
- Upper right smaller window region &rarr; Selectable editor region.
- Toolbar along left side &rarr; `t` (for tools) to toggle it being visible or not
- With cursor anywhere in viewport, hit `shift-space` and will bring up tool bar as a pop-up menu
- Click `n` and toolbar will pop out of upper right side with object transformation settings
- Pie menus? Around 3:50 in video

[Select & Transform - Blender 2.80 Fundamentals](https://www.youtube.com/watch?v=hTL6AKR8YDs&list=PLa1F2ddGya_-UvuAqHAksYnB0qL9yWDO6&index=5)

## Duplication

- 2 finger click on object, which brings up a popup menu
- Select `Duplicate`
- Single finger drag away from original object and you'll have a 2nd object that you can place
- To more finely position object when it is selected, go into Object Properties and type in coordinates for x, y, z

## Python Scripting

- Start Blender from the terminal command line so that print statements will put their output in this terminal window: `/Applications/Blender.app/Contents/MacOS/Blender &`
- Select `Scripting` from menu along top left of window. This puts the interface into a scripting-friendly state.
- Click on the `+ New` button of the Text Editor to bring up a new text editor window.
- Type `print('hello world')` in text editor.
- Run by clicking the run icon of the Text Editor or hitting `cmd-p` (`alt-p` on Windows) while mouse is anywhere within text editor window.


## Animation

- <span style="color:red; font-size:150%">&#x2605;</span> [How to Make an Object Fade in/out in Blender (Tutorial)](https://www.youtube.com/watch?v=3QjN693Gzwo)
- [Fade In – Fade Out Effects in Blender](https://prosperocoder.com/posts/blender/fade-in-fade-out-effects/)
- <span style="color:red; font-size:150%">&#x2605;</span> [Olav3D Tutorials](https://www.youtube.com/c/Olav3D/search?query=keyframe)
    - [[2.8] Blender Tutorial: Simple Animation For Beginners](https://www.youtube.com/watch?v=Dyj0sJVd3Lw) &rarr; importance of keyframes to animate objects (transition between 2 states or positions), using physics for motion
    - [How to Code 3D Objects From Scratch With Blender and Python](https://www.youtube.com/watch?v=tsmkqU25_As) &rarr; excellent
    - [How to Select And Transform Objects With Python in Blender](https://www.youtube.com/watch?v=VAmNUSUdVA0) &rarr; excellent
    - [[2.79] Tutorial: 3D Animation With Python and Blender](https://www.youtube.com/watch?v=ssHiWpVuxTk) &rarr; note older version of Blender so interface is not the same but can figure it out

- [Create 3D objects and animations in Blender with Python API](https://demando.se/blogg/post/dev-generating-a-procedural-solar-system-with-blenders-python-api/)

- `import bpy`
    - `bpy.context`: it contains getters and readers on read-only values that describe your current working context or even the area (i.e. the panel in your window) that is currently being accessed
    - `bpy.data`: it gives you access to the resources in your scene (the objects, the materials, the meshes…) so you can load, add or delete them
    - `bpy.ops`: that’s the real meat of the API – it’s what allows you to perform actions and call operators on your objects or your views; it’s basically how you can simulate user actions via scripting (like selecting an object, entering edit mode, applying subdivisions, changing to “flat” shading, maximising a window…)
- Start Blender from the command line: `/Applications/Blender.app/Contents/MacOS/Blender &`

---

# Log

## Thursday, 2021-09-02

- Go through [Create 3D objects and animations in Blender with Python API](https://demando.se/blogg/post/dev-generating-a-procedural-solar-system-with-blenders-python-api/), which is excellent!
    - Complete through Step 4 adding sun and radius rings
    - Complete through Step 5, shader and materials for planets etc.

