use <polychannel.scad>

/*---------------------------------------------------------------------------------------
// Functions to convert between relative and absolute positions and vice versa in
// a list of shape/size/position/rotation parameters.
// 
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
function add_list_of_vecs(v) = [for(i=v) 1]*v;
function extract_rel_pos_vectors(p, n, pos_index=2) = [
    for (i=[0:1:n]) p[i][pos_index]
];
function rel_to_abs_position_oneline(p, line_index) = [
    p[line_index][0],
    p[line_index][1],
    add_list_of_vecs(extract_rel_pos_vectors(p, line_index)),
    p[line_index][3]
];
function rel_to_abs_positions(p) = [
    for (i=[0:1:len(p)-1]) rel_to_abs_position_oneline(p, i)
];

// Circular arc functions to calculate absolute and relative positions along an arc
// n is the number of segments in arc, so number of points in arc is n+1
function calc_arc_pos_i(radius, angle1, angle2, n, i) = [
    radius*cos(angle1 + i*(angle2-angle1)/n), 
    radius*sin(angle1 + i*(angle2-angle1)/n),
    0
];
function calc_arc_rot_i(angle1, angle2, n, i) = [
    angle1 + i*(angle2-angle1)/n, 
    [0, 0, 1]
];
function arc_pos_rot_oneline(shape, size, radius, angle1, angle2, n, i) = [
    shape, size, calc_arc_pos_i(radius, angle1, angle2, n, i), calc_arc_rot_i(angle1, angle2, n, i)
];
function arc_abs_position(shape, size, radius, angle1, angle2, n) = [
    for (i=[0:1:n]) arc_pos_rot_oneline(shape, size, radius, angle1, angle2, n, i)
];
function arc_rel_position(shape, size, radius, angle1, angle2, n) = 
    abs_to_rel_positions(arc_abs_position(shape, size, radius, angle1, angle2, n));


echo();
temp_n = 4;
temp_angle1 = 0;
temp_angle2 = -90;
temp_radius = 1;
// for (i=[0:1:temp_n])
//     echo(
//         i, calc_arc_pos_i(temp_radius, temp_angle1, temp_angle2, temp_n, i), 
//         calc_arc_rot_i(temp_angle1, temp_angle2, temp_n, i),
//         arc_pos_rot_oneline("cube", [1, 0.01, 2], temp_radius, temp_angle1, temp_angle2, temp_n, i)
//         );
// echo();

params_pos_absolute = arc_abs_position("cube", [1, 0.01, 2], temp_radius, temp_angle1, temp_angle2, temp_n);
echo(params_pos_absolute);
echo();

polychannel(params_pos_absolute);
translate([5, 0, 0]) polychannel(arc_abs_position("cube", [1, 0.01, 2], temp_radius, temp_angle1, 180, 2*temp_n));

test_params_pos_absolute = [
    ["cube", [1, 0.01, 2], [temp_radius, -2, 0], [0, [0, 0, 1]]],
    each arc_abs_position("cube", [1, 0.01, 2], temp_radius, temp_angle1, 90, temp_n),
    ["cube", [0.01, 1, 2], [-2, temp_radius, 0], [0, [0, 0, 1]]]
];
echo(test_params_pos_absolute);
test_params_pos_abs_to_relative = abs_to_rel_positions(test_params_pos_absolute);
test_params_pos_relative = [
    ["cube", [1, 0.01, 2], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [1, 0.01, 2], [0, 2, 0], [0, [0, 0, 1]]],
    each arc_rel_position("cube", [1, 0.01, 2], temp_radius, temp_angle1, 90, temp_n),
    ["cube", [0.01, 1, 2], [-2, 0, 0], [0, [0, 0, 1]]]
];
echo(test_params_pos_relative);

translate([-5, 0, 0]) polychannel(test_params_pos_absolute);
translate([-5, 0, 3]) polychannel(test_params_pos_abs_to_relative, relative_positions=true, clr="Salmon");
translate([-10, 0, 0]) polychannel(test_params_pos_relative, relative_positions=true, clr="MediumPurple");

