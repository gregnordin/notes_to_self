
echo("");
module shape3D(size, position, center=true) {
    translate(position) cube(size, center=center);
}

function partial_sum(v, n, r = 0) = n <= 0 
        ? r + v[0] 
        : partial_sum(v, n - 1, r + v[n]); 

dim = [10, 8, 2, 25, 5]; 
n = len(dim); 
x_pos = [for(i = [0:n-1]) partial_sum(dim, i)]; 
echo(x_pos); // ECHO: [10, 18, 20, 45, 50] 
echo("");
dim2 = [[10, 1], [8, 1], [2, 1], [25, 1], [5, 2]]; 
n2 = len(dim2); 
x_pos2 = [for(i = [0:n2-1]) partial_sum(dim2, i)]; 
echo(x_pos2); // ECHO: [10, 18, 20, 45, 50] 
echo("");



module polylinehull_absolute_positions(sizes, positions, clr="lightblue", center=true) {
    for (i = [1:len(sizes2)-1]) {
        // echo(i, sizes2[i], positions2[i]);
        color(clr) hull() {
            shape3D(sizes2[i-1], positions2[i-1]);
            shape3D(sizes2[i], positions2[i]);
        };
    };

}

// Not finished. Probably don't need if I can create a vector of absolute positions 
// from a vector of relative positions.
module polylinehull_relative_positions(sizes, positions, clr="lightblue", center=true) {
    for (i = [1:len(sizes2)-1]) {
        // echo(i, sizes2[i], positions2[i]);
        color(clr) hull() {
            shape3D(sizes2[i-1], positions2[i-1]);
            shape3D(sizes2[i], positions2[i]);
        };
    };

}


module polylinehull(sizes, positions=[], relative_positions=[], clr="lightblue", center=true) {
    if (len(positions) > 0) {
        polylinehull_absolute_positions(sizes, positions, clr=clr, center=center)
        echo("len(positions) > 0");
    } else {
        echo("len(positions) == 0");
        if (len(relative_positions) > 0) {
            echo("len(relative_positions) > 0");
        } else echo("len(relative_positions) == 0");
    }
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
relative_positions = [
    [0, 0, 0],
    [10, 0, 0],
    [10, 0, 0],
    [0, 8, 0],
    [0, 7, 0],
    [0, 0, 10],
    [-4, 0, -0.5],
    [-8, 0, -7.5],
    [-8, 0, 0]
];


// for (i = [0:len(sizes2)-1]) {
//     // echo(i, sizes2[i], positions2[i]);
//     // color("blue") translate([0, -50, 0]) primitive(sizes[i], positions[i]);
//     color("blue") shape3D(sizes2[i], positions2[i]);
// }

// for (i = [1:len(sizes2)-1]) {
//     // echo(i, sizes2[i], positions2[i]);
//     color("Salmon") translate([0, -25, 0]) hull() {
//         shape3D(sizes2[i-1], positions2[i-1]);
//         shape3D(sizes2[i], positions2[i]);
//     };
// };

translate([0, -25, 0]) polylinehull(sizes2, positions2, clr="Salmon"); //, positions=[], relative_positions=[], center=true)
