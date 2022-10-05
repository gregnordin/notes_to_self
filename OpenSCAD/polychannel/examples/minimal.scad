use <../polychannel.scad>

eps = 0.01;
params_pos_relative = [
    ["sphr", [eps, 4, 4], [0, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 4, 4], [7, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 3, 3], [0, 0, 0], [0, [0, 0, 1]]],  // Note relative position is zero; this line effectively just changes the size of the circle leaving it in the same place.
    ["cube", [eps, 0.5, 0.5], [3, 0, 0], [0, [0, 0, 1]]],
    ["cube", [0.5, 0.5, 0.5], [5, 0, 0], [0, [0, 0, 1]]],
    ["cube", [0.5, 0.5, 0.5], [0, 4, 0], [0, [0, 0, 1]]],
];
polychannel(params_pos_relative);
color("red") translate([0, 0, 5]) polychannel(params_pos_relative, show_only_shapes=true);

//Annotations
color("blue") translate([8,-4,0]) rotate([90,0,0]) scale(0.1) text("polychannel() output",halign="center",valign="center");
color("blue") translate([8,-4,5]) rotate([90,0,0]) scale(0.1) text("Shapes-only",halign="center",valign="center");

