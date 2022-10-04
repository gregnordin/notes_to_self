/*
Purpose: Develop parameter data structure, function to convert from 
relative to absolute position in the data structure, and shape3D
module that uses each data structure line to create a shape
with desired size, position, and rotational orientation.

Rev. 1.0, 10/1/22, G. Nordin
*/

$fn=50;

// Funadamental shape creation module for polychannel module.
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

// Function to add list of vectors. See add2() at 
// https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Tips_and_Tricks#Add_all_values_in_a_list
function add_list_of_vecs(v) = [for(i=v) 1]*v;
// // add_list_of_vecs works with lists of vectors
// input_vector_list = [ [2, 3] , [5, 8] , [10, 12] ];
// echo();
// echo(add_list_of_vecs(input_vector_list));
// // ECHO: [17, 23]
// echo();

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

// Test data
eps = 0.01;
params_pos_absolute = [
    ["sphr", [eps, 4, 4], [0, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 4, 4], [7, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 2, 2], [7, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 2*sqrt(2), 2], [10, 0, 0], [45, [0, 0, 1]]],
    ["cube", [eps, 2, 2], [10, 5, 0], [90, [0, 0, 1]]],
    ["cube", [3, 2, 3], [10, 10, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 1*sqrt(2), 1], [10, 15, 0], [45, [0, 0, 1]]],
    ["sphr", [eps, 2, 2], [15, 15, 0], [0, [0, 0, 1]]]
];
params_pos_relative = [
    ["sphr", [eps, 4, 4], [0, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 4, 4], [7, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 2, 2], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 2*sqrt(2), 2], [3, 0, 0], [45, [0, 0, 1]]],
    ["cube", [eps, 2, 2], [0, 5, 0], [90, [0, 0, 1]]],
    ["cube", [3, 2, 3], [0, 5, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 1*sqrt(2), 1], [0, 5, 0], [45, [0, 0, 1]]],
    ["sphr", [eps, 2, 2], [5, 0, 0], [0, [0, 0, 1]]]
];

// Calculate absolute positions from relative positions
test_params_pos_absolute = rel_to_abs_positions(params_pos_relative);
echo();

// Display relative, absolute, and calculated absolute positions
for (i=[0:1:len(params_pos_relative)-1]) {
    echo(params_pos_relative[i], params_pos_absolute[i], test_params_pos_absolute[i]);
}

// Draw shapes for visual confirmation.
for (p=test_params_pos_absolute) {
    // echo(p);
    shape3D(p[0], p[1], p[2], p[3]);
}
