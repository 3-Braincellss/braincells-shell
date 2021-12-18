"""
TO DO: add comments here
"""

from parser import HighlightTransformer, ShellParser

from prompt_toolkit.lexers import Lexer

from exceptions import ShellError

__all__ = [
    "ShellHighlighter",
]


class ShellHighlighter(Lexer):
    """
    ShellHighlighter, Wrapper to ``prompt_toolkit`` Lexer.

    Needed to make our highlighter compatible with ``PromptSession``.
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
        except ShellError:
            return default

        return lambda _: highlighted
