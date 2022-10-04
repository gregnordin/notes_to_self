length = 10;
width_x = 0.5;
width_z = 1;
module shape() {
    translate([0, length/2, 0])
    cube([width_x, length, width_z], center=true);
}

shape();
color("Salmon") rotate(a=45, v=[1, 0, 0]) shape();
color("LightSlateGray") rotate(a=45, v=[-1, 0, 0]) shape();
