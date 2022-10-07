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

function abs_to_rel_positions_keep_first_position(p) = 
    abs_to_rel_positions2(p, keep_first_position=true);


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

abs_to_rel1 = abs_to_rel_positions2(params_pos_absolute);
abs_to_rel2 = abs_to_rel_positions_keep_first_position(params_pos_absolute);

polychannel(abs_to_rel1);
color("red") translate([0, 0, 5]) polychannel(abs_to_rel1, show_only_shapes=true);

polychannel(abs_to_rel2);
color("red") translate([0, 0, 5]) polychannel(abs_to_rel2, show_only_shapes=true);
