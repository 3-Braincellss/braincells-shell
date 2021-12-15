# pylint: skip-file
# flake8: noqa
"""
Module Contents
===============

We use ``lark`` to produce an AST from the following grammar:

grammar.lark
------------
.. code-block:: text

    %import common.LETTER

    command : pipe | seq | call | WHITESPACE
    seq     : command ";" command
    pipe    : call "|" call
            | pipe "|" call
    call        : WHITESPACE? (redirection WHITESPACE)* arguments (WHITESPACE arguments)* (WHITESPACE redirection)* WHITESPACE?

    arguments     : (quoted | UNQUOTED)+

    redirection : l_redirection | r_redirection

    l_redirection : "<" WHITESPACE? arguments
    r_redirection : ">" WHITESPACE? arguments

    quoted        : single_quoted | double_quoted | back_quoted
    double_quoted : "\"" (back_quoted | DOUBLE_QUOTE_CONTENT)* "\""
    back_quoted    : "`" BACKQUOTED "`"
    single_quoted : "'" SINGLE_QUOTE_CONTENT* "'"

    BACKQUOTED           : /[^\\n`]+/
    DOUBLE_QUOTE_CONTENT : /[^\\n"`]+/
    SINGLE_QUOTE_CONTENT : /[^\\n']+/
    UNQUOTED             : /[^\\s"'`\\n;|<>]+/
    WHITESPACE           : /[\\s]+/


We then transform the resultant **AST** in 2 ways:

1. Into a command object that our shell will execute
2. Into a formatted text list that is then used for syntax highlighting.

Henceforth, we have 2 modules that do exactly that:


"""
from .highlight_transformer import HighlightTransformer, ShellHighlighter
from .command_transformer import CommandTransformer
from .parser import ShellParser

__all__ = [
    "HighlightTransformer",
    "CommandTransformer",
    "ShellParser",
]
