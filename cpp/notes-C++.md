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