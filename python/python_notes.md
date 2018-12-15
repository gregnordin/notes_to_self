
## Is a particular package/module installed?

[How do I check whether a module is installed or not in Python?](https://askubuntu.com/questions/588390/how-do-i-check-whether-a-module-is-installed-or-not-in-python)


## Some key constructs in python

[What Does It Take To Be An Expert At Python? by James Powell](https://www.youtube.com/watch?v=7lmCu8wz8ro)

### Metaclass

- Hook into class creation process
- Can make sure subclasses implement certain methods
- Is a way for library code writer to ensure that user code writer does certain things

### Decorator

- Wrap behavior around a function, can force behavior before and after a function
- Examples: timing, authentication, logging

### Generator

- Can run code sequentially rather than eagerly
- Run some library code, then some user code, then some library code, then some user code, etc.
- Enforce sequence of actions

### Context Manager

- Run start up and tear down actions even if some error occurs during code execution after start up and before tear down