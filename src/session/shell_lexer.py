"""
ShellLexer
==========
Module representing the lexer used by the shell.
"""
import os
from prompt_toolkit.lexers import PygmentsLexer


class ShellLexer(PygmentsLexer):
    """Class representing the lexer the shell uses for syntax highlighting.

    Args:
        lexer (:obj:`RegexLexer`): The lexer used to lex the user's
            input
    """

    def __init__(self, lexer):
        super().__init__(lexer)

    def lex_document(self, document):
        """Lexes the users input. This works very similarly to the usual
        PygmentsLexer's lex_document method, however every text token
        created is converted to a namespace token if the text within the
        token is an existing path.

        Args:
            document (:obj:`Document`): The user's input that is to be
                lexed.
        """
        line_builder = super().lex_document(document)
        line = line_builder(0)
        for index, token_pair in enumerate(line):
            if token_pair[0] == "class:pygments.text" and os.path.exists(token_pair[1]):
                line[index] = ("class:pygments.name.namespace", token_pair[1])
        return line_builder
