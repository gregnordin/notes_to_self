default_param_a = 1;
default_param_b = 2;
default_param_c = 3;
default_param_d = [1.5, -1.5, 0.5*default_param_c];
default_param_e = "label";
default_param_f = "red";

default_params = [
    default_param_a,
    default_param_b,
    default_param_c,
    default_param_d,
    default_param_e,
    default_param_f
];

function param_a(p=default_params) = p[0];
function param_b(p=default_params) = p[1];
function param_c(p=default_params) = p[2];
function param_d(p=default_params) = p[3];
function param_e(p=default_params) = p[4];
function param_f(p=default_params) = p[5];

module echo_default_params(p=default_params) {
    echo();
    echo("In echo_default_params");
    echo(p);
}

module echo_params(p=default_params) {
    echo();
    echo("In echo_params");
    echo(p);
    echo("param_a:", param_a(p));
    echo("param_b:", param_b(p));
    echo("param_c:", param_c(p));
    echo("param_d:", param_d(p));
    echo("param_e:", param_e(p));
    echo("param_f:", param_f(p));
}

module module_with_params(p=default_params) {
    echo();
    echo("In module_with_params");
    echo(p);
    echo(param_a(p));
    color(param_f(p)) translate(param_d(p)) cube([param_a(p), param_b(p),param_c(p)], center=true);
    color(param_f(p)) translate(param_d(p) + [0,0,param_c(p)]) scale(0.1) text(param_e(p));
    
}
