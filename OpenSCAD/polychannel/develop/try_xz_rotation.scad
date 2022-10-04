length = 10;
width_y = 0.5;
width_z = 1;
module shape() {
    translate([length/2, 0, 0])
    cube([length, width_y, width_z], center=true);
}

shape();
color("Salmon") rotate(a=45, v=[0, 1, 0]) shape();
color("LightSlateGray") rotate(a=45, v=[0, -1, 0]) shape();
