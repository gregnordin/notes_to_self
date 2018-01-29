

# Information

## General

[Ten Things I Wish I’d Known About bash](https://zwischenzugs.com/2018/01/06/ten-things-i-wish-id-known-about-bash/)

Jumping back and forth on the command line: [Moving efficiently in the CLI](https://clementc.github.io/blog/2018/01/25/moving_cli/)

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

## `wc` Word Count

Line, word, and character count for a file.

    wc ~/Dropbox/todo/done.txt