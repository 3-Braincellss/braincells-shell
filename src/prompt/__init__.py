"""
Module Contents
===============

This module is where the user interaction happens.

It contains a ``ShellSession`` submodule that manages user input
and displays results of commands on the screen.

This module uses ``prompt_toolkit`` library that has some nice
user interaction features. For example:

- Command buffer
- Text completions
- Standard shell keybindings. (Emacs keybindings are on by default.)
- Syntax highlighting.

For text completions we used a premade ``PathCompleter`` that was provided
in the prompt_toolkit API. Though we had tweak it a tiny bit to make it work
for our use case.

For syntax highlighting, `prompt_toolkit` uses formatted strings
(Lists of tuples, where each tuple contains the class value and the text to be
displayed.)

We transform user given data into formatted string list using a lark
transformer, which give us a lot of flexibility in comparison to the
default RegexLexer recommended by ``prompt_toolkit``.
"""
from .highlighter import ShellHighlighter
from .completer import ShellPathCompleter
from .shellsession import ShellSession

__all__ = [
    "ShellPathCompleter",
    "ShellSession",
    "ShellHighlighter",
]
