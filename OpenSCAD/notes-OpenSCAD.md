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

