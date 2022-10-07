use <../polychannel.scad>

module stick() {
    cube([10, 2, 1]);
}

color("lightblue") stick();

rot_x_45 = rot_x(45);
color("red") rotate(a=rot_x_45[0], v=rot_x_45[1]) stick();

rot_y_45 = rot_y(45);
color("lightgreen") rotate(a=rot_y_45[0], v=rot_y_45[1]) stick();

rot_z_45 = rot_z(45);
color("gray") rotate(a=rot_z_45[0], v=rot_z_45[1]) stick();

// Annotations
color("lightblue") translate([15,4,3]) rotate([90,0,180]) scale(0.1) text("Original",halign="center",valign="center");
color("red") translate([15,4,1.6]) rotate([90,0,180]) scale(0.1) text("rot_x(45)",halign="center",valign="center");
color("lightgreen") translate([15,4,0.2]) rotate([90,0,180]) scale(0.1) text("rot_y(45)",halign="center",valign="center");
color("gray") translate([15,4,-1.2]) rotate([90,0,180]) scale(0.1) text("rot_z(45)",halign="center",valign="center");
