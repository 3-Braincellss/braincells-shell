# pylint: skip-file
# flake8: noqa
"""
grammar.lark
============
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
"""
from .parser import run_parser

__all__ = [
    "run_parser",
]
