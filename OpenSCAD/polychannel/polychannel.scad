/*--------------------------------------------------------------------------------------
/ General purpose multi-segment channel module: polychannel.
/
/ Given a list of sizes and positions, a series of connected channels is constructed
/ using the hull() operation to connect sequential pairs of cubes with specified
/ size and position as given in the sizes and positions list.
/
/ Rev. 1, 9/28/22, by G. Nordin - Initial version
/ Rev. 1.5, 9/29/22, by Dallin Miner - Modify to select sphere as well as cube shapes
/ Rev. 2, 10/1/22, by G. Nordin - Generalize to include rotation of shapes
--------------------------------------------------------------------------------------*/
$fn=50;

echo();
echo();

// Convert data structure from relative to absolute positions.

// Function to add list of vectors. See add2() at 
// https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Tips_and_Tricks#Add_all_values_in_a_list
function add_list_of_vecs(v) = [for(i=v) 1]*v;
function extract_rel_pos_vectors(p, n, pos_index=2) = [
    for (i=[0:1:n]) p[i][pos_index]
];
function pos_rel_to_abs_oneline(p, line_index) = [
    p[line_index][0],
    p[line_index][1],
    add_list_of_vecs(extract_rel_pos_vectors(p, line_index)),
    p[line_index][3]
];
function convert_params_rel_to_abs(p) = [
    for (i=[0:1:len(p)-1]) pos_rel_to_abs_oneline(p, i)
];

// Fundamental shape creation module for polychannel module.
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

module polychannel_absolute_positions(params, clr="lightblue", center=true, show_only_shapes=false) {
    // echo("len(params)", len(params));
    // echo("params", params);
    if (show_only_shapes) {
        for (i = [0:1:len(params)-1]) {
            // echo("shapes only", i, params[i]);
            color(clr) shape3D(params[i][0], params[i][1], params[i][2], params[i][3], center=center);
        }
    } else {
        for (i = [1:1:len(params)-1]) {
            // echo("with hull", i, params[i-1], params[i]);
            color(clr) hull() {
                shape3D(params[i-1][0], params[i-1][1], params[i-1][2], params[i-1][3], center=center);
                shape3D(params[i][0], params[i][1], params[i][2], params[i][3], center=center);
            };
        };
    }
}

module polychannel(params, relative_positions=false, clr="lightblue", center=true, show_only_shapes=false) {
    if (relative_positions) {
        params_abs = convert_params_rel_to_abs(params);
        polychannel_absolute_positions(params_abs, clr=clr, center=center, show_only_shapes=show_only_shapes);
    } else {
        polychannel_absolute_positions(params, clr=clr, center=center, show_only_shapes=show_only_shapes);
    }
}

// Test data
eps = 0.01;
params_pos_absolute = [
    ["sphr", [eps, 4, 4], [0, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 4, 4], [7, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 1, 1], [7, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 1*sqrt(2), 1], [10, 0, 0], [45, [0, 0, 1]]],
    ["cube", [eps, 1, 1], [10, 5, 0], [90, [0, 0, 1]]],
    ["cube", [3, 2, 3], [10, 10, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 1*sqrt(2), 1], [10, 15, 0], [45, [0, 0, 1]]],
    ["sphr", [eps, 2, 2], [15, 15, 0], [0, [0, 0, 1]]]
];
params_pos_relative = [
    ["sphr", [eps, 4, 4], [0, 0, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 4, 4], [7, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 1, 1], [0, 0, 0], [0, [0, 0, 1]]],
    ["cube", [eps, 1*sqrt(2), 1], [3, 0, 0], [45, [0, 0, 1]]],
    ["cube", [eps, 1, 1], [0, 5, 0], [90, [0, 0, 1]]],
    ["cube", [3, 2, 3], [0, 5, 0], [0, [0, 0, 1]]],
    ["sphr", [eps, 1*sqrt(2), 1], [0, 5, 0], [45, [0, 0, 1]]],
    ["sphr", [eps, 2, 2], [5, 0, 0], [0, [0, 0, 1]]]
];


polychannel(params_pos_relative, relative_positions=true, clr="red", show_only_shapes=true);

translate([0, -25, 0]) polychannel(params_pos_absolute, clr="Salmon");

translate([0, 25, 0]) polychannel(params_pos_relative, relative_positions=true);

