/*--------------------------------------------------------------------------------------
/ General purpose multi-segment channel module: polychannel.
/
/ Given a list of sizes and positions, a series of connected channels is constructed
/ using the hull() operation to connect sequential pairs of cubes with specified
/ size and position as given in the sizes and positions list.
/
/ Rev. 1, 9/28/22, by G. Nordin
--------------------------------------------------------------------------------------*/

function select(vector, indices) = [ for (index = indices) vector[index] ];

module shape3D(shape_data, position, center=true) {
    shape = shape_data[0];
    size = shape_data[1];
    if(shape=="cube"){
        translate(position) cube(size, center=center);
    }
    else if(shape=="sphr"){
        fn = shape_data[2];
        translate(position) scale(size) sphere(d=1, $fn=fn);
    }
    else {
        assert(false, "invalid shape");
    }
}

// These functions are helper functions to create a vector of absolute positions from
// a vector of relative positions.
// See https://forum.openscad.org/Calculating-Summarize-Arrays-generate-Array-td29132.html
// for the original code, which cummulatively summed scalars.
function partial_sum(v, n, r = 0) = n <= 0 
        ? r + v[0] 
        : partial_sum(v, n - 1, r + v[n]); 
function partial_sum_vectors(v, n, r = [0,0,0]) = partial_sum(v, n, r); 

// Tests for partial_sum and partial_sum_vectors
dim = [10, 8, 2, 25, 5]; 
n = len(dim); 
x_pos = [for(i = [0:n-1]) partial_sum(dim, i)]; 
echo(x_pos); // ECHO: [10, 18, 20, 45, 50] 
echo("");
dim2 = [[10, 1], [8, 1], [2, 1], [25, 1], [5, 2]]; 
n2 = len(dim2); 
x_pos2 = [for(i = [0:n2-1]) partial_sum_vectors(dim2, i)]; 
echo(x_pos2); // ECHO: [[10, 1], [18, 2], [20, 3], [45, 4], [50, 6]]
echo("");
x_pos3 = [for(i = [0:n2-1]) partial_sum(dim2, i, [0,0,0])]; 
echo(x_pos3); // ECHO: [[10, 1], [18, 2], [20, 3], [45, 4], [50, 6]]
echo("");

module polychannel_absolute_positions(shapes, positions, clr="lightblue", center=true, show_only_shapes=false) {
    if (show_only_shapes) {
        for (i = [0:len(shapes)-1]) {
            color(clr) shape3D(shapes[i], positions[i]);
        }
    } else {
        for (i = [1:len(shapes)-1]) {
            color(clr) hull() {
                shape3D(shapes[i-1], positions[i-1]);
                shape3D(shapes[i], positions[i]);
            };
        };
    }
}

module polychannel(shapes, positions, relative_positions=false, clr="lightblue", center=true, show_only_shapes=false) {
    assert(len(shapes) == len(positions), "polychannel: shapes and positions arrays must have the same length");
    if (relative_positions) {
        absolute_positions = [for(i = [0:len(shapes)-1]) partial_sum_vectors(positions, i)];
        polychannel_absolute_positions(shapes, absolute_positions, clr=clr, center=center, show_only_shapes=show_only_shapes);
    } else {
        polychannel_absolute_positions(shapes, positions, clr=clr, center=center, show_only_shapes=show_only_shapes);
    }
}


// Example usage - see polychannel_result.png for output

eps = 0.01;

shapes = [
    ["sphr", [eps, 4, 4], 50],
    ["sphr", [eps, 4, 4], 50],
    ["cube", [eps, 1, 1]],
    ["cube", [eps, 1, 1]],
    ["cube", [5, 5, 5]],
    ["cube", [2, eps, 2]],
    ["sphr", [2, 2, 2], 50],
    ["sphr", [2, 2, 2], 50],
    ["cube", [1, 1, 1]],
    ["cube", [1, 1, 1]],
    ["cube", [1, 1, 1]]
];
positions = [
    [0, 0, 0],
    [7, 0, 0],
    [7, 0, 0],
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
    [0, 0, 0],  // All subsequent positions are relative to this position
    [7, 0, 0],
    [0, 0, 0],
    [3, 0, 0],
    [10, 0, 0],
    [0, 8, 0],
    [0, 7, 0],
    [0, 0, 10],
    [-4, 0, -0.5],
    [-8, 0, -7.5],
    [-8, 0, 0]
];

polychannel(shapes, positions, clr="red", show_only_shapes=true);

translate([0, -25, 0]) polychannel(shapes, positions, clr="Salmon");

translate([0, 25, 0]) polychannel(shapes, relative_positions, relative_positions=true);

