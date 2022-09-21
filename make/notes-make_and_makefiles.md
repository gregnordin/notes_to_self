

[Makefile cheatsheet](https://bytes.usc.edu/cs104/wiki/makefile/).

[How to make makefile find target in subdirectory makefile](https://stackoverflow.com/questions/17873044/how-to-make-makefile-find-target-in-subdirectory-makefile) - see 2nd answer about how to change directories for POSIX make (as opposed to GNU make).

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

When a target (`all`) has a dependency (`build`) that itself is a target (but `.PHONY`, i.e., not a file) but has no dependencies, it looks like everytime the initial target (`all`) gets run, that dependency (`build`) will also be run.

## `create_directory2`

### Purpose

