use <../polychannel.scad>

function abs_to_rel_positions2(p, keep_first_position=false) = [
    for (i=[0:1:len(p)-1]) [
        p[i][0], 
        p[i][1],
        i==0
            ? keep_first_position==true
                ? p[i][2]
                : p[i][2] - p[i][2]
            : p[i][2] - p[i-1][2],
        p[i][3]
    ]
];

function abs_to_rel_positions_keep_first_position(p) = 
    abs_to_rel_positions2(p, keep_first_position=true);


eps=0.01;
// params_pos_relative = [
//     ["sphr", [eps, 4, 4], [0, 10, 0], [0, [0, 0, 1]]],
//     ["sphr", [eps, 4, 4], [7, 0, 0], [0, [0, 0, 1]]],
//     ["sphr", [eps, 3, 3], [0, 0, 0], [0, [0, 0, 1]]],  // Note relative position is zero; this line effectively just changes the size of the circle leaving it in the same place.
//     ["cube", [eps, 0.5, 0.5], [3, 0, 0], [0, [0, 0, 1]]],
//     ["cube", [0.5, 0.5, 0.5], [5, 0, 0], [0, [0, 0, 1]]],
//     ["cube", [0.5, 0.5, 0.5], [0, 4, 0], [0, [0, 0, 1]]],
// ];

params_pos_absolute = [
    ["sphr", [eps, 4, 4], [0, 10, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 4, 4], [7, 10, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 3, 3], [7, 10, 0], [0, [0, 0, 1]]],  // Note relative position is zero; this line effectively just changes the size of the circle leaving it in the same place.
    ["cube", [eps, 0.5, 0.5], [10, 10, 0], [0, [0, 0, 1]]],
    ["cube", [0.5, 0.5, 0.5], [15, 10, 0], [0, [0, 0, 1]]],
    ["cube", [0.5, 0.5, 0.5], [15, 14, 0], [0, [0, 0, 1]]],
];

abs_to_rel1 = abs_to_rel_positions2(params_pos_absolute);
abs_to_rel2 = abs_to_rel_positions_keep_first_position(params_pos_absolute);

// polychannel(abs_to_rel1);
// color("red") translate([0, 0, 5]) polychannel(abs_to_rel1, show_only_shapes=true);

// polychannel(abs_to_rel2);
// color("red") translate([0, 0, 5]) polychannel(abs_to_rel2, show_only_shapes=true);


function _calc_arc_xy_pos_i(radius, angle1, angle2, n, i, r0) = [
    r0[0] + radius*cos(angle1 + i*(angle2-angle1)/n), 
    r0[1] + radius*sin(angle1 + i*(angle2-angle1)/n),
    r0[2]
];
function _calc_arc_xy_rot_i(angle1, angle2, n, i) = [
    angle1 + i*(angle2-angle1)/n, 
    [0, 0, 1]
];
function _arc_xy_pos_rot_oneline(shape, size, radius, angle1, angle2, n, i, r0) = [
    shape, size, _calc_arc_xy_pos_i(radius, angle1, angle2, n, i, r0), _calc_arc_xy_rot_i(angle1, angle2, n, i)
];
function _arc_xy_abs_position(shape, size, radius, angle1, angle2, n, r0) = [
    for (i=[0:1:n]) _arc_xy_pos_rot_oneline(shape, size, radius, angle1, angle2, n, i, r0)
];
function arc_xy_rel_position(shape, size, radius, angle1, angle2, n, r0=[0,0,0]) = 
    abs_to_rel_positions_keep_first_x(_arc_xy_abs_position(shape, size, radius, angle1, angle2, n, r0));
function abs_to_rel_positions_keep_first_x(p) = [
    for (i=[0:1:len(p)-1]) [
        p[i][0], 
        p[i][1],
        i==0
            ? [p[i][2][0], 0, 0]
            : p[i][2] - p[i-1][2],
        p[i][3]
    ]
];

z_vec = [0, 0, 1];
n_segs90 = 12;
radius90 = 1.5;
width_90bends = 1.5;
height_90bends = 1;
size_90bends = [width_90bends, width_90bends, height_90bends];
params_90bends_arcs = [
    ["cube", [eps, width_90bends, height_90bends], [0, 0, 0], [0, z_vec]],
    ["cube", [eps, width_90bends, height_90bends], [6.5, 0, 0], [0, z_vec]],
    each arc_xy_rel_position("cube", [width_90bends, eps, height_90bends], radius90, -90, 0, n_segs90, r0=[0, 0, 0]),
    ["cube", [width_90bends, eps, height_90bends], [0, 4, 0], [0, z_vec]],
    each arc_yz_rel_position("cube", [width_90bends, height_90bends, eps], radius90, -90, 90, 2*n_segs90),
    ["cube", [width_90bends, eps, height_90bends], [0, -1.5, 0], [0, z_vec]],
    each arc_xy_rel_position("cube", [width_90bends, eps, height_90bends], radius90, 0, -90, n_segs90),
    ["cube", [eps, width_90bends, height_90bends], [-0.5, 0, 0], [0, z_vec]],
    each arc_xz_rel_position("cube", [height_90bends, width_90bends, eps], radius90/1.5, 90, 180, n_segs90),
    each arc_xz_rel_position("cube", [height_90bends, width_90bends, eps], radius90/1.5, 0, -90, n_segs90),
    ["cube", [eps, width_90bends, height_90bends], [-4, 0, 0], [0, z_vec]],
];
polychannel(params_90bends_arcs, clr="Salmon", show_only_shapes=true);
translate([0, 10, 0]) 
    polychannel(params_90bends_arcs);
