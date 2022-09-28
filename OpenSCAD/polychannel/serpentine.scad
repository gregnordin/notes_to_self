use <polychannel.scad>

function serp_rel_x_pos(n, lx) = n == 0
    ? 0
    : lx * ((n+1) % 2);

// function serp_rel_y_pos(n, ly) = ly * (n % 2);

// function sign_serp_rel_y_pos(n) = n

// function partial_sum(v, n, r = 0) = n <= 0 
//         ? r + v[0] 
//         : partial_sum(v, n - 1, r + v[n]); 

module serpentine_channel(
    n = 4,              // Number of serpentine segments
    l = 10,             // Length of serpentine segment
    size = [1, 1, 1],   // Size of channel in x,y,z
    gap = 3             // Gap between serpentine segments
) {
    n_serp_segments = n;
    n_gap_segments = n_serp_segments - 1;
    n_positions = n_serp_segments + n_gap_segments + 1;
    echo("n_serp_segments:", n_serp_segments);
    echo("n_gap_segments:", n_gap_segments);
    echo("n_positions:", n_positions);

    lx = gap + size[0];
    ly = l - size[1];
    echo("lx, ly", lx, ly);
    positions = [for (i= [0: 1: n_positions-1]) 0];
    echo(positions);

    for (i = [0: 1: n_positions-1]) {
        echo(i, serp_rel_x_pos(i, 1), serp_rel_y_pos(i, 1));
    }

    // for (i = [1: n]) {
    //     translate([w/2 + (i-1)*(gap+w), -l/2, 0]) ychan(l, w, h);
    //     s = i % 2 ? 1 : -1;
    //     translate([(i-1)*(gap+w)+w, s/2*(l-w), 0]) xchan(gap, w, h);
    // }
}

size = [1, 1, 1];

serpentine_channel();

function temp(n, ly) = n%2 == 1
    ? ly
    : 0;

function sign(n) = (n+1) % 4 == 0
    ? -1
    : 1;

function serp_rel_y_pos(n, ly) = ly * (n%2) * sign(n);

echo([for (i = [0:1:7]) temp(i, 1)]);
echo([for (i = [0:1:7]) sign(i)]);
echo([for (i = [0:1:7]) temp(i, 2) * sign(i)]);
echo([for (i = [0:1:7]) serp_rel_y_pos(i, 3)]);
