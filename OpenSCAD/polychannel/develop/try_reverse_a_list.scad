use <../polychannel.scad>

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
function extract_all_rel_position_vectors(p) =
    _extract_rel_pos_vectors(params_pos_relative, len(params_pos_relative)-1);



eps = 0.01;
params_pos_relative = [
    ["sphr", [eps, 4, 4], [0, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 4, 4], [7, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 3, 3], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 0.5, 0.5], [3, 0, 0], [0, [0, 0, 1]]],
    ["cube", [0.5, 0.5, 0.5], [5, 0, 0], [0, [0, 0, 1]]],
    ["cube", [0.5, 0.5, 0.5], [0, 4, 0], [0, [0, 0, 1]]],
];
polychannel(params_pos_relative);

rel_positions = extract_all_rel_position_vectors(params_pos_relative);
final_position = _add_list_of_vecs(rel_positions);

echo();
echo(params_pos_relative);
echo();
echo(reverse_order(params_pos_relative));
echo();
echo(rel_positions);
echo(final_position);
echo(-final_position);
echo();

color("Salmon") translate([0, 0, 5]) 
    polychannel(reverse_order(params_pos_relative));

// Equivalent set of operations:
color("Orchid") translate([0, 0, 10])
    translate(final_position)
        mirror([0, 1, 0]) mirror([1, 0, 0]) 
            polychannel(params_pos_relative);
