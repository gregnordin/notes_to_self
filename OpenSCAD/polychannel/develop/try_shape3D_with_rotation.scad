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
    : convert_params_rel_to_abs(p, n-1, r + p[n][2])[n][2];

// function add(v, n, i = 0, r = 0) = i <= n ? add(v, n, i + 1, r + v[i]) : r;
// input = [2, 3, 5, 8, 10, 12];
// for (i=[0:1:len(input)-1])
//     echo(add(input, n=i));

function add(v, i = 0, r = 0) = i < len(v) ? add(v, i + 1, r + v[i]) : r;
input = [2, 3, 5, 8, 10, 12];
output = add(input);
echo(output);

// Construct a sublist from given list
input_sub = [
    for (j=[0:1:2]) input[j]
];
echo(input_sub);
echo(add(input_sub));
for (i=[0:1:len(input)-1]) {
    input_sub = [
        for (j=[0:1:i]) input[j]
    ];
    echo(i, input_sub, add(input_sub));
}

// Construct a list of cummulative sums
echo();
echo("Cummulative sums");
cumm_sum = [
    for (i=[0:1:len(input)-1]) let (input_sub = [
        for (j=[0:1:i]) input[j]
    ]) add(input_sub)
];
echo(cumm_sum);
echo();
echo("cumm_sum_func");
function cumm_sum_func(v) = [
    for (i=[0:1:len(v)-1]) let (v_sub = [
        for (j=[0:1:i]) v[j]
    ]) add(v_sub)
];
echo(cumm_sum_func(input));

echo();
echo("Cummulative sum 2nd elements");
input2 = [[0, 2], [1, 3], [2, 5], [3, 8], [4, 10], [5, 12]];
echo(0, input2[0], input2[0][1]);
echo(1, input2[1], input2[1][1]);
cumm_sum2 = [
    for (i=[0:1:len(input2)-1]) let (input_sub = [
        for (j=[0:1:i]) input2[j][1]
    ]) add(input_sub)
];
echo(cumm_sum2);
echo();
echo("cumm_sum_func2");
function cumm_sum_func2(v) = [
    for (i=[0:1:len(v)-1]) let (v_sub = [
        for (j=[0:1:i]) v[j][1]
    ]) add(v_sub)
];
echo(cumm_sum_func2(input2));

echo();
echo("cumm_sum_func3");
function cumm_sum_func3(v, sum_index, pos_index=1) = [
    for (i=[sum_index:1:sum_index]) let (v_sub = [
        for (j=[0:1:i]) v[j][pos_index]
    ]) add(v_sub)
];
echo(2, cumm_sum_func3(input2, 2), cumm_sum_func3(input2, 2)[0]);


// function convert_rel_to_abs() = 
//     [

//     ];

function temp_rel_to_abs(p, n) = 
    [
        p[n][0],
        p[n][1],
        each convert_params_rel_to_abs(p, n)[2],
        p[n][3]
    ];

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

// function abs_pos(p, n, pos_index=2) = [
//     for i=[n:1:n] let (positions=[for (j=[0:1:n]) [p[pos_index][j]]]) positions
// ];

// echo();
// echo("Trying it out...");
// temp_absolute = [
//     for (p=params_pos_relative)  {};
// ]
// echo(temp_absolute);
// echo();


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
