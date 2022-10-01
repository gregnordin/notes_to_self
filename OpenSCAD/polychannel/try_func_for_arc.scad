function partial_sum(v, n, r = 0) = n <= 0 
        ? r + v[0] 
        : partial_sum(v, n - 1, r + v[n]); 
function partial_sum_vectors(v, n, r = [0,0,0]) = partial_sum(v, n, r); 



// function test_arc_abs_position(radius, arc_deg, n) = [
//     for (i=[0:1:n]) let (a=i*arc_deg/n, r=radius) [r*cos(a), r*sin(a), 0]
// ]; 
// function test_arc_rel_position(radius, arc_deg, n) = [ 
//     [0, 0, 0],
//     for (i=[1:1:n]) let (a_i=i*arc_deg/n, a_im1=(i-1)*arc_deg/n, r=radius) 
//         [r*(cos(a_i) - cos(a_im1)), r*(sin(a_i) - sin(a_im1)), 0]
// ]; 

// n = 6;
// test_abs_pos = test_arc_abs_position(10, 90, n);
// echo(test_abs_pos);
// test_rel_pos = test_arc_rel_position(10, 90, n);
// echo(test_rel_pos);
// // Double check that getting absolute positions from relative positions is correct
// test_abs_pos_from_rel = [for(i=[0:1:n]) partial_sum_vectors(test_rel_pos, i, test_abs_pos[0])];
// echo(test_abs_pos_from_rel);

function test_arc_abs_position(radius, angle1, angle2, n) = [
    for (i=[0:1:n]) let (a=angle1 + i*(angle2-angle1)/n, r=radius) [r*cos(a), r*sin(a), 0]
]; 
function test_arc_rel_position(radius, angle1, angle2, n) = [
    for (i=[0:1:n]) let (p=test_arc_abs_position(radius, angle1, angle2, n)) 
    i == 0
    ? p[0] - p[0]
    : p[i] - p[i-1]
];
// function test_arc_rel_position(radius, angle1, angle2, n) = [ 
//     [0, 0, 0],
//     for (i=[1:1:n]) let (a_i=angle1 + i*(angle2-angle1)/n, a_im1=angle1 + (i-1)*(angle2-angle1)/n, r=radius) 
//         [r*(cos(a_i) - cos(a_im1)), r*(sin(a_i) - sin(a_im1)), 0]
// ]; 

n = 14;
angle1 = 0;
angle2 = 90;
radius = 10;
test_abs_pos = test_arc_abs_position(radius, angle1, angle2, n);
echo(test_abs_pos);

for (pos=test_abs_pos)
    translate(pos) sphere(0.3, $fn=50);

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
big_list_abs = [for(i=[0:1:len(big_list_rel)-1]) partial_sum_vectors(big_list_rel, i, [0,0,0])];
echo(big_list_abs);

for (pos=big_list_abs)
    color("blue", alpha=0.75) translate(pos) sphere(0.6, $fn=50);
