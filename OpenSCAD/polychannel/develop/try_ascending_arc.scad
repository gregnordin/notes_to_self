use <../polychannel.scad>

function uniformly_increase_z(p, delta_z) = [
    for (i=[0:1:len(p)-1]) [
        p[i][0], 
        p[i][1],
        i==0
            ? p[i][2]
            : [p[i][2][0], p[i][2][1], p[i][2][2] + delta_z],
        p[i][3]
    ]
];

function uniformly_increase_in_one_dimension(p, delta, dimension="z") = [
    for (i=[0:1:len(p)-1]) [
        p[i][0], 
        p[i][1],
        i==0
            ? p[i][2]
            : dimension == "z"
                ? [p[i][2][0], p[i][2][1], p[i][2][2] + delta]
                : dimension == "y"
                    ? [p[i][2][0], p[i][2][1] + delta, p[i][2][2]]
                    : [p[i][2][0] + delta, p[i][2][1], p[i][2][2]],
        p[i][3]
    ]
];

function uniformly_increase_rel_pos(p, change_vec) = [
    for (i=[0:1:len(p)-1]) let (delta = change_vec/(len(p)-1))[
        p[i][0], 
        p[i][1],
        i==0
            ? p[i][2]
            : p[i][2] + delta,
        p[i][3]
    ]
];

function uniformly_increase_rel_pos_in_z(p, total_pos_change) = 
    uniformly_increase_rel_pos(p, [0, 0, total_pos_change]);
function uniformly_increase_rel_pos_in_y(p, total_pos_change) = 
    uniformly_increase_rel_pos(p, [0, total_pos_change, 0]);
function uniformly_increase_rel_pos_in_x(p, total_pos_change) = 
    uniformly_increase_rel_pos(p, [total_pos_change, 0, 0]);


eps = 0.01;
chan1 = [
    ["cube", [2, eps, 1], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [2, eps, 1], [0, 3, 0], [0, [0, 0, 1]]],
    each arc_xy_rel_position("cube", [2, eps, 1], radius=3, angle1=0, angle2=90, n=10),
    ["cube", [eps, 2, 1], [-3, 0, 0], [0, [0, 0, 1]]],
];
polychannel(chan1);

// Increase z by 0.2
arc2 = [
    ["cube", [2, eps, 1], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [2, eps, 1], [0, 3, 0], [0, [0, 0, 1]]],
    each uniformly_increase_rel_pos(
        arc_xy_rel_position("cube", [2, eps, 1], radius=3, angle1=0, angle2=90, n=10),
        [0, 0, 2]
    ),
    ["cube", [eps, 2, 1], [-3, 0, 0], [0, [0, 0, 1]]],
];
translate([5, 0, 0])
    polychannel(arc2); //, show_only_shapes=true);

echo();
echo(arc2);
echo("arc2 final position:", get_final_position(arc2));
echo([1, 2, 3] / 3);
echo();

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
