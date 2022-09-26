

# Information

## General

[Ten Things I Wish I’d Known About bash](https://zwischenzugs.com/2018/01/06/ten-things-i-wish-id-known-about-bash/)

Jumping back and forth on the command line: [Moving efficiently in the CLI](https://clementc.github.io/blog/2018/01/25/moving_cli/)

## Tutorial

[Shell Scripting for Beginners – How to Write Bash Scripts in Linux](https://www.freecodecamp.org/news/shell-scripting-crash-course-how-to-write-bash-scripts-in-linux/)

```

# Variables:
variable_name=value
# To get the value of the variable, add $ before the variable:
greeting=Hello
name=Tux
echo $greeting $name

# Change file permission to be executable
chmod u+x hello_world.sh

# Run script. Either
./hello_world.sh
# or
bash hello_world.sh

# Numerical expressions can be calculated and stored in a variable using the syntax:
var=$((expression))
```

Logical operators:

OPERATION	|SYNTAX	EXPLANATION |
:----| :---: |
Equality |	num1 -eq num2  |
Greater than equal to	|num1 -ge num2	 | 
Greater than	|num1 -gt num2  |
Less than equal to	|num1 -le num2	  |
Less than	|num1 -lt num2  |
Not Equal to	|num1 -ne num2	 |
AND | -a |
OR | -o |

Example: if a is greater than 40 and b is less than 6:

    if [ $a -gt 40 -a $b -lt 6 ]

```
# Looping with numbers:
for i in {1..5}
do
    echo $i
done

# Looping with strings:
for X in cyan magenta yellow  
do
	echo $X
done

# While loop
i=1
while [[ $i -le 10 ]] ; do
   echo "$i"
  (( i += 1 ))  # Expression that increments counter, i
done

# Reading file line-by-line
LINE=1
while read -r CURRENT_LINE
	do
		echo "$LINE: $CURRENT_LINE"
    ((LINE++))
done < "sample_file.txt"

# How to execute commands with back ticks
# If you need to include the output of a complex command in your script, 
# you can write the statement inside back ticks.
#
# Syntax:
# var= ` commands `
#
# Example: Suppose we want to get the output of a list of mountpoints with tmpfs 
# in their name. We can craft a statement like this: df -h | grep tmpfs.
# To include it in the bash script, we can enclose it in back ticks.
#
var=`df -h | grep tmpfs`
echo $var

# How to get arguments for scripts from the command line
# $@ represents the position of the parameters, starting from one.
for x in $@
do
    echo "Entered arg is $x"
done

```

## Expansions

From [Learning the Shell](http://linuxcommand.org/lc3_lts0080.php), here are some key expansion things to know:

**Parameter expansion**: $USER means replace this with the definition of USER. For a list of parameters: `printenv | less`

Command substitution:

    echo $(ls)    Applications Calibre Library Desktop Docear Documents Downloads Dropbox Dropbox-Deanne Library Movies Music NetBeansProjects Pictures Projects Public PycharmProjects Qt Sites Things VirtualBox VMs Virtualenvs anaconda envs nltk_data

**Double quotes**: enclosing text with double quotes indicates that it should all stay together. However, expansion of $XXX still takes place in the string. To prevent this, use SINGLE QUOTES, which suppresses all expansions!

In double quotes, you can use \ to escape characters. For example `\$` means use a literal `$` character rather than do parameter expansion

**Backslash** - use at end of line just before return character to indicate continuation of command onto next line:

    ls -l \   --reverse \   --human-readable \   --full-time

  
    
---

# Commands

## grep

[grep is a beautiful tool](https://www.eriwen.com/tools/grep-is-a-beautiful-tool/)

    # Case insensitive search for given string in file    
    grep -i "the" demo_file

## find

[How to Search for Files from the Linux Command Line](https://www.freecodecamp.org/news/how-to-search-for-files-from-the-linux-command-line/).

## crontab

### Information


>Crontab (CRON TABle) is a file which contains the schedule of cron entries to be run and at specified times. 
>
>Cron job or cron schedule is a specific set of execution instructions specifing day, time and command to execute. crontab can have multiple execution statments.

- [Crontab – Quick Reference](http://www.adminschoice.com/crontab-quick-reference)
- [crontab.guru](https://crontab.guru) - compose cron jobs online
- Corey Schafer's [Linux/Mac Tutorial: Cron Jobs - How to Schedule Commands with crontab](https://www.youtube.com/watch?v=QZJ1drMQz1A)

### Schema

	# ┌───────────── minute (0 - 59)
    # │ ┌───────────── hour (0 - 23)
    # │ │ ┌───────────── day of month (1 - 31)
    # │ │ │ ┌───────────── month (1 - 12)
    # │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;
    # │ │ │ │ │                                       7 is also Sunday on some systems)
    # │ │ │ │ │
    # │ │ │ │ │
    # * * * * *  command_to_execute


### Commands

	# List contents of crontab
	$ crontab -l
    
    # Delete crontab
	$ crontab -r

    # Edit crontab
	$ crontab -3

	# Set editor to nano
    $ export EDITOR='/usr/bin/nano'
    
    # See what root-level jobs are scheduled
    $ sudo crontab -l
    

## rsync

[Linux/Mac Terminal Tutorial: How To Use The rsync Command - Sync Files Locally and Remotely, Corey Schafer](https://www.youtube.com/watch?v=qE77MbDnljA)  
[Geek to Live: Mirror files across systems with rsync, Gina Trapani](https://lifehacker.com/196122/geek-to-live--mirror-files-across-systems-with-rsync)  

## ln

Create a symlink.  
[Is it possible to navigate to a parent directory in the jupyter tree?](https://stackoverflow.com/questions/38282336/is-it-possible-to-navigate-to-a-parent-directory-in-the-jupyter-tree)  
[How to Create and Use Symbolic Links (aka Symlinks) on a Mac](https://www.howtogeek.com/297721/how-to-create-and-use-symbolic-links-aka-symlinks-on-a-mac/)  

You can specify either a path to a directory or file:

    ln -s /path/to/original /path/to/link
    
The -s here tells the ln command to create a symbolic link. If you want to create a hard link, you’d omit the -s. Most of the time symbolic links are the better choice, so don’t create a hard link unless you have a specific reason for doing so.



## `wc` Word Count

Line, word, and character count for a file.

    wc ~/Dropbox/todo/done.txt