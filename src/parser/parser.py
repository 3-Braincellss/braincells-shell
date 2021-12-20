"""
ShellParser
===========

A light weight wrapper for the ``lark`` parser.

All it does is initialises the lark parser with our grammar.
"""

import os

from lark import Lark
from lark.exceptions import UnexpectedInput

from exceptions import ShellSyntaxError

__all__ = [
    "ShellParser",

]


class ShellParser(Lark):
    """
    Parser that is capable of parsing our grammar
    that is defined in the ``grammar.lark``
    """
    def __init__(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "grammar.lark")
        with open(filename, encoding="utf-8") as grammar:
            super().__init__(grammar.read(), start="command")

    def parse(self, text):
        """
        We overrode the default parse method to support
        our exception interface.

        Parameters:
            text(:obj:`str`): Input text to be parsed
        Returns:
            Parse tree of this text.
        Raises:
            ShellSyntaxError: Whenever text cannot be parsed.
        """
        try:
            tree = super().parse(text)
        except UnexpectedInput as err:
            raise ShellSyntaxError(err.get_context(text)) from err
        return tree
