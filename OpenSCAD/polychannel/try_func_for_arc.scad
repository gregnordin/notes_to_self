function partial_sum(v, n, r = 0) = n <= 0 
        ? r + v[0] 
        : partial_sum(v, n - 1, r + v[n]); 
function partial_sum_vectors(v, n, r = [0,0,0]) = partial_sum(v, n, r); 



function test_arc_abs_position(radius, arc_deg, n) = [
    for (i=[0:1:n]) let (a=i*arc_deg/n, r=radius) [r*cos(a), r*sin(a), 0]
]; 
function test_arc_rel_position(radius, arc_deg, n) = [ 
    [0, 0, 0],
    for (i=[1:1:n]) let (a_i=i*arc_deg/n, a_im1=(i-1)*arc_deg/n, r=radius) 
        [r*(cos(a_i) - cos(a_im1)), r*(sin(a_i) - sin(a_im1)), 0]
]; 

n = 6;
test_abs_pos = test_arc_abs_position(10, 90, n);
echo(test_abs_pos);
test_rel_pos = test_arc_rel_position(10, 90, n);
echo(test_rel_pos);
// Double check that getting absolute positions from relative positions is correct
test_abs_pos_from_rel = [for(i=[0:1:n]) partial_sum_vectors(test_rel_pos, i, test_abs_pos[0])];
echo(test_abs_pos_from_rel);


