use <../polychannel.scad>

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


z_vec = [0, 0, 1];
n_segs90 = 12;
radius90 = 1.5;
width_90bends = 1.5;
height_90bends = 1;
params_90bends_arcs = [
    ["cube", [eps, width_90bends, height_90bends], [0, 0, 0], [0, z_vec]],
    // ["cube", [eps, width_90bends, height_90bends], [6.5, 0, 0], [0, z_vec]],
    each set_first_position(arc_xy_rel_position("cube", [width_90bends, eps, height_90bends], radius90, -90, 0, n_segs90), pos=[10, 0, 0]),
    ["cube", [width_90bends, eps, height_90bends], [0, 4, 0], [0, z_vec]],
    each arc_yz_rel_position("cube", [width_90bends, height_90bends, eps], radius90, -90, 90, 2*n_segs90),
    ["cube", [width_90bends, eps, height_90bends], [0, -1.5, 0], [0, z_vec]],
    each arc_xy_rel_position("cube", [width_90bends, eps, height_90bends], radius90, 0, -90, n_segs90),
    ["cube", [eps, width_90bends, height_90bends], [-0.5, 0, 0], [0, z_vec]],
    each arc_xz_rel_position("cube", [height_90bends, width_90bends, eps], radius90/1.5, 90, 180, n_segs90),
    each arc_xz_rel_position("cube", [height_90bends, width_90bends, eps], radius90/1.5, 0, -90, n_segs90),
    ["cube", [eps, width_90bends, height_90bends], [-7.5, 0, 0], [0, z_vec]],
];
polychannel(params_90bends_arcs, clr="Salmon", show_only_shapes=true);
translate([0, 10, 0]) 
    polychannel(params_90bends_arcs);

echo();
echo();
echo(get_final_position(params_90bends_arcs));
// echo(arc_xy_rel_position("cube", [width_90bends, eps, height_90bends], radius90, -90, 0, n_segs90));
// echo(set_first_position(arc_xy_rel_position("cube", [width_90bends, eps, height_90bends], radius90, -90, 0, n_segs90), pos=[10, 0, 0]));
echo();