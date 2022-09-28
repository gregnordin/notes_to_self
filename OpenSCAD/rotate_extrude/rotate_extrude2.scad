chan_size = [1, 0.8];

color("red") rotate_extrude(angle=180, convexity=10, $fn=100) translate([1.5, 0]) square(chan_size, true);

color("blue", 0.5) translate([1.5, 0]) square(chan_size, true);
