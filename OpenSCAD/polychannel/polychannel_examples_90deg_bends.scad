use <polychannel.scad>

// Note: all examples use relative coordinates to specify shape positions.

eps = 0.01;
x_vec = [1, 0, 0];
y_vec = [0, 1, 0];
z_vec = [0, 0, 1];

// Simple rectangular straight channels and 90deg bends.
width_90bends = 1.5;
height_90bends = 1;
size_90bends = [width_90bends, width_90bends, height_90bends];
params_90bends = [
    ["cube", size_90bends, [0, 0, 0], [0, z_vec]],
    ["cube", size_90bends, [8, 0, 0], [0, z_vec]],
    ["cube", size_90bends, [0, 7, 0], [0, z_vec]],
    ["cube", size_90bends, [0, 0, 3], [0, z_vec]],
    ["cube", size_90bends, [0, -4, 0], [0, z_vec]],
    ["cube", size_90bends, [-3, 0, 0], [0, z_vec]],
    ["cube", size_90bends, [0, 0, -2], [0, z_vec]],
    ["cube", size_90bends, [-5, 0, 0], [0, z_vec]],
];
translate([0, 45, 0]) {
    polychannel(params_90bends, clr="Salmon", show_only_shapes=true);
    translate([0, 10, 0]) polychannel(params_90bends);
};

// Similar but use thin shapes.
params_90bends_thin = [
    ["cube", [eps, width_90bends, height_90bends], [0, 0, 0], [0, z_vec]],
    ["cube", [eps, width_90bends*sqrt(2), height_90bends], [8, 0, 0], [45, z_vec]],
    ["cube", [width_90bends, eps, height_90bends*sqrt(2)], [0, 7, 0], [45, x_vec]],
    ["cube", [width_90bends, eps, height_90bends*sqrt(2)], [0, 0, 3], [-45, x_vec]],
    ["cube", [eps, width_90bends*sqrt(2), height_90bends], [0, -4, 0], [45, z_vec]],
    ["cube", [eps, width_90bends, height_90bends*sqrt(2)], [-3, 0, 0], [-45, y_vec]],
    ["cube", [eps, width_90bends, height_90bends*sqrt(2)], [0, 0, -2], [-45, y_vec]],
    ["cube", [eps, width_90bends, height_90bends], [-5, 0, 0], [0, z_vec]],
];
translate([0, 20, 0]) {
    polychannel(params_90bends_thin, clr="Salmon", show_only_shapes=true);
    translate([0, 10, 0]) polychannel(params_90bends_thin);
};

// Similar but use circular arcs.
n_segs90 = 12;
radius90 = 1.5;
params_90bends_arcs = [
    ["cube", [eps, width_90bends, height_90bends], [0, 0, 0], [0, z_vec]],
    ["cube", [eps, width_90bends, height_90bends], [6.5, 0, 0], [0, z_vec]],
    each arc_xy_rel_position("cube", [width_90bends, eps, height_90bends], radius90, -90, 0, n_segs90),
    ["cube", [width_90bends, eps, height_90bends], [0, 4, 0], [0, z_vec]],
    each arc_yz_rel_position("cube", [width_90bends, height_90bends, eps], radius90, -90, 90, 2*n_segs90),
    ["cube", [width_90bends, eps, height_90bends], [0, -1.5, 0], [0, z_vec]],
    each arc_xy_rel_position("cube", [width_90bends, eps, height_90bends], radius90, 0, -90, n_segs90),
    ["cube", [eps, width_90bends, height_90bends], [-0.5, 0, 0], [0, z_vec]],
    each arc_xz_rel_position("cube", [height_90bends, width_90bends, eps], radius90/1.5, 90, 180, n_segs90),
    each arc_xz_rel_position("cube", [height_90bends, width_90bends, eps], radius90/1.5, 0, -90, n_segs90),
    ["cube", [eps, width_90bends, height_90bends], [-4, 0, 0], [0, z_vec]],
];
translate([0, 0, 0]) {
    polychannel(params_90bends_arcs, clr="Salmon", show_only_shapes=true);
    translate([0, 10, 0]) polychannel(params_90bends_arcs);
};