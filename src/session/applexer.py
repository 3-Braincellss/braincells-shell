"""
App Lexer
=========

Lexer that detects our defined apps """

from pygments.lexer import RegexLexer
from pygments.token import Keyword, Name, Text
import os

from apps import AppFactory


class AppLexer(RegexLexer):

    apps = "|".join(
        map(lambda x: f"{x}(?![^ ;\|><])", AppFactory().apps.keys()))
    valid_paths = "run.py"

    tokens = {
        "root": [
            (f"{apps}", Keyword.Reserved),
            # (f"{valid_paths}", Name.Namespace),
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
        cls.valid_paths = "|".join(
            map(lambda x: f"^{x}(( )*| +.*)$", out))
