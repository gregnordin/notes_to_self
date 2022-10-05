use <../polychannel.scad>

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

final_position = get_final_position(params_pos_relative);
params_pos_absolute = rel_to_abs_positions(params_pos_relative);

echo();
echo(params_pos_relative);
echo();
echo(reverse_order(params_pos_relative));
echo();
echo(final_position);
echo(-final_position);
echo(get_final_position(params_pos_relative));
echo(params_pos_absolute);
echo(params_pos_absolute[5][2]);
echo();

color("Salmon") translate([0, 0, 5]) 
    polychannel(reverse_order(params_pos_relative));

// Equivalent set of operations:
color("Orchid") translate([0, 0, 10])
    translate(final_position)
        mirror([0, 1, 0]) mirror([1, 0, 0]) 
            polychannel(params_pos_relative);
