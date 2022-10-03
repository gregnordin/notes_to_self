// Purpose: develop a function that converts parameters data structure from
// absolute to relative positions.

function simple_copy(p) = [
    for (i=[0:1:len(p)-1]) p[i]
];

function copy_using_individual_elements(p) = [
    for (i=[0:1:len(p)-1]) [
        p[i][0], 
        p[i][1],
        p[i][2],
        p[i][3]
    ]
];

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

// Test data
eps = 0.01;
params_pos_absolute = [
    ["sphr", [eps, 4, 4], [0, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 4, 4], [7, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 1, 1], [7, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 1*sqrt(2), 1], [10, 0, 0], [45, [0, 0, 1]]],
    ["cube", [eps, 1, 1], [10, 2, 0], [90, [0, 0, 1]]]
];
params_pos_relative = [
    ["sphr", [eps, 4, 4], [0, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 4, 4], [7, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 1, 1], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 1*sqrt(2), 1], [3, 0, 0], [45, [0, 0, 1]]],
    ["cube", [eps, 1, 1], [0, 2, 0], [90, [0, 0, 1]]]
];

// Try it out
echo(params_pos_absolute);
echo(simple_copy(params_pos_absolute));
echo(copy_using_individual_elements(params_pos_absolute));
echo(abs_to_rel_positions(params_pos_absolute));
