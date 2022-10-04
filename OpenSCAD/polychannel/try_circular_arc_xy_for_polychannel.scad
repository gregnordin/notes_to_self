use <polychannel.scad>

/*---------------------------------------------------------------------------------------
// Circular arc functions to calculate absolute and relative positions along an arc
// n is the number of segments in arc, so number of points in arc is n+1.
//
// Examples
// --------
// test_arc = arc_xy_rel_position("cube", [1, 0.01, 2], 4, 0, 90, 12);
// test_params_pos_relative = [
//     ["cube", [1, 0.01, 2], [0, 0, 0], [0, [0, 0, 1]]],
//     ["cube", [1, 0.01, 2], [0, 2, 0], [0, [0, 0, 1]]],
//     each test_arc,
//     ["cube", [0.01, 1, 2], [-2, 0, 0], [0, [0, 0, 1]]]
// ];
/--------------------------------------------------------------------------------------*/
function _calc_arc_xy_pos_i(radius, angle1, angle2, n, i) = [
    radius*cos(angle1 + i*(angle2-angle1)/n), 
    radius*sin(angle1 + i*(angle2-angle1)/n),
    0
];
function _calc_arc_xy_rot_i(angle1, angle2, n, i) = [
    angle1 + i*(angle2-angle1)/n, 
    [0, 0, 1]
];
function _arc_xy_pos_rot_oneline(shape, size, radius, angle1, angle2, n, i) = [
    shape, size, _calc_arc_xy_pos_i(radius, angle1, angle2, n, i), _calc_arc_xy_rot_i(angle1, angle2, n, i)
];
function _arc_xy_abs_position(shape, size, radius, angle1, angle2, n) = [
    for (i=[0:1:n]) _arc_xy_pos_rot_oneline(shape, size, radius, angle1, angle2, n, i)
];
function arc_xy_rel_position(shape, size, radius, angle1, angle2, n) = 
    abs_to_rel_positions(_arc_xy_abs_position(shape, size, radius, angle1, angle2, n));

/*---------------------------------------------------------------------------------------
// Examples
/--------------------------------------------------------------------------------------*/

echo(); echo();
n_segs = 12;
radius = 2;
spacing = 4;

/*---------------------------------------------------------------------------------------
// 90deg arcs
/--------------------------------------------------------------------------------------*/
// 90deg arc
polychannel(rel_to_abs_positions(arc_xy_rel_position("cube", [1, 0.01, 2], radius, 0, 90, n_segs)));
// -90deg arc
translate([spacing, 0, 0]) 
    polychannel(rel_to_abs_positions(arc_xy_rel_position("cube", [1, 0.01, 2], radius, 0, -90, n_segs)));
// 90deg arc starting at -45deg
translate([2*spacing, 0, 0]) 
    polychannel(rel_to_abs_positions(arc_xy_rel_position("cube", [1, 0.01, 2], radius, -45, 45, n_segs)));
// -90deg arc starting at 45deg
translate([3*spacing, 0, 0]) 
    polychannel(rel_to_abs_positions(arc_xy_rel_position("cube", [1, 0.01, 2], radius, 45, -45, n_segs)));
// 90deg arc starting at 90deg
translate([0, -spacing, 0]) 
    polychannel(rel_to_abs_positions(arc_xy_rel_position("cube", [1, 0.01, 2], radius, 90, 180, n_segs)));
// 90deg arc starting at 180deg
translate([spacing, -spacing, 0]) 
    polychannel(rel_to_abs_positions(arc_xy_rel_position("cube", [1, 0.01, 2], radius, 180, 270, n_segs)));
// 90deg arc starting at 45deg
translate([2.5*spacing, -spacing, 0]) 
    polychannel(rel_to_abs_positions(arc_xy_rel_position("cube", [1, 0.01, 2], radius, 45, 135, n_segs)));
// 90deg arc starting at 135deg
translate([3.5*spacing, -spacing, 0]) 
    polychannel(rel_to_abs_positions(arc_xy_rel_position("cube", [1, 0.01, 2], radius, 135, 225, n_segs)));

/*---------------------------------------------------------------------------------------
// 180deg arcs
/--------------------------------------------------------------------------------------*/
// 180deg arc
translate([5*spacing, 0, 0]) 
    polychannel(rel_to_abs_positions(arc_xy_rel_position("cube", [1, 0.01, 2], radius, 0, 180, n_segs)));
// -180deg arc
translate([6.5*spacing, 0, 0]) 
    polychannel(rel_to_abs_positions(arc_xy_rel_position("cube", [1, 0.01, 2], radius, 0, -180, n_segs)));
// -180deg arc starting at 180deg
translate([7*spacing, 0, 0]) 
    polychannel(rel_to_abs_positions(arc_xy_rel_position("cube", [1, 0.01, 2], radius, 180, 0, n_segs)));
// 180deg arc starting at -90deg
translate([4.5*spacing, -1.5*spacing, 0]) 
    polychannel(rel_to_abs_positions(arc_xy_rel_position("cube", [1, 0.01, 2], radius, -90, 90, n_segs)));
// 180deg arc starting at -90deg
translate([5.5*spacing, -1.5*spacing, 0]) 
    polychannel(rel_to_abs_positions(arc_xy_rel_position("cube", [1, 0.01, 2], radius, 90, -90, n_segs)));

/*---------------------------------------------------------------------------------------
// 90deg, 180deg, 135deg arcs with entrance and exit channels
/--------------------------------------------------------------------------------------*/
n_segs90 = 12;
radius90 = 1;
spacing90 = 5;
clr = "Salmon";
test_params_pos_relative_90deg = [
    ["cube", [1, 0.01, 2], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [1, 0.01, 2], [0, 2, 0], [0, [0, 0, 1]]],
    each arc_xy_rel_position("cube", [1, 0.01, 2], radius90, 0, 90, n_segs90),
    ["cube", [0.01, 1, 2], [-2, 0, 0], [0, [0, 0, 1]]]
];
translate([-spacing90, 0, 0]) 
    polychannel(rel_to_abs_positions(test_params_pos_relative_90deg), clr="Salmon");

test_params_pos_relative_90deg_2 = [
    ["cube", [0.01, 1, 2], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [0.01, 1, 2], [-2, 0, 0], [0, [0, 0, 1]]],
    each arc_xy_rel_position("cube", [1, 0.01, 2], radius90, 90, 180, n_segs90),
    ["cube", [1, 0.01, 2], [0, -2, 0], [0, [0, 0, 1]]]
];
translate([-2*spacing90, 0, 0]) 
    polychannel(rel_to_abs_positions(test_params_pos_relative_90deg_2), clr="LightSlateGray");

test_params_pos_relative_180deg = [
    ["cube", [1, 0.01, 2], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [1, 0.01, 2], [0, 2, 0], [0, [0, 0, 1]]],
    each arc_xy_rel_position("cube", [1, 0.01, 2], radius90, 0, 180, n_segs90),
    ["cube", [1, 0.01, 2], [0, -2, 0], [0, [0, 0, 1]]]
];
translate([-1*spacing90, -1.5*spacing90, 0]) 
    polychannel(rel_to_abs_positions(test_params_pos_relative_180deg), clr="PaleTurquoise");

test_params_pos_relative_180deg_2 = [
    ["cube", [1, 0.01, 2], [0, 0, 0], [90, [0, 0, 1]]],
    ["cube", [1, 0.01, 2], [-2, 0, 0], [90, [0, 0, 1]]],
    each arc_xy_rel_position("cube", [1, 0.01, 2], radius90, 90, 270, n_segs90),
    ["cube", [1, 0.01, 2], [2, 0, 0], [90, [0, 0, 1]]]
];
translate([-2*spacing90, -1*spacing90, 0]) 
    polychannel(rel_to_abs_positions(test_params_pos_relative_180deg_2), clr="SeaGreen");


