/*--------------------------------------------------------------------------------------
/ Serpentine channel module based on the polychannel module.
/
/ Serpentine long channel axis is y. As more long channel segments are added,
/ the serpentine channel grows in x. 
/
/ See serpentine_algorithm.jpg to see the method used by this code.
/
/ Rev. 1, 9/28/22, by G. Nordin
--------------------------------------------------------------------------------------*/
use <polychannel.scad>

// Functions to help create the relative positions for the long
// serpentine channel segments.
function serp_rel_x_pos(n, lx) = n == 0
    ? 0
    : lx * ((n+1) % 2);

function sign(n) = (n+1) % 4 == 0
    ? -1
    : 1;

function serp_rel_y_pos(n, ly) = ly * (n%2) * sign(n);

echo([for (i = [0:1:7]) serp_rel_x_pos(i, 2)]);
echo([for (i = [0:1:7]) sign(i)]);
echo([for (i = [0:1:7]) serp_rel_y_pos(i, 3)]);
echo([for (i = [0:1:7]) [serp_rel_x_pos(i, 2), serp_rel_y_pos(i, 3), 0]]);

// Main serpentine channel module
module serpentine_channel(
    n = 4,              // Number of serpentine segments
    l = 15,             // Length of serpentine segment
    size = [1, 1, 1],   // Size of channel in x,y,z
    gap = 2,            // Gap between serpentine segments
    clr = "lightblue"   // Color
) {
    n_serp_segments = n;
    n_gap_segments = n_serp_segments - 1;
    n_positions = n_serp_segments + n_gap_segments + 1;
    // echo("n_serp_segments:", n_serp_segments);
    // echo("n_gap_segments:", n_gap_segments);
    // echo("n_positions:", n_positions);
    shapes = [for (i= [0: 1: n_positions-1])["cube", size]];
    // echo(shapes);

    lx = gap + size[0];
    ly = l - size[1];
    // echo("lx, ly", lx, ly);
    positions = [for (i= [0: 1: n_positions-1]) [serp_rel_x_pos(i, lx), serp_rel_y_pos(i, ly), 0]];
    // echo(positions);

    polychannel(shapes, positions, relative_positions=true, clr=clr);
}

// Example usage - see serpentine_result.png for output
serpentine_channel();
size = [0.5, 2, 20];
translate([0, 0, -20]) serpentine_channel(n=9, l=25, size=size, clr="Salmon");
echo("");
