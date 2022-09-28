
echo("");
module shape3D(size, position, center=true) {
    translate(position) cube(size, center=center);
}
module primitive(size, position, rotation, center=true) {
    translate(position) rotate(a=rotation) cube(size, center=center);
}

sizes = [
    [1, 1, 1],
    [5, 5, 5],
    [2, 2, 2],
    [2, 2, 2],
    [1, 1, 1]
];
positions = [
    [0, 0, 0],
    [20, 0, 0],
    [20, 15, 0],
    [20, 15, 10],
    [3, 3, 3]
];


// for (i = [1:len(sizes)-1]) {
//     echo(i, sizes[i], positions[i]);
//     color("Salmon") translate([0, -25, 0]) hull() {
//         shape3D(sizes[i-1], positions[i-1]);
//         shape3D(sizes[i], positions[i]);
//     };
// };

size1 = [1, 1, 1];

sizes2 = [
    size1,
    [0.1, 1, 1],
    5*size1,
    [2, 0.1, 2],
    2*size1,
    2*size1,
    size1,
    size1,
    size1
];
positions2 = [
    [0, 0, 0],
    [10, 0, 0],
    [20, 0, 0],
    [20, 8, 0],
    [20, 15, 0],
    [20, 15, 10],
    [16, 15, 9.5],
    [8, 15, 2],
    [0, 15, 2]
];
rotations = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
];
// rotations = [
//     [0, 0, 0],
//     [0, 0, 0],
//     [0, 0, 0],
//     [0, 0, 0],
//     [0, 0, 0],
//     [0, 0, 0],
//     [0, 0, 0]
// ];


for (i = [0:len(sizes2)-1]) {
    echo(i, sizes2[i], positions2[i]);
    // color("blue") translate([0, -50, 0]) primitive(sizes[i], positions[i]);
    color("blue") shape3D(sizes2[i], positions2[i]);
}

for (i = [1:len(sizes2)-1]) {
    echo(i, sizes2[i], positions2[i]);
    color("Salmon") translate([0, -25, 0]) hull() {
        shape3D(sizes2[i-1], positions2[i-1]);
        shape3D(sizes2[i], positions2[i]);
    };
};
