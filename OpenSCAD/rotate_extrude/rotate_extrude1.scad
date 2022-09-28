// Example below taken from https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#rotate_extrude
eps = 0.01;
// translate([eps, 60, 0])
   rotate_extrude(angle=270, convexity=10)
       translate([40, 50]) circle(10);
// rotate_extrude(angle=90, convexity=10)
//    translate([20, 0]) circle(10);
// translate([20, eps, 0])
//    rotate([90, 0, 0]) cylinder(r=10, h=80+eps);

// Play around
// color("red") 
//    rotate_extrude(angle=270, convexity=10)
    // translate([25, 0]) circle(20);

// 90 deg rectangular bend
size = [20, 15];
color("red") rotate_extrude(angle=90, convexity=10, $fn=100) translate([100, 0]) square(size, true);
