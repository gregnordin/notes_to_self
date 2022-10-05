/*--------------------------------------------------------------------------------------
/ General purpose multi-segment channel module: polychannel.
/
/ Given a list of sizes and positions, a series of connected channels is constructed
/ using the hull() operation to connect sequential pairs of cubes with specified
/ size and position as given in the sizes and positions list.
/
/ Rev. 1, 9/28/22, by G. Nordin - Initial version
/ Rev. 1.5, 9/29/22, by Dallin Miner - Modify to select sphere as well as cube shapes
/ Rev. 2, 10/1/22, by G. Nordin - Generalize to include rotation of shapes
/ Rev. 3, 10/4/22, by G. Nordin - Generalize to include rotation of shapes
--------------------------------------------------------------------------------------*/
$fn=50;

echo();
echo();


/*---------------------------------------------------------------------------------------
// polychannel module.
/--------------------------------------------------------------------------------------*/
// This is the module that should always be used. It is set by default to operate on
// shape-position lists that use relative positions for the elements.
module polychannel(params, relative_positions=true, clr="lightblue", center=true, show_only_shapes=false) {
    if (relative_positions) {
        params_abs = rel_to_abs_positions(params);
        polychannel_absolute_positions(params_abs, clr=clr, center=center, show_only_shapes=show_only_shapes);
    } else {
        polychannel_absolute_positions(params, clr=clr, center=center, show_only_shapes=show_only_shapes);
    }
}

// Module that does the heavy lifting of creating a polychannel. Should be used by calling
// the polychannel() module.
module polychannel_absolute_positions(params, clr="lightblue", center=true, show_only_shapes=false) {
    // echo("len(params)", len(params));
    // echo("params", params);
    if (show_only_shapes) {
        for (i = [0:1:len(params)-1]) {
            // echo("shapes only", i, params[i]);
            color(clr) shape3D(params[i][0], params[i][1], params[i][2], params[i][3], center=center);
        }
    } else {
        for (i = [1:1:len(params)-1]) {
            // echo("with hull", i, params[i-1], params[i]);
            color(clr) hull() {
                shape3D(params[i-1][0], params[i-1][1], params[i-1][2], params[i-1][3], center=center);
                shape3D(params[i][0], params[i][1], params[i][2], params[i][3], center=center);
            };
        };
    }
}


/*---------------------------------------------------------------------------------------
// Fundamental shape creation module for polychannel module.
/--------------------------------------------------------------------------------------*/
module shape3D(shape, size, position, rotation, center=true) {
    a = rotation[0];
    v = rotation[1];
    if(shape=="cube"){
        translate(position) rotate(a=a, v=v) cube(size, center=center);
    }
    else if(shape=="sphr" || shape=="sphere"){
        translate(position) rotate(a=a, v=v)  scale(size) sphere(d=1);
    }
    else {
        assert(false, "invalid shape");
    }
}


/*---------------------------------------------------------------------------------------
// Utility functions.
--------------------------------------------------------------------------------------*/

// Reverse the order of a list of parameters with relative positions.
function reverse_order(p) = [
    for (i=[len(p)-1:-1:0]) [
        p[i][0], 
        p[i][1],
        i==len(p)-1
            ? p[0][2]
            : p[i+1][2],
        p[i][3]
    ]
];

// Get all of the relative position vectors from list of parameters.
function extract_all_rel_position_vectors(p) =
    _extract_rel_pos_vectors_up_to_n(params_pos_relative, len(params_pos_relative)-1);

// Return the final position of the center of the last element for a 
// list of parameters that uses relative position vectors.
function get_final_position(p) = rel_to_abs_positions(p)[len(p)-1][2];


/*---------------------------------------------------------------------------------------
// Functions to convert between relative and absolute positions and vice versa in
// a list of shape/size/position/rotation parameters.
//
// Examples
// --------
// params_absolute = [
//   ["cube", [1, 1, 2], [0, 0, 0], [0, [0, 0, 1]]],
//   ["cube", [1, 1, 2], [5, 0, 0], [0, [0, 0, 1]]],
//   ["cube", [1, 1, 2], [5, 4, 0], [0, [0, 0, 1]]],
//   ["cube", [1, 1, 2], [8, 4, 0], [0, [0, 0, 1]]],
// ];
// params_relative = [
//   ["cube", [1, 1, 2], [0, 0, 0], [0, [0, 0, 1]]],
//   ["cube", [1, 1, 2], [5, 0, 0], [0, [0, 0, 1]]],
//   ["cube", [1, 1, 2], [0, 4, 0], [0, [0, 0, 1]]],
//   ["cube", [1, 1, 2], [3, 0, 0], [0, [0, 0, 1]]],
// ];
//
// // Will be equal to params_relative:
// p_relative_test = abs_to_rel_positions(params_absolute);
// echo(p_relative_test);
// echo(params_relative);
//
// // Will be equal to params_absolute:
// p_absolute_test = rel_to_abs_positions(params_relative);  
// echo(p_absolute_test);
// echo(params_absolute);
/--------------------------------------------------------------------------------------*/
function abs_to_rel_positions(p) = [
    for (i=[0:1:len(p)-1]) [
        p[i][0], 
        p[i][1],
        i==0
            ? p[i][2] - p[i][2]
            : p[i][2] - p[i-1][2],
        p[i][3]
    ]
];
// Function to add list of vectors. See add2() at 
// https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Tips_and_Tricks#Add_all_values_in_a_list
function _add_list_of_vecs(v) = [for(i=v) 1]*v;
function _extract_rel_pos_vectors_up_to_n(p, n, pos_index=2) = [
    for (i=[0:1:n]) p[i][pos_index]
];
function rel_to_abs_position_oneline(p, line_index) = [
    p[line_index][0],
    p[line_index][1],
    _add_list_of_vecs(_extract_rel_pos_vectors_up_to_n(p, line_index)),
    p[line_index][3]
];
function rel_to_abs_positions(p) = [
    for (i=[0:1:len(p)-1]) rel_to_abs_position_oneline(p, i)
];


/*---------------------------------------------------------------------------------------
// Circular arc functions to calculate absolute and relative positions along an arc in xy.
// n is the number of segments in arc, so number of points in arc is n+1.
//
// Example
// -------
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
// Circular arc functions to calculate absolute and relative positions along an arc in xz.
// n is the number of segments in arc, so number of points in arc is n+1.
/--------------------------------------------------------------------------------------*/
function _calc_arc_xz_pos_i(radius, angle1, angle2, n, i) = [
    radius*cos(angle1 + i*(angle2-angle1)/n), 
    0,
    radius*sin(angle1 + i*(angle2-angle1)/n)
];
function _calc_arc_xz_rot_i(angle1, angle2, n, i) = [
    angle1 + i*(angle2-angle1)/n, 
    [0, -1, 0]
];
function _arc_xz_pos_rot_oneline(shape, size, radius, angle1, angle2, n, i) = [
    shape, size, _calc_arc_xz_pos_i(radius, angle1, angle2, n, i), _calc_arc_xz_rot_i(angle1, angle2, n, i)
];
function _arc_xz_abs_position(shape, size, radius, angle1, angle2, n) = [
    for (i=[0:1:n]) _arc_xz_pos_rot_oneline(shape, size, radius, angle1, angle2, n, i)
];
function arc_xz_rel_position(shape, size, radius, angle1, angle2, n) = 
    abs_to_rel_positions(_arc_xz_abs_position(shape, size, radius, angle1, angle2, n));

/*---------------------------------------------------------------------------------------
// Circular arc functions to calculate absolute and relative positions along an arc in yz.
// n is the number of segments in arc, so number of points in arc is n+1.
/--------------------------------------------------------------------------------------*/
function _calc_arc_yz_pos_i(radius, angle1, angle2, n, i) = [
    0,
    radius*cos(angle1 + i*(angle2-angle1)/n), 
    radius*sin(angle1 + i*(angle2-angle1)/n)
];
function _calc_arc_yz_rot_i(angle1, angle2, n, i) = [
    angle1 + i*(angle2-angle1)/n, 
    [1, 0, 0]
];
function _arc_yz_pos_rot_oneline(shape, size, radius, angle1, angle2, n, i) = [
    shape, size, _calc_arc_yz_pos_i(radius, angle1, angle2, n, i), _calc_arc_yz_rot_i(angle1, angle2, n, i)
];
function _arc_yz_abs_position(shape, size, radius, angle1, angle2, n) = [
    for (i=[0:1:n]) _arc_yz_pos_rot_oneline(shape, size, radius, angle1, angle2, n, i)
];
function arc_yz_rel_position(shape, size, radius, angle1, angle2, n) = 
    abs_to_rel_positions(_arc_yz_abs_position(shape, size, radius, angle1, angle2, n));


// Example
eps = 0.01;

params_pos_relative = [
    ["sphr", [eps, 4, 4], [0, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 4, 4], [7, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 3, 3], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 1, 1], [3, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 1*sqrt(2), 1], [3, 0, 0], [45, [0, 0, 1]]],
    ["cube", [eps, 1, 1], [0, 2, 0], [90, [0, 0, 1]]],
    ["cube", [3, 1, 3], [0, 3, 0], [0, [0, 0, 1]]],
    ["cube", [1, eps, 1], [0, 2, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 1*sqrt(2), 1], [0, 2, 0], [45, [0, 0, 1]]],
    ["sphr", [eps, 2, 2], [5, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [2, 2, 2], [2, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [2, 2, 2], [0, -4, 4], [0, [0, 0, 1]]],
    ["cube", [1, eps, 2], [0, -3, 0], [0, [0, 0, 1]]],
    each arc_xy_rel_position("cube", [1, eps, 2], radius=3, angle1=0, angle2=-90, n=10),
    ["cube", [1, 1, 2], [-2, 0, 0], [0, [0, 0, 1]]],
    each arc_xz_rel_position("cube", [2, 1, eps], radius=3, angle1=-90, angle2=-270, n=20),
    each arc_xy_rel_position("cube", [1, eps, 2], radius=1, angle1=-90, angle2=0, n=10),
    ["cube", [1, eps, 1], [0, 5, 0], [0, [0, 0, 1]]],
    each arc_xy_rel_position("cube", [1, eps, 1], radius=1, angle1=0, angle2=90, n=10),
    ["cube", [eps, 1, 1], [-15, 0, 0], [0, [0, 0, 1]]],
];
params_pos_absolute = rel_to_abs_positions(params_pos_relative);

polychannel(params_pos_relative, clr="red", show_only_shapes=true);
translate([0, 25, 0]) polychannel(params_pos_absolute, relative_positions=false);
translate([0, -25, 0]) polychannel(params_pos_relative, clr="Salmon");

echo();
echo(get_final_position(params_pos_relative));
echo();
