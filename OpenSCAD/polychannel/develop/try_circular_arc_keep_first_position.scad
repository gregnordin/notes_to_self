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

eps=0.01;
params_pos_relative = [
    ["sphr", [eps, 4, 4], [0, 10, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 4, 4], [7, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 3, 3], [0, 0, 0], [0, [0, 0, 1]]],  // Note relative position is zero; this line effectively just changes the size of the circle leaving it in the same place.
    ["cube", [eps, 0.5, 0.5], [3, 0, 0], [0, [0, 0, 1]]],
    ["cube", [0.5, 0.5, 0.5], [5, 0, 0], [0, [0, 0, 1]]],
    ["cube", [0.5, 0.5, 0.5], [0, 4, 0], [0, [0, 0, 1]]],
];

polychannel(params_pos_relative);
color("red") translate([0, 0, 5]) polychannel(params_pos_relative, show_only_shapes=true);


function test_func(a, test_bool=false) = test_bool ? a : [0, 0, 0];
function test_func2(a, test_bool=false) = [
    for (i=[0:1:3]) [
    i,
    i+1,
    i==0 ?i-1 : i+2,
    test_bool==true ? 100: -100,
    i==0 
        ? test_bool==true 
            ? a
            : [0, 0, 0]
        : 5
    // test_bool==true ? a : [0, 0, 0];
    ]
];

echo();
echo(test_func([1, 2, 3]));
echo(test_func([1, 2, 3], test_bool=true));
echo();
echo(test_func2([1, 2, 3]));
echo(test_func2([1, 2, 3], test_bool=true));
echo();
