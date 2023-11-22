# Purpose

## Problem

 When I create a device geometry in a module, it would be very useful to set variables that have important coordinates that other code outside the module can use to interface to the geometry defined in the module. However, Openscad has no facility for a geometry module to set global variables outside the module's scope. As an alternative, I can pass a set of parameters to the geometry module to make the geometry and create a series of functions that take the same set of parameters to compute each of the important coordinates. However, this becomes unwieldy for large numbers of parameters.

## Solution

- Pack parameters into a list (array) and pass list as argument to modules and functions.
- Create a series of helper functions to extract specific values from list where the name of each helper function is the name of the relevant parameter.
- In modules/functions, use helper functions to get needed values for computations.

