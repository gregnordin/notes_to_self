use <polychannel.scad>

// Note: all examples use relative coordinates to specify shape positions.

eps = 0.01;
width = 2;
height = 1;

params_arc = [
    each arc_yz_rel_position("cube", [width, height, eps], radius=2, angle1=0, angle2=45, n=4),
];
translate([0, 0, 0]) {
    polychannel(params_arc, clr="Salmon", show_only_shapes=true);
    translate([0, 3, 0]) polychannel(params_arc);
};