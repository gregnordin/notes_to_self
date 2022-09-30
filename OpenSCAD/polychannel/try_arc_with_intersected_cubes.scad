module shape3D(size, position, center=true) {
    translate(position) cube(size, center=center);
}

size1 = [1, 0.01, 1];
pos1 = [5, 0, 0];

angle_total = 90;
angle_increment = 10;
n_seg = angle_total / angle_increment;
echo("n_seg", n_seg);

// shape3D(size1, pos1);

for (i = [0:1:n_seg]) {
    color("red") rotate(a=i*angle_increment, v=[0,0,1]) shape3D(size1, pos1);
}

echo(norm([1, 1, 1]));

// // Below: play with rotate() operation
// // Manual example:
// // https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#rotate
// x= 5; y = 10; z = 10; // point coordinates of end of cylinder
 
// length = norm([x,y,z]);  // radial distance
// b = acos(z/length); // inclination angle
// c = atan2(y,x);     // azimuthal angle

// rotate([0, b, c]) 
//     cylinder(h=length, r=0.5, $fn=50);
// %cube([x,y,z]); // corner of cube should coincide with end of cylinder

// translate([0, 20, 0]) {
//     // color("red")
//     rotate([0, b, 0]) rotate([0, 0, c])
//     // rotate([0, b, c])
//         cylinder(h=length, r=0.5, $fn=50);
//     %cube([x,y,z]); // corner of cube should coincide with end of cylinder
// }