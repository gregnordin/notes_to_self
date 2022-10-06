use <../polychannel.scad>

eps = 0.01;
base_arc_xy = arc_xy_rel_position("cube", [2, eps, 1], radius=4, angle1=0, angle2=90, n=10);
chan1 = [
    ["cube", [2, eps, 1], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [2, eps, 1], [0, 3, 0], [0, [0, 0, 1]]],
    each base_arc_xy,
    ["cube", [eps, 2, 1], [-3, 0, 0], [0, [0, 0, 1]]],
];
polychannel(chan1);
echo(get_final_position(chan1));

chan2 = [
    ["cube", [2, eps, 1], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [2, eps, 1], [0, 3, 0], [0, [0, 0, 1]]],
    each uniformly_increase_rel_pos_in_z(base_arc_xy, -2),
    ["cube", [eps, 2, 1], [-8, 0, 0], [0, [0, 0, 1]]],
];
translate([5, 0, 0])
    polychannel(chan2);

chan3 = [
    ["cube", [2, eps, 1], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [2, eps, 1], [0, 3, 0], [0, [0, 0, 1]]],
    each uniformly_increase_rel_pos_in_z(base_arc_xy, 4),
    ["cube", [eps, 2, 1], [-13, 0, 0], [0, [0, 0, 1]]],
];
translate([10, 0, 0])
    polychannel(chan3);

chan4 = [
    ["cube", [2, eps, 1], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [2, eps, 1], [0, 3, 0], [0, [0, 0, 1]]],
    each base_arc_xy,
    ["cube", [eps, 2, 1], [-4, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 2, 1], [-2, 0, 2], [0, [0, 0, 1]]],
    ["cube", [eps, 2, 1], [-12, 0, 0], [0, [0, 0, 1]]],
];
translate([15, 0, 0])
    polychannel(chan4);


// Simple test channel to manually look at modified relative positions in the Console.
arc_test = [
    ["cube", [2, eps, 1], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [2, eps, 1], [0, 3, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 2, 1], [-3, 0, 0], [0, [0, 0, 1]]],
];
arc_test_mod = uniformly_increase_rel_pos(arc_test, [0, 0, 1]);
echo();
echo(arc_test);
echo(arc_test_mod);
echo();
