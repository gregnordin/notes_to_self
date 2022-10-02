# Add-ons

## BOSL

[Belfry OpenScad Library - BOSL](https://github.com/revarbat/BOSL)

Includes:

- Great math library with 2D & 3D transforms
- Threading library


# Tuesday, 9/27/22

- Try out `rotate_extrude()`.
- Start creating `polylinehull` module.


# Wednesday, 9/28/22

- Create `polychannel` module.
- Create `serpentine` module.
- Create `serpentinecircularends` module.


# Thursday, 9/29/22

How create a polychannel that has one or more channel sections with a circular arc? Information needed for each arc (limit to only 90&deg; and 180&deg; arcs? Maybe also 45&deg; arcs, possibly 30/60&deg; arcs?):

- Cross sectional shape.
- Arc radius.
- Arc angular extent (usually 90&deg; or 180&deg;).
- Position for starting face of arc and vector for starting direction of arc (which is the surface normal of the starting face where the arc connects to the previous channel section).
- Whether the arc is in the xy, xz, or yz plane (i.e., axis of rotation for 90&deg;.

Approach:

- Convert relative positions to absolute positions (as needed).
- Parse shapes array and break into polychannel-arc-polychannel-arc sections.
- Sequentially handle polychannel sections with hull() and arc sections with rotate_extrude().

```
for shape in shapes:
    if shape == arc:
        create arc
    else:
        
```

```
shapes = {
    cube1
    cube2
    cube3 - position at face of arc
    arc1
    cube4 - position at face of arc
    cube5
}
relative_positions = {
    pos1
    pos2
    pos3
    0 (arc1 starts at position of last shape)
    0 (cube4 starts at position of arc endface)
    pos5
}
```

Alternatively, we could build a data structure where the shape and position information is all together:

```
polychannel_params = {
    {shape params-type and position}
}
```

Possibilities for circular arcs:

- [sweep()](https://github.com/openscad/list-comprehension-demos/blob/master/sweep.scad).
- [Snippet: Circular sector and arcs with OpenScad](https://www.xarg.org/snippet/circular-sector-and-arcs-with-openscad/) - looks simple, try it.
- [Circular sector and arc](https://openhome.cc/eGossip/OpenSCAD/SectorArc.html) - more complicated.


# 9/30/22 - 10/1/22

Try creating an arc with intersection of cubes rotated and moved along an arc. Led to idea to do something like this with flat plate-like shapes and hull() between them, which is compatible with the polychannel approach and would just need the shapes and positions of the shapes.

- &#9989; Try embedding the output of a function in a list&rarr; it works.
- `try_func_for_arc.scad`
    - &#9989; Create functions for absolute positions and relative positions along a 90&deg; arc.
    - &#9989; Make arc go from angle a to angle b (CCW).
    - &#9989; Make angle a and angle b handle CW as well as CCW directions.
    - &#9989; Put into a list with other positions.
- `try_shape3D_with_rotation`
    - &#9989; Add `rotate()` to shape3D.
        - &#9989; Shape data structure:
            - [`<shape>, <size>, <relative position>, <rotation>`]
                - `<shape>` = "cube" or "sphere/sphr"
                - `<size>` = [3, 2, 1]
                - `<position>` = [10, 12, 0] (absolute or relative, always specify as relative and then use function to turn it into absolute)
                - `<rotation>` &rarr; angle (a=90), axis of rotation (v=[0, 0, 1]) = [90, [0, 0, 1]]
            - Example
                - `["sphr", [0.01, 4, 4], [0, 0, 0], [45, [0, 0, 1]]]`
        - &#9989; Can `relative position` be easily turned into `absolute position` with this data structure? Write function to do it.
- Create new polychannel module to use the above shape3D and data structure.
- Create function to make new data structure entries for an arc that include positions and shape angles.
- Put into a list with other positions/shapes and input into polychannel.

