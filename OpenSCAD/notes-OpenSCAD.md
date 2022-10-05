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


# 9/30/22 - 10/5/22

Try creating an arc with intersection of cubes rotated and moved along an arc. Led to idea to do something like this with flat plate-like shapes and hull() between them, which is compatible with the polychannel approach and would just need the shapes and positions of the shapes.

- `try_embed_function_in_array.scad`
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
                - `<position>` = [10, 12, 0] can be absolute or relative, always specify as relative and then use function to turn it into absolute?
                - `<rotation>` &rarr; angle (a=90), axis of rotation (v=[0, 0, 1]) = [90, [0, 0, 1]]
            - Example
                - `["sphr", [0.01, 4, 4], [0, 0, 0], [45, [0, 0, 1]]]`
        - &#9989; Can `relative position` be easily turned into `absolute position` with this data structure? Write functions to do it. **Use simple single purpose functions that work together.** Openscad functions are too limiting to do it all in one function.
- &#9989; Create new polychannel module to use the above shape3D and data structure. **Do a lot of debugging.**
- &#9989; Expand example test data.
- `try_abs_to_rel_pos_conversion.scad`
    - &#9989; Create function to take an data structure with absolute positions and turn it into one with relative positions. I need this to make it simpler to create an arc data structure with relative positions.
- `try_circular_arc_xy_for_polychannel.scad`
    - **Positive angle rotation from x to y around +z axis.**
    - &#9989; Create function to make new data structure entries for an xy arc that includes positions and shape rotation angles. Use absolute positions to make it tractable given Openscad's limitations for functions.
    - &#9989; Put into a list with other positions/shapes and input into polychannel.
    - &#9989; Create relative position arc function.
    - &#9989; Use absolute to relative position converstion in list with other positions/shapes and input into polychannel.
    - &#9989; Try more extensive set of arc angles.
- `try_circular_arc_xz_for_polychannel.scad`
    - **Positive angle rotation from x to z around -y axis.**
    - &#9989; Create functions for xz arcs.
- `try_circular_arc_yz_for_polychannel.scad`
    - **Positive angle rotation from y to z around +x axis.**
    - &#9989; Create functions for yz arcs.
- &#9989; Move xy, xz, yz arc functions to `polychannels.scad`
- &#9989; Change polychannel default to `relative_positions=true`
- &#9989; Add examples that illustrate use of polychannel and arc features.
    - &#9989; Multiple sequential 90&deg; bends - `polychannel_examples_90deg_bends.scad`.
    - &#9989; Individual arcs that show starting position and sense of angular rotation.
    - &#9989; Shape changing.
    - &#9989; Round channels and turns.
- &#10060; Add a starting position to arc creation function so can use absolute positions?
- &#9989; Move examples into an examples directory.
- &#9989; Improve examples and text in project wiki.
- Fix README.md and notes-polychannel.md.
- Update `serpentine.scad` and `serpentine_circularends.scad`.
- Re-do Dallin's interleaved 1D mixer to use circular arcs for the narrow interleaved channels and the narrow channels feeding into and out of the high aspect ratio mixer channel.
- Utility functions
    - &#9989; Function to reverse the order of a list of shape/positions.
    - &#9989; Function to sum up all of the relative positions in a params list to give the final position.
    - &#9989; Function to get the final position from a list of shape/positions.


Other possible modules for channel paths that use the new data format developed above and the hull-based polychannel approach:

- S-curve.
    - Inputs:
        - radius1
        - radius2
        - Separation between input and output channels (= radius1 + radius2 + diff)
            - Separation direction (positive or negative)
        - Plane of S: xy, xz, yz
- 90&deg; xy bend with z change.
- [Bézier curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve) and linked Bezier curves.
    - [Python Bezier package](https://bezier.readthedocs.io/en/stable/python/reference/bezier.curve.html).
- [B-splines](https://en.wikipedia.org/wiki/B-spline)?
- Spirals.
- 3D serpentine channels with 90&deg; corners and with 180&deg; circular arc bends.
    - Stacked in z with channels in xy.
    - Stacked in x or y with vertical channels.

