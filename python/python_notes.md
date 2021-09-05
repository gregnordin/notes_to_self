
## How to install your own local package

See [Lessons Learned from two years as a Data Scientist](https://dawndrain.github.io/braindrain/two_years.html).

>You can see where python looks for projects that you're trying to import by doing:

    import sys
    print(sys.path)

>.... For the longest time I did not know how to import my own code across projects! I had this one `dawn_utils.py` file which I must have copy-pasted like five times. The solution is to add your project's folder to one of the directories on the `PYTHONPATH` (what `sys.path` shows). In practice the way to do this is to go to your project's root folder (which should contain a subfolder like `project_src` that has your project's actual code) and create a `setup.py` file like:

    from setuptools import setup
    
    setup(
        name='my-project',
        version='0.0',
        packages=['project_src',],
    		install_requires=[],
        long_description=open('readme.txt').read(),
    )

> You can then do `pip install .` or `pip install -e .` (which will make it so that you can edit your project and have the changes propagate without having to reinstall it). You should now be able to do `import project_src` and go to town.


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