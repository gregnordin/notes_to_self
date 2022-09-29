/*--------------------------------------------------------------------------------------
/ General purpose multi-segment channel module: polychannel.
/
/ Given a list of sizes and positions, a series of connected channels is constructed
/ using the hull() operation to connect sequential pairs of cubes with specified
/ size and position as given in the sizes and positions list.
/
/ Rev. 1, 9/28/22, by G. Nordin
--------------------------------------------------------------------------------------*/

module shape3D(size, position, center=true) {
    translate(position) cube(size, center=center);
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

module polychannel_absolute_positions(sizes, positions, clr="lightblue", center=true, show_only_shapes=false) {
    if (show_only_shapes) {
        for (i = [0:len(sizes)-1]) {
            color(clr) shape3D(sizes[i], positions[i]);
        }
    } else {
        for (i = [1:len(sizes)-1]) {
            color(clr) hull() {
                shape3D(sizes[i-1], positions[i-1]);
                shape3D(sizes[i], positions[i]);
            };
        };
    }
}

module polychannel(sizes, positions, relative_positions=false, clr="lightblue", center=true, show_only_shapes=false) {
    assert(len(sizes) == len(positions), "polychannel: sizes and positions arrays must have the same length");
    if (relative_positions) {
        absolute_positions = [for(i = [0:len(sizes)-1]) partial_sum_vectors(positions, i)];
        polychannel_absolute_positions(sizes, absolute_positions, clr=clr, center=center, show_only_shapes=show_only_shapes);
    } else {
        polychannel_absolute_positions(sizes, positions, clr=clr, center=center, show_only_shapes=show_only_shapes);
    }
}


// Example usage - see polychannel_result.png for output

size1 = [1, 1, 1];

sizes = [
    size1,
    [0.1, 1, 1],
    5 * size1,
    [2, 0.1, 2],
    2 * size1,
    2 * size1,
    size1,
    size1,
    size1
];
positions = [
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
    [0, 0, 0],  // All subsequent positions are relative to this position
    [10, 0, 0],
    [10, 0, 0],
    [0, 8, 0],
    [0, 7, 0],
    [0, 0, 10],
    [-4, 0, -0.5],
    [-8, 0, -7.5],
    [-8, 0, 0]
];

polychannel(sizes, positions, clr="red", show_only_shapes=true);

translate([0, -25, 0]) polychannel(sizes, positions, clr="Salmon");

translate([0, 25, 0]) polychannel(sizes, relative_positions, relative_positions=true);

