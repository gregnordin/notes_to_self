use <polychannel.scad>

chan_size = [1, 0.8];
thin = 0.01;

module channel_circular_arc(radius, chan_size, angle=180, center=true, clr="lightblue", convexity=10, fn=100) {
    assert(len(chan_size) == 2, "channel_circular_arc: chan_size must be have 2 dimensions")
    color(clr) 
        rotate_extrude(angle=angle, convexity=convexity, $fn=fn) 
            translate([radius, 0]) square(chan_size, center);
}

// color("red") rotate_extrude(angle=180, convexity=10, $fn=100) translate([1.5, 0]) square(chan_size, true);

// color("blue", 0.5) translate([1.5, 0]) square(chan_size, true);

size = [chan_size[0], thin, chan_size[1]];

sizes = [size, size];
positions = [
    [0, 0, 0],
    [0, 10, 0]
];

polychannel(sizes, positions, relative_positions=true, clr="green");

n_serp_segments = 7;
gap_multiplier = 3;
gap = gap_multiplier * chan_size[0];
period = gap + chan_size[0];
radius = 0.5 * period;
translate([radius, positions[1][1], 0]) channel_circular_arc(radius, chan_size);

for (i = [0: 1: n_serp_segments-1]) {
    x_pos = i * period;
    x_translation = [x_pos, 0, 0];
    echo();
    polychannel(sizes, positions + [x_translation, x_translation], relative_positions=false, clr="green");
    if (i != n_serp_segments-1) {
        if (i%2 == 0)
            translate([radius + i * period, positions[1][1], 0]) channel_circular_arc(radius, chan_size);
        else {
            translate([radius + i * period, positions[0][1], 0]) mirror([0, 1, 0]) channel_circular_arc(radius, chan_size);
        }
    }
}

echo(2*positions[1]);
echo(3*positions);

for (i = [0: 1: n_serp_segments-1]) {
    x_pos = i * period;
    echo(x_pos);
}

