# `make` version

## Original

Original version of `make`:

```
$ make --version
GNU Make 3.81
Copyright (C) 2006  Free Software Foundation, Inc.
```

This is too old. 

## brew install latest GNU make

    brew install make
    
Now add the following to the top of my `.bash_profile`:

    # GNU "make" has been installed as "gmake".
    # If you need to use it as "make", you can add a "gnubin" directory
    # to your PATH from your bashrc like:
    PATH="/opt/homebrew/opt/make/libexec/gnubin:$PATH"
    # Now Homebrew GNU make is my default make

Check that everything is in order (after running `$ source ~/bash_profile`):

    $ which make
    /opt/homebrew/opt/make/libexec/gnubin/make
    (base)
    nordin@ECEns-MacBook-Pro-4 ~/Documents/Projects/notes_to_self (master)*
    $ make --version
    GNU Make 4.3
    Built for arm-apple-darwin21.1.0
    Copyright (C) 1988-2020 Free Software Foundation, Inc.


# Information

Basics:

```
target1: dependency1 dependency2 ...
	command1  # Each line is executed as a subshell, & therefore won't affect subsequent lines (so don't do cd and expect it to stick)
	command2
	...
```

[Makefile cheatsheet](https://bytes.usc.edu/cs104/wiki/makefile/).

[How to make makefile find target in subdirectory makefile](https://stackoverflow.com/questions/17873044/how-to-make-makefile-find-target-in-subdirectory-makefile) - see 2nd answer about how to change directories for POSIX make (as opposed to GNU make).

[How to write exactly bash scripts into Makefiles?](https://unix.stackexchange.com/questions/270778/how-to-write-exactly-bash-scripts-into-makefiles)

>If you really want to “write exactly bash scripts into Makefiles” then you'll need to do it a bit indirectly. **If you just paste the script after the target line, then you'll run into two problems that just cannot be bypassed: the command lines need to be indented with a tab, and dollar signs need to be escaped.**

>If you use GNU make (as opposed to BSD make, Solaris make, etc.), then you can define your script as a variable using the multi-line definition syntax, and then use the value function to use the raw value of the variable, bypassing expansion.

>In addition, as explained by skwllsp, **you need to tell make to execute the command list for each target as a single shell script rather than line by line, which you can do in GNU make by defining a .ONESHELL target.**

>       define my_important_task =
        # script goes here
        endef
    
>       my-important-task: ; $(value my_important_task)
    
>       .ONESHELL: 

Here is some additional info from [Chnossos answer](https://stackoverflow.com/questions/1789594/how-do-i-write-the-cd-command-in-a-makefile):

>New special target: .ONESHELL instructs make to invoke a single instance of the shell and provide it with the entire recipe, regardless of how many lines it contains.


[How do I write the 'cd' command in a makefile?](https://stackoverflow.com/questions/1789594/how-do-i-write-the-cd-command-in-a-makefile)

>It is actually executing the command, changing the directory to some_directory, however, this is performed in a sub-process shell, and affects neither make nor the shell you're working from.

>If you're looking to perform more tasks within some_directory, you need to add a && and append the other commands as well. Note that you cannot use new lines as they are interpreted by make as the end of the rule, so any new lines you use for clarity need to be escaped by a backslash.

[Makefile for Projects with Subdirectories](https://yuukidach.github.io/2019/08/05/makefile-learning/) - See Practice 3 for interesting way of handling `.PHONY`:

    PHONY := $(TARGET)
    ...
    PHONY += clean
    clean:
        ...
    ...
    PHONY += echoes
    echoes:
        ...
    ...
    .PHONY = $(PHONY)

Or, one can just put `.PHONY: <something>` right before `<something>` definition.




---

# 9/20/22

## `create_directory`

### Purpose

What happens when you have the following?

```
all: build
build:
    mkdir -p $(BUILD)
clean:
    rm -rf $(BUILD)
.PHONY build clean
```

### Results

Run 1st time: runs `build` and creates the directory `build`.  
Run 2nd time: runs `build` (`mkdir -p $(BUILD)`) again, but it doesn't do anything because the directory already exists.

### Conclusion

When a target (`all`) has a dependency (`build`) that itself is a target (but `.PHONY`, i.e., not a file) but has no dependencies, it looks like every time the initial target (`all`) gets run, that dependency (`build`) will also be run.

## `create_directory2`

### Purpose

