use <polychannel.scad>;


// Circular arc functions to calculate absolute and relative positions along an arc
function test_arc_abs_position(radius, angle1, angle2, n) = [
    for (i=[0:1:n]) let (a=angle1 + i*(angle2-angle1)/n, r=radius) [r*cos(a), r*sin(a), 0]
]; 
function test_arc_rel_position(radius, angle1, angle2, n) = [
    for (i=[0:1:n]) let (p=test_arc_abs_position(radius, angle1, angle2, n)) 
    i == 0
    ? p[0] - p[0]
    : p[i] - p[i-1]
];

// Example case
n = 14;
angle1 = 0;
angle2 = 90;
radius = 10;
// Absolute position
test_abs_pos = test_arc_abs_position(radius, angle1, angle2, n);
echo(test_abs_pos);
for (pos=test_abs_pos)
    translate(pos) sphere(0.3, $fn=50);
// Relative position
test_rel_pos = test_arc_rel_position(radius, angle1, angle2, n);
echo(test_rel_pos);
// Double check that getting absolute positions from relative positions is correct
test_abs_pos_from_rel = [for(i=[0:1:n]) partial_sum_vectors(test_rel_pos, i, test_abs_pos[0])];
echo(test_abs_pos_from_rel);
echo();
for (pos=test_abs_pos_from_rel)
    color("red", alpha=0.35) translate(pos) sphere(0.6, $fn=50);


big_list_rel = [
    [0, 0, 0], 
    [5, 0, 0],
    each test_rel_pos,
    [6, 6, 0]
];
echo(big_list_rel);
big_list_abs = [for(i=[0:1:len(big_list_rel)-1]) partial_sum_vectors(big_list_rel, i, [5,0,0])];
echo(big_list_abs);

for (pos=big_list_abs)
    color("blue", alpha=0.35) translate(pos) sphere(0.9, $fn=50);

// echo(big_list_abs[-1]);