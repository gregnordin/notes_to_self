/*--------------------------------------------------------------------------------------
/ Serpentine channel module based on the polychannel module.
/
/ Serpentine long channel axis is y. As more long channel segments are added,
/ the serpentine channel grows in x.
/
/ Rev. 1, 9/28/22, by G. Nordin
--------------------------------------------------------------------------------------*/
use <polychannel.scad>

// Create a channel that follows a circular arc. Note that this is based on the 
// openscad function 'rotate_extrude', which is kind of weird so you have to 
// carefully read its documentation to understand what it does. The main points
// are that it takes a 2D x-y shape that is some distance from the x axis, flips
// it into the x-z plane and then rotates it about the z axis with a radius
// that is the 2D shape's distance from the x axis. Also, be sure to not have
// any translation of the 2D shape's position in the y dimension because this
// will bizarely be converted to an offset in the z direction for the extruded
// shape.
module channel_circular_arc(radius, chan_size, angle=180, center=true, clr="lightblue", convexity=10, fn=100) {
    assert(len(chan_size) == 2, "channel_circular_arc: chan_size must be have 2 dimensions")
    color(clr) 
        rotate_extrude(angle=angle, convexity=convexity, $fn=fn) 
            translate([radius, 0]) square(chan_size, center);
}

// Main serpentine channel module
module serpentine_channel(
    n = 4,                    // Number of serpentine segments
    l = 10,                   // Length of serpentine segment
    cross_section = [1, 0.8], // Size of channel in x,y,z
    gap = 2,                  // Gap between serpentine segments
    thin_size = 0.01,         // Thickness of rectangular plate used for polychannel channels
    clr = "lightblue"         // Color
) {
    size = [cross_section[0], thin_size, cross_section[1]];
    sizes = [size, size];
    positions = [
        [0, 0, 0],
        [0, l, 0]
    ];
    n_serp_segments = n;
    period = gap + cross_section[0];
    radius = 0.5 * period;

    for (i = [0: 1: n_serp_segments-1]) {
        x_pos = i * period;
        x_translation = [x_pos, 0, 0];
        polychannel(sizes, positions + [x_translation, x_translation], relative_positions=false, clr=clr);
        if (i != n_serp_segments-1) {
            if (i%2 == 0)
                translate([radius + i * period, positions[1][1], 0]) 
                    channel_circular_arc(radius, cross_section, clr=clr);
            else {
                translate([radius + i * period, positions[0][1], 0]) 
                    mirror([0, 1, 0]) 
                        channel_circular_arc(radius, cross_section, clr=clr);
            }
        }
    }
}

// Example usage - see serpentinecircularends_result.png for output
serpentine_channel();
translate([0, -17, -5]) serpentine_channel(n=13, l=15, gap=1, cross_section=[0.5, 1], clr="cornflowerblue");
translate([0, -50, -10]) serpentine_channel(n=6, l=25, gap=4, cross_section=[0.5, 10], clr="Salmon");
