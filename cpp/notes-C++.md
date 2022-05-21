[C++ crash course for C programmers by Nicolas P. Rougier](https://github.com/rougier/CPP-Crash-Course)


# 3/14/22

## Objective

Try some C++ syntax things before implementing in OpenFoam `codeFixedValue` boundary conditions.

    $ g++ try_arrays.cpp -o temp; ./temp



# 2/17/22

## Objective

Try out C++ on my new M1 Max MacBook Pro.

### Info

Good C++ syntax refresher: [CodeAcademy: Getting Started with C++](https://www.codecademy.com/learn/c-plus-plus-for-programmers/modules/getting-started-with-c-plus-plus/cheatsheet).

### `220217_try_cpp`

#### `hello_world.cpp`

    #include <iostream>
    #include <string>
    using namespace std;
    
    // This program print out “Hello World!”
    int main()
    {
        string message = "Hello World!\n";
        cout << message;
        return 0;
    }
    
In terminal:

    nordin@ECEns-MacBook-Pro ~/Documents/Projects/notes_to_self/cpp/220217_try_cpp (master)*
    $ which g++
    /usr/bin/g++
    $ g++ hello_world.cpp -o temp
    $ ls
    hello_world.cpp temp
    $ ./temp
    Hello World!
    
Note: I have a problem in VS Code where it points to a different `g++` install from homebrew (in `.vscode/c_cpp_properties.json`) than the system `g++` that is used above by default. When I have more time I need to figure out how to fix this, possibly by changing my terminal PATH to point to the Homebrew version.

    {
        "configurations": [
            {
                "name": "Mac",
                "includePath": [
                    "${workspaceFolder}/**",
                    "/opt/homebrew/Cellar/gcc/11.2.0_3/include/c++/11/tr1"
                ],
                "defines": [],
                "macFrameworkPath": [],
                "compilerPath": "/opt/homebrew/bin/gcc-11",
                "cStandard": "gnu17",
                "cppStandard": "gnu++17",
                "intelliSenseMode": "macos-gcc-arm64"
            }
        ],
        "version": 4
    }
    
