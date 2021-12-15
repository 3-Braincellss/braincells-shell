"""
TO DO: add comments here
"""

from prompt_toolkit.lexers import Lexer

from parser import ShellParser, HighlightTransformer
from exceptions import ShellError

__all__ = [
    "ShellHighlighter",
]


class ShellHighlighter(Lexer):
    """

    """
    def __init__(self):
        self.parser = ShellParser()
        self.transformer = HighlightTransformer()

    def lex_document(self, document):
        text = document.lines[0]

        def default(_):
            return [("class:err", text)]

        try:
            tree = self.parser.parse(text)
        except ShellError:
            return default

        try:
            highlighted = self.transformer.transform(tree)
        except ShellError as err:
            return default

        return lambda _: highlighted
