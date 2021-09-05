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

- [Blender Tutorial - Animating With Python, UNLOCK the power](https://www.youtube.com/watch?v=QnvN1dieIAU)
    - <span style="color:red; font-size:150%">&#x2605;</span> Edit &rarr; Preferences &rarr; Interface &rarr; click on Python Tooltips checkbox - when hover over something in one of the windows, popup tooltip shows python statement for that thing.  See 16:20 in video.
    - <span style="color:red; font-size:150%">&#x2605;</span> In REPL, start typing command and after typing a `.` or any other character, hit `tab` and it will show all of the possible commands or completions of what you have started typing.
    - 19:00 - right click on something in the interface and select `Copy data_path` to get the data_path text you need to set this parameter in an argument list.
- Start Blender from the terminal command line so that print statements will put their output in this terminal window: `/Applications/Blender.app/Contents/MacOS/Blender &`
- Select `Scripting` from menu along top left of window. This puts the interface into a scripting-friendly state.
- Click on the `+ New` button of the Text Editor to bring up a new text editor window.
- Type `print('hello world')` in text editor.
- Run by clicking the run icon of the Text Editor or hitting `cmd-p` (`alt-p` on Windows) while mouse is anywhere within text editor window.
- <span style="color:red; font-size:150%">&#x2605;</span> [Create 3D objects and animations in Blender with Python API](https://demando.se/blogg/post/dev-generating-a-procedural-solar-system-with-blenders-python-api/)
- `import bpy`
    - `bpy.context`: it contains getters and readers on read-only values that describe your current working context or even the area (i.e. the panel in your window) that is currently being accessed
    - `bpy.data`: it gives you access to the resources in your scene (the objects, the materials, the meshes…) so you can load, add or delete them
    - `bpy.ops`: that’s the real meat of the API – it’s what allows you to perform actions and call operators on your objects or your views; it’s basically how you can simulate user actions via scripting (like selecting an object, entering edit mode, applying subdivisions, changing to “flat” shading, maximising a window…)
- Start Blender from the command line: `/Applications/Blender.app/Contents/MacOS/Blender &`


## Animation

- <span style="color:red; font-size:150%">&#x2605;</span> [How to Make an Object Fade in/out in Blender (Tutorial)](https://www.youtube.com/watch?v=3QjN693Gzwo)
- [Fade In – Fade Out Effects in Blender](https://prosperocoder.com/posts/blender/fade-in-fade-out-effects/)
- <span style="color:red; font-size:150%">&#x2605;</span> [Olav3D Tutorials](https://www.youtube.com/c/Olav3D/search?query=keyframe)
    - [[2.8] Blender Tutorial: Simple Animation For Beginners](https://www.youtube.com/watch?v=Dyj0sJVd3Lw) &rarr; importance of keyframes to animate objects (transition between 2 states or positions), using physics for motion
    - [How to Code 3D Objects From Scratch With Blender and Python](https://www.youtube.com/watch?v=tsmkqU25_As) &rarr; excellent
    - [How to Select And Transform Objects With Python in Blender](https://www.youtube.com/watch?v=VAmNUSUdVA0) &rarr; excellent
    - [[2.79] Tutorial: 3D Animation With Python and Blender](https://www.youtube.com/watch?v=ssHiWpVuxTk) &rarr; note older version of Blender so interface is not the same but can figure it out
- [Create 3D objects and animations in Blender with Python API](https://demando.se/blogg/post/dev-generating-a-procedural-solar-system-with-blenders-python-api/)
- With cursor over 3D view, hit `space` to toggle animation running

---

# Log

## Thursday, 2021-09-02

- Go through [Create 3D objects and animations in Blender with Python API](https://demando.se/blogg/post/dev-generating-a-procedural-solar-system-with-blenders-python-api/), which is excellent!
    - Complete through Step 4 adding sun and radius rings
    - Complete Step 5, shader and materials for planets etc.
    - Complete Step 6, animating the planets
    - Complete Step 7, autocleaning the scene
    - Complete Step 8, Auto-setting scene properties, render engine, the 3D view settings

## Friday, 2021-09-03

**Objective**: Create 3D stacked rectangular-like objects and animate fade in.  
**Result**: Basic success with some caveats as noted in "Observations".

Rectangular layer-like object centered at `(x,y) = (0,0)` with bottom at `z=0`:
    
    xy_layer_size = 10
    z_layer_size = 0.5
    layer_scale = (1, 1, z_layer_size / xy_layer_size)
    
    layer = bpy.ops.mesh.primitive_cube_add(
        size=xy_layer_size, 
        scale=layer_scale, 
        location=(0, 0, z_layer_size/2)
    )

When re-run script, need to get rid of objects and materials created in previous runs. Run the following code at the beginning of the script to do that:

    def clean_up():
        # Delete materials from last time script ran
        original_materials = ['Dots Stroke', 'Material']
        for mat in bpy.data.materials:
            print(mat.name)
            if mat.name not in original_materials:
                bpy.data.materials.remove(mat)
        # Delete objects from last time script ran
        for obj in bpy.data.objects:
            obj.select_set(True)
            bpy.ops.object.delete(use_global=False)
            
    clean_up()

Couldn't figure out [f-curves (see Blender documentation)](https://docs.blender.org/manual/en/latest/editors/graph_editor/fcurves/introduction.html) in the time available.  

Instead, go through <span style="color:red; font-size:150%">&#x2605;</span> <span style="color:red; font-size:150%">&#x2605;</span> [Color Animation in Blender with Python](https://prosperocoder.com/posts/blender/color-animation/), which is excellent and just what I need for now. Try it out and the colors of a slice continuously change between specified colors. Then change some of the colors to have `alpha=0` and observe that both the colors and transparency fade in and out.

Next, start new Blender file, `210903_python_3D_layer_alpha_animate.blend`, to create layers and fade them in. Do the following:

- Create code to make a single layer and fade it in. 
- Pull layer and material code into for loop.
- Create 4 layers

**Observations**:

- Can see outlines of layers during whole animation, need to eliminate
- Last part of each layer animation is jerky
- Need to change camera position
- Change light position?

Found [Blender Tutorial - Animating With Python, UNLOCK the power](https://www.youtube.com/watch?v=QnvN1dieIAU), which is really good.

## Saturday, 2021-09-04

**To do**

- &#9989; Create a rendered video and see if it has outlines of layers in it and if last part of each animation is jerky
    - &#10060; If everything is great, proceed to make a better animation for conventional 3D printing with layers.
    - <span style="color:#32cd32; font-size:150%">&#9654;</span> If problems still exist:
        - How eliminate object outlines for transparent objects?
        - How remove jerky transparency animation &rarr; use a different interpolation? How?
- Remove background and make it all black or all white?

**Things I tried**

Use solution at [How to set camera location in the scene while pointing towards an object with a fixed distance](https://blender.stackexchange.com/questions/100414/how-to-set-camera-location-in-the-scene-while-pointing-towards-an-object-with-a) to set camera distance from origin, looking at the origin in `210903_python_3D_layer_alpha_animate.blend`. Works well.

With the camera in the right position, now try rendering a video. To make the render process go much faster, do the following in the output panel:

- Change video resolution to 720x480 (width x height) from 1920x1080.
- Change file format to Movie &rarr; FFmpeg Video
- Change container to MPEG-4
- Make sure video codec is H.264

Next, go to Layout window arrangement and select View &rarr; Viewport Render Animation. This will render the animation. I did a bunch of other stuff and there was only a static image of the final scene for all of the frames in the output (don't use from the main menu Renderer &rarr; Render Animation). Some good points can be found here, but not the last step as I just noted: [[2.8] Blender : How to Render an Animation in EEVEE](https://www.youtube.com/watch?v=nQXQCT_hKSs).

- Change resolution back to 1920x180
- Choose AVI JPEG file format
- Set quality to 100%
- Other settings: 24 fps and render frames 1 to 250

**Results**:

- avi output file is 199 MB! But it renders pretty fast (much, much faster than mpeg-4).
- Transparent layers still have outlines
- Final part of each layer fade-in is still jerky
- Bottom of 2nd layer is banded, but not other layers
    - Try changing Postprocessing &rarr; Dither from 1.0 to 2.0, but it doesn't help



