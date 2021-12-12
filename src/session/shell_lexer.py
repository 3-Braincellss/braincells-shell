"""
ShellLexer
==========
Module representing the lexer used by the shell.
"""
import os

from prompt_toolkit.lexers import Lexer
from prompt_toolkit.document import Document

class ShellLexer(Lexer):
    """Class representing the lexer the shell uses for syntax highlighting.

    Args:
        lexer (:obj:`RegexLexer`): The lexer used to lex the user's
            input
    """

    def lex_document(self, document: Document):
        line = document.lines[0]
        lexed = []
        if line:
            args = line.split(" ")
            for each in args:
                lexed.append(("class:user_host", each))

        return lambda _: lexed
