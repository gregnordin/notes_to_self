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
- **Set viewport to be the same as the active camera**
    - `View` &rarr; `Cameras` &rarr; `Active Camera` (same as Numpad 0, but I don't have a number pad)

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
- Run by clicking the run icon of the Text Editor or hitting `option-p` (`alt-p` on Windows) while mouse is anywhere within text editor window.
- <span style="color:red; font-size:150%">&#x2605;</span> [Create 3D objects and animations in Blender with Python API](https://demando.se/blogg/post/dev-generating-a-procedural-solar-system-with-blenders-python-api/)
- `import bpy`
    - `bpy.context`: it contains getters and readers on read-only values that describe your current working context or even the area (i.e. the panel in your window) that is currently being accessed
    - `bpy.data`: it gives you access to the resources in your scene (the objects, the materials, the meshes…) so you can load, add or delete them
    - `bpy.ops`: that’s the real meat of the API – it’s what allows you to perform actions and call operators on your objects or your views; it’s basically how you can simulate user actions via scripting (like selecting an object, entering edit mode, applying subdivisions, changing to “flat” shading, maximising a window…)
- Start Blender from the command line: `/Applications/Blender.app/Contents/MacOS/Blender &`

## Use external code editor

- [Blender docs - Use an External Editor](https://docs.blender.org/api/current/info_tips_and_tricks.html#use-an-external-editor)
    - In Blender in a python editor window, reference and execute external script `myscript.py` relative to the blend-file:

            import bpy
            import os
            
            filename = os.path.join(os.path.dirname(bpy.data.filepath), "myscript.py")
            exec(compile(open(filename).read(), filename, 'exec'))
    
- Use VS Code as the external editor
    - Set up to do autocomplete
        - Follow [Using Microsoft Visual Studio Code as external IDE for writing Blender scripts/add-ons](https://b3d.interplanety.org/en/using-microsoft-visual-studio-code-as-external-ide-for-writing-blender-scripts-add-ons/) "How to enable the autocomplete for Blender API in Visual Studio Code" using [Korchy/blender_autocomplete](https://github.com/Korchy/blender_autocomplete).



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

Use solution at [How to set camera location in the scene while pointing towards an object with a fixed distance](https://blender.stackexchange.com/questions/100414/how-to-set-camera-location-in-the-scene-while-pointing-towards-an-object-with-a) to set camera distance from origin, looking at the origin in `210903_python_3D_layer_alpha_animate.blend`. **Works well.**

With the camera in the right position, now try rendering a video. To make the render process go much faster, do the following in the output panel:

- Change video resolution to 720x480 (width x height) from 1920x1080.
- Change file format to Movie &rarr; FFmpeg Video
- Change container to MPEG-4
- Make sure video codec is H.264

Next, go to Layout workspace and select View &rarr; Viewport Render Animation. This will render the animation. I did a bunch of other stuff and there was only a static image of the final scene for all of the frames in the output (don't use from the main menu Renderer &rarr; Render Animation). Some good points can be found here, but not the last step as I just noted: [[2.8] Blender : How to Render an Animation in EEVEE](https://www.youtube.com/watch?v=nQXQCT_hKSs).

- Change resolution back to 1920x1080
- Choose AVI JPEG file format
- Set quality to 100%
- Other settings: 24 fps and render frames 1 to 250

**Results**:

- avi output file is 199 MB! But it renders pretty fast (much, much faster than mpeg-4).
- Transparent layers still have outlines
- Final part of each layer fade-in is still jerky
- Bottom of 2nd layer is banded, but not other layers
    - Try changing Postprocessing &rarr; Dither from 1.0 to 2.0, but it doesn't help
- All rendered videos are in `/tmp`

Go through [https://docs.blender.org/manual/en/latest/render/output/animation.html](https://docs.blender.org/manual/en/latest/render/output/animation.html) and learn about workflows - the Direct Approach and the Frame Sequence approach.

**Turn off grid and XY lines**

In the Layout workspace before rendering, click on `Floor` and `X`,`Y` in the dropdown menu as in the image below. Also turn off `Origins` to eliminate the little dot that denotes the center of each object.

![](assets/210903_turn_off_grid_and_XY_lines.png)

**Try more things**

- In `210903_python_3D_layer_alpha_animate.blend`, create `frame_pairs_for_layers` in a for loop with programmatic specification of number of layers and fade-in times

        start_frame = 10
        num_fadein_frames = 15
        num_frames_between_fadeins = 20
        num_layers = 5
        frame_pairs_for_layers = []
        for i in range(num_layers):
            base_frame = start_frame + i * (num_fadein_frames + num_frames_between_fadeins)
            frame_pairs_for_layers.append(
                (base_frame, base_frame + num_fadein_frames)
            )
        print(frame_pairs_for_layers)
        
        # Print output: [(10, 25), (45, 60), (80, 95), (115, 130), (150, 165)]

- In `Output Properties` reduce number of frames from 250 to 185

**Next**

- Create a 90&deg; channel bend 3 layers tall where channel can be seen on the two visible layer stack faces. 
    - Need function(s) that can create and place the necessary layer shapes for each exposure region.
        - How create an L-shaped 3D object?
    - How group them together to have joint keyframes? No &rarr; as shown in [Blender Tutorial - Animating With Python, UNLOCK the power](https://www.youtube.com/watch?v=QnvN1dieIAU), you can just programmatically give objects the same keyframe times.
- Animate the following cases:
    - Conventional 3D printing method
    - Reduced edge dose like we presented in 2017 paper (actually, there we increased the edge dose)
        - Reduced dose in layers above channel?
    - Reduced layer thickness along channel edges embedded in 10 &mu;m bulk layers, which is the full generalized 3D printing method in our Nature Communications paper
- &#10060; Have an underlying surface on which to build the layers that is always visible? This is basically replacing the grid with a solid surface.

## Monday, 2021-09-06

Try basics of running an external script file within Blender with `210906_use_external_script_file.blend` and `210906_use_external_script_file.py` and set up VS Code to do blender autocompletes.

## Saturday, 2021-09-11

**To do**

- &#9989; Run code from 2021-09-03 in external file edited with VS Code and produce a video to make sure full workflow still works.
- &#9989; Increase number of layers and change camera position to accommodate.
- Start to do L-shaped channel animation.

**Run 2021-09-03 from external file and produce a video**

- Move code verbatim to external python file.
- Start new blender file, go to Scripting workspace, create edit window, paste in short code to execute external python file.

Create video. Do next operations within Blender.

- Go to Animation workspace
- In output pane:
    - Keep 1920x1080 resolution
    - Choose AVI JPEG file format
    - Set quality to 100%
    - Other settings: 24 fps and render frames 1 to 170
- In Layout workspace turn off grid, XY lines, and origin (center points of objects)
    - Set viewport to be same as active camera: `View` &rarr; `Cameras` &rarr; `Active Camera`
    - `View` &rarr; `Viewport render animation`. **Works**.
- Select `Render` &rarr; `Render Animation`. It goes a lot slower than the preview method and creates a movie file with a static image. Why???
    - [Blender Eevee Tutorial: Animation and Render](https://www.youtube.com/watch?v=9817LRCcnYk) at about 8:40-9:05 shows how to change interpolation between keyframes. Timeline &rarr; Dope Sheet &rarr; turn off "Only show selected" arrowhead so that all of the keyframes are shown on the timeline. Then select an object &rarr; Channel &rarr; Extrapolation mode &rarr; Linear Extrapolation (`bpy.ops.action.extrapolation_type(type='LINEAR'`). I've tried figuring out how to set this programmatically with python, but no luck for now. I need to move on.
    - [Eevee render not looking same as my viewport!](https://www.reddit.com/r/blender/comments/iioc2m/eevee_render_not_looking_the_same_as_my_viewport/g380a7d/) - good thread.
- Change output folder for rendered animations to `~/Downloads/renderings` from `/tmp`

**Data structures and algorithm**

    Create z positions as floats
    Use each z position as a key in a dict
    For each key, have a list of objects, each with their own material
    Create a list of frame index tuples like [(frame0, frame1), (frame2, frame3), ...]
    Create objects and put them into the appropriate z position's list in the dict
    Loop over the dict

Or:
    
    dict:
    {z_position_1: {
        'objects': [],
        'beginning_frame': XX,
        'ending_frame': YY
        }
    }

Or:
    
    class Layer:
        z_position
        objects
        beginning_frame
        ending_frame
    Create list of objects ordered by increasing z position
    Loop over the list, setting keyframes and colors?

Or:
    
    class animated_object:
        object with its material
        set keyframes and colors
        
Hmm, trying things out and the `mesh.primitive_cube_add()` is problematic. Need alternatives.

- [Boolean difference modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/introduction.html#example)
- [How to join objects with Python?](https://blender.stackexchange.com/questions/13986/how-to-join-objects-with-python)
- [Shadows on alpha channel PNG's and eevee](https://blender.stackexchange.com/questions/123607/shadows-on-alpha-channel-pngs-and-eevee) &rarr; uses Alpha Clip mode instead of Alpha Blend


Learn how to difference 2 objects: [Boolean difference not making any diiference (Python scripting)](https://blender.stackexchange.com/questions/48160/boolean-difference-not-making-any-diiference-python-scripting) - **very good**. Implement it in `210911_difference_two_objects.blend`.

**Use different method of making a 3D layer object that gets ride of the scaling problem I was having by creating a primitive cube with no arguments and then changing its `.scale` property, followed by changing its `.location` property to put it where I want it.**

**I now have successful boolean difference to create channel layers**.

**To do**

- Problem with `clean_up` where it crashes on objects that are unlinked. **Need to fix.**
    - [How to delete object from scene through the Blender Python API](https://b3d.interplanety.org/en/how-to-delete-object-from-scene-through-the-blender-python-api/)
    - in code, print objects in for loop.
    - Delete by hand?
- Still need to figure out how to render animation rather than viewport render animation.


## Monday, 2021-09-13

[2.91 Python API No change after applying boolean modifier operator](https://blender.stackexchange.com/questions/196816/2-91-python-api-no-change-after-applying-boolean-modifier-operator).

- Implement the code in the final answer and see how it works. Works fine. Moves subtractive objects so they are not in the View Layer.
- Add my `clean_up()` code and it deletes objects in View Layer and then crashes:

        Info: Deleted 3 object(s)
        Traceback (most recent call last):
          File "/Users/nordin/Documents/Projects/notes_to_self/Blender/210913_stackexchange_example_difference.blend/Text", line 151, in <module>
          File "/Users/nordin/Documents/Projects/notes_to_self/Blender/210913_stackexchange_example_difference.blend/Text", line 147, in clean_up
        RuntimeError: Error: Object 'attach_hulls' can't be selected because it is not in View Layer 'View Layer'!


[How to use alpha transparent textures in Blender](https://artisticrender.com/how-to-use-alpha-transparent-textures-in-blender/). See section: "What is the differences between blend modes in Eevee?". Need to use `Alpha Blend`.

[Shader Nodes &rarr; Introduction](https://docs.blender.org/manual/en/latest/render/shader_nodes/introduction.html)

>An important concept to understand when building node setups is that of the shader socket. The output of all surface and volume shaders is a shader, describing lighting interaction at the surface or of the volume, rather than the color of the surface.

>There are a few types of shaders available as nodes:

>BSDF shader  
Describe light reflection, refraction and absorption at an object surface.

>Emission shader  
Describe light emission at an object surface or in a volume.

>Volume shader  
Describe light scattering inside a volume.

>Background shader  
Describe light emission from the environment.

>Each shader node has a color input, and outputs a shader. These can then be mixed and added together using Mix and Add Shader nodes. No other operations are permitted. The resulting output can then be used by the renderer to compute all light interactions, for direct lighting or global illumination.

Specific shaders

[Transparent BSDF](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/transparent.html) - *used to add transparency without refraction, passing straight through the surface, as if there were no geometry there. ... Note that only pure white transparent shaders are completely transparent.*

[Principled BSDF](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html) - *combines multiple layers into a single easy to use node.*

[Specular BSDF](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/specular_bsdf.html) - Eevee Only - *combines multiple layers into a single easy to use node.*

[Mix Shader](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/mix.html) - *used to mix two shaders together.*


# Tuesday, 2021-09-14

## Using nodes for material and shading with transparency

<span style="color:red; font-size:150%">&#x2605;</span> Watch [Blender 2.9+ Basic Material Transparency](https://www.youtube.com/watch?v=esIKF8WvaVg) from [Basic Alpha Transparency](https://www.katsbits.com/codex/alpha/#blender-29-transparency).

- Go to Shading workspace
- Select `Display render preview` in main 3D window
- Mix Shader Fac: 0.5
- Transparent BSDF (T-BSDF) Color: White
- Principled BSDF (P-BSDF):
    - In Shading workspace, add Texture &rarr; Image Texture and choose image `golden.png`.
    - **Vary Alpha to control transparency**
- Material Settings:
    - Blend Mode: Alpha Blend
    - Shadow Mode: None &rarr; critical
    - `Show Backface` makes object semi-transparent (i.e., can partially see through to backfaces of object) when Alpha set to 1.0. Uncheck and object is transparent but can't see backfaces of object, can see things behind the object. 

Principled and Transparent BSDF into Mix Shader with image texture:  
![](assets/Principled and Transparent BSDF into Mix Shader with image texture.png)  
Principled with base color and Transparent BSDF into Mix Shader:  
![](assets/Principled and Transparent BSDF into Mix Shader.png)  
Principled BSDF with base color only:  
![](assets/Principled BSDF only.png)  

### What I've learned:

1. For P-BSDF and T-BSDF put through a Mix Shader (with texture image):
    - Mix Shader Fac controls the ultimate transparency when P-BSDF Alpha &rarr; 1.0.
    - Show Backface does exactly what it says. When checked, Backface Culling removes backface so it looks the same as if Show Backface is unchecked. 
2. For P-BSDF with texture image:
    - Varying Alpha changes the overall transparency of the object
    - Absolutely turn off Show Backface!
3. For P-BSDF with manually set Base Color (no texture image):
    - Varying Alpha changes the overall transparency of the object
    - Absolutely turn off Show Backface!
    - **So, same as if use a texture image**

## Transparency animation fixing all of my previous problems

- Use #3 above (only P-BSDF with manually set Base Color)
- Set 3D view Viewport Shading in upper right corner to `Display render preview`
- Manually add keyframes at frames 1, 30, 45 with Alpha = 1, 0.023, 0.87, respectively
- In `Output Properties` set `File Format` to `AVI JPEG` and End frame to 65
- View &rarr; Viewport Render Animation &rArr; Good animation!
- Render &rarr; Render Animation &rArr; **Good animation from camera perspective!**
    - No evidence of edge lines
    - Smooth fade-in and fade-out animation with no jerk at end of coming to full transparency


## Next:

Apply this to 3D printed layer animation:

- Create material and apply it to objects (need unique material for each?? Can materials be cloned so can set up several base materials at beginning of code and just clone them for each layer?)
    - &#9989; How programmatically create material from python?
- Create animation, adding keyframes and changing alpha of materials, start with just bulk layers
- Then apply to channel layers made with boolean difference operation
- Do more complicated boolean difference operation to get 90&deg; channel bends
- Do edge exposure case with secondary images
- Do embedded different layer thicknesses and multiple exposure times

# Wednesday, 2021-09-15

Look up information about creating materials in Blender with Nodes:

- [Transparent material in Blender in render mode (Eevee or Cycles) in Python, Blender 2.93 [closed]](https://blender.stackexchange.com/questions/234268/transparent-material-in-blender-in-render-mode-eevee-or-cycles-in-python-blen)
- [Principled BSDF via Python API](https://blender.stackexchange.com/questions/160042/principled-bsdf-via-python-api)
- [Adding new Principled BSDF materials using python scripting](https://stackoverflow.com/questions/63098407/adding-new-principled-bsdf-materials-using-python-scripting)

# Thursday, 2021-09-16

## Info

<span style="color:red; font-size:150%">&#x2605;</span> [Blender 3D — How to create and render a scene in Blender using Python API, by Armindo Cachada | Jun 7, 2021](https://spltech.co.uk/blender-3d%E2%80%8A-%E2%80%8Ahow-to-create-and-render-a-scene-in-blender-using-python-api/) - *In this article, I will show you how you can create a scene in Blender, using the Python 2.93 Blender API.* - Cube, plane, light source, camera and constraining camera to point at an object (very easy to do).

## Task

### Objective

Create from scratch entire scene (light, camera, layers (no channels), materials) from python. When re-run script, delete everything and start fresh.

Info:

    Camera
    Location: 16.344, -15.382, 11.012
    Rotation (XYZ Euler): 63.9, 0.0, 46.7
    
    Light
    Point, 1000 W, Diffuse = Specular = Volume = 1.0, Radius = 0.1 m
    Location: 4.0762, 1.0055, 5.9039
    Rotation (XYZ Euler): 37.3, 3.16, 107

### Files
  
`210916_uniform_layers_with_materials.py`, `210916_uniform_layers_with_materials.blend`