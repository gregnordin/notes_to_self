// use <polychannel.scad>;
$fn=50;

module shape3D(shape, size, position, rotation, center=true) {
    a = rotation[0];
    v = rotation[1];
    if(shape=="cube"){
        translate(position) rotate(a=a, v=v) cube(size, center=center);
    }
    else if(shape=="sphr" || shape=="sphere"){
        translate(position) rotate(a=a, v=v)  scale(size) sphere(d=1);
    }
    else {
        assert(false, "invalid shape");
    }
}

eps = 0.01;

params_pos_absolute = [
    ["sphr", [eps, 4, 4], [0, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 4, 4], [7, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 2, 2], [7, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 2*sqrt(2), 2], [10, 0, 0], [45, [0, 0, 1]]],
    ["cube", [eps, 2, 2], [10, 5, 0], [90, [0, 0, 1]]]
];

for (p=params_pos_absolute) {
    echo(p);
    shape3D(p[0], p[1], p[2], p[3]);
}

// shapes = [
//     ["sphr", [eps, 4, 4], [0, 0, 0],
//     ["sphr", [eps, 4, 4], [7, 0, 0],
//     ["cube", [eps, 1, 1]],
//     ["cube", [eps, 1, 1]],
//     ["cube", [5, 5, 5]],
//     ["cube", [2, eps, 2]],
//     ["sphr", [2, 2, 2], 50],
//     ["sphr", [2, 2, 2], 50],
//     ["cube", [1, 1, 1]],
//     ["cube", [1, 1, 1]],
//     ["cube", [1, 1, 1]]
// ];
// positions = [
//     [0, 0, 0],
//     [7, 0, 0],
//     [7, 0, 0],
//     [10, 0, 0],
//     [20, 0, 0],
//     [20, 8, 0],
//     [20, 15, 0],
//     [20, 15, 10],
//     [16, 15, 9.5],
//     [8, 15, 2],
//     [0, 15, 2]
// ];
// relative_positions = [
//     [0, 0, 0],  // All subsequent positions are relative to this position
//     [7, 0, 0],
//     [0, 0, 0],
//     [3, 0, 0],
//     [10, 0, 0],
//     [0, 8, 0],
//     [0, 7, 0],
//     [0, 0, 10],
//     [-4, 0, -0.5],
//     [-8, 0, -7.5],
//     [-8, 0, 0]
// ];