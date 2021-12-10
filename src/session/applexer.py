"""
App Lexer
=========

Lexer that detects our defined apps """

from pygments.lexer import RegexLexer
from pygments.token import Keyword, Name, Text
from prompt_toolkit.lexers import PygmentsLexer
import os

from apps import AppFactory


class AppLexer(RegexLexer):

    apps = "|".join(
        map(lambda x: f"{x}(?![^ ;\|><])", AppFactory().apps.keys()))

    tokens = {
        "root": [
            (f"{apps}", Keyword.Reserved),
            ("run.py", Name.Namespace),
            (f"(^ )+", Text)
        ]
    }

    @classmethod
    def update_dirs(cls):
        out = []
        for root, dirs, files in os.walk('.'):
            for dir in dirs:
                out.append(os.path.join(root, dir)[2:])
            for file in files:
                out.append(os.path.join(root, file)[2:])
        regex = "|".join(
            map(lambda x: f"{x}(?![^ ])", out))
        cls.tokens["root"][1] = (f"{regex}", Name.Namespace)


def get_lexer():
    return PygmentsLexer(AppLexer)
