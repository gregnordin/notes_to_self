#include <iostream>
#include <string>
#include <math.h>
using namespace std;

// This program print out “Hello World!”
int main()
{
    string message = "Hello World!\n";
    cout << message;
    cout << "\n";
    
    float arr1[3] = {1, 2, 3};
    cout << "arr1:\n";
    cout << arr1 << "\n";
    cout << "\n";
    
    const int num_pump_cycles = 4;
    float arr2[num_pump_cycles] = {0.1, 0.2, 0.3, 0.4};
    cout << "arr2:\n";
    for (int i = 0; i < num_pump_cycles; i++ ){
        cout << i << " " << arr2[i] << "\n";
    }
    cout << "\n";
    
    float arr3[num_pump_cycles] = {};
    cout << "arr3:\n";
    float t0 = 0.01;
    float delta_t = 0.04;
    for (int i = 0; i < num_pump_cycles; i++ ){
        float t = t0 + i * delta_t + 0.023;
        float N_float = (t - t0) / delta_t;
        int N_int = floor(N_float);
        arr3[N_int] = (t - t0) - (N_int * delta_t);
        cout << i << " " << t0 << " " << t << " " << N_float << " " << N_int << " " << arr3[N_int] << "\n";
        t0 = t0 + delta_t;
    }
    
    
    
    return 0;
}