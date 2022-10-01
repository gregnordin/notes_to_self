/*
Purpose: Develop parameter data structure, function to convert from 
relative to absolute position in the data structure, and shape3D
module that uses each data structure line to create a shape
with desired size, position, and rotational orientation.

Rev. 1.0, 10/1/22, G. Nordin
*/

$fn=50;

// Functions to convert from relative to absolute positions.
function convert_params_rel_to_abs(p, n, r=[0, 0, 0]) = n <=0
    ? [p[n][0], p[n][1], p[n][2] + r, p[n][3]]
    : convert_params_rel_to_abs(p, n-1, r + p[n][2]);

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

// Print test data relative and absolute positions
for (i=[0:1:len(params_pos_relative)-1]) {
    echo(params_pos_relative[i], params_pos_absolute[i]);
}
// Calculate absolute positions from relative positions
echo();
for (i=[0:1:len(params_pos_relative)-1]) {
    echo(params_pos_relative[i], convert_params_rel_to_abs(params_pos_relative, i));
}
echo();

// Draw shapes for visual confirmation.
for (p=params_pos_absolute) {
    // echo(p);
    shape3D(p[0], p[1], p[2], p[3]);
}
