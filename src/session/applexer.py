"""
App Lexer
=========

Lexer that detects our defined apps """

from pygments.lexer import RegexLexer
from pygments.token import Keyword, Name, Text
from prompt_toolkit.lexers import PygmentsLexer
from .shell_lexer import ShellLexer
import os

from apps import AppFactory


class AppLexer(RegexLexer):

    apps = "|".join(
        map(lambda x: f"\\b{x}(?![^ \|;><])",
            AppFactory().apps.keys()))

    tokens = {"root": [(f"{apps}", Keyword.Reserved), (f"\S+", Text)]}

    


def get_lexer():
    """
    Creates and returns a ShellLexer that utilises the AppLexer.
    """
    return ShellLexer(AppLexer)
