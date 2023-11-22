use <lib.scad>

// include <lib.scad>
// The variable "default_params" is available only with "include <lib.scad>" and not with "use <lib.scad>"
// echo(default_params);
// echo(default_param_a);
// Note that the next line will set "default_param" for every instance of its use including in "lib.scad"
// default_param_a = 10;
// echo(default_param_a);

// Use module with default parameters
echo_default_params();
echo_params();
module_with_params();

// Set up new list of parameters and use them
value_param_a = 3;
value_param_b = 4;
value_param_c = 0.5;
value_param_d = [-2.5, 3, 0.5*value_param_c];
value_param_e = "custom";
value_param_f = "blue";

value_params = [
    value_param_a,
    value_param_b,
    value_param_c,
    value_param_d,
    value_param_e,
    value_param_f
];

echo_params(value_params);
module_with_params(value_params);

