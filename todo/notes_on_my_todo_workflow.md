## Frequently used commands

Add todo and immediately mark it as done.

    > t add "x some todo +someprojecttag"

List what I've done so far today

    > tt

List items on todo list

    > t list

List what I've done the last 2 days

    > t xp 1

List what I did on a specific day and put in Markdown list format

    > dd YYYY-MM-DD

## Using todo.txt and my enhancements

### Copying stuff to the clipboard

- In iTerm2 selecting any text in the terminal automatically copies it to the clipboard
- In iTerm2 `cmd-shift-A` copies the output of the last command to the clipboard
- Piping a command to `pbcopy` redirects the command's output to the clipboard
- The `tee` command can be used to send the output of a command to multiple other commands. For example:
    - Adding `| tee >(pbcopy)` to a command pipes its output to the clipboard and to `stdout`
        - Example: `echo $PATH | tee >(pbcopy)` echoes `PATH` to the clipboard and to the terminal

### Get todo items for a day and reformat to Markdown

The following bash function is defined in my `.bash_profile`. It grabs all of the todo items for the specified day, strips the dates off each line and prepends the line with `- ` to make a nice Markdown list. It then copies the list to the clipboard (Mac OS) as well as prints it to `stdout`.

    # Extract done items for specified date, strip "x date date" and add prefix "- "
    # This puts the output in nice Markdown list format.
    # 2/28/17: Add `| tee >(pbcopy)` to send the output to the clipboard as well as stdout
    # Example usage: 
    #     prompt> dd 2017-01-23
    dd() {
        grep "x $1" /Users/nordin/Dropbox/todo/done.txt | cut -d' ' -f 4- | sed 's/^/- /' | tee >(pbcopy)
    }
