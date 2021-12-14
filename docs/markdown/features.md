# Added Features

The features listed in our specification for the development of the shell consisted of adding more applications, unsafe application variants, piping, redirecting, command substitution as well as general refactoring.

This section will highlight the additional features added to the shell that were not requested but we thought would make a more effective shell.

## Clear Command

Just like in traditional shell, the Comp0010 Shell supports the `clear` command, which will remove all text from the terminal.

```
clear
```




## Command Buffer

The Comp0010 has it's own command buffer, meaning that users will be able to use the up and down arrow keys in order to quickly navigate between previously entered commands.

## Syntax Highlighting

Unlike the standard terminal found on most systems, the Comp0010 shell has syntax highlighting. Things that will be highlighted include:

* Applications (`app`, `ls`, etc)
* Operations (`|`, `>`, `;`)
* Valid file paths
* Invalid commands
