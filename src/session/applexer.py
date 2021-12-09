"""
App Lexer
=========

Lexer that detects our defined apps """

from pygments.lexer import RegexLexer
from pygments.token import Keyword

from apps import AppFactory


class AppLexer(RegexLexer):

    apps = "|".join(map(lambda x: f"^{x}( )*$", AppFactory().apps.keys()))

    tokens = {
        "root": [
            (f'{apps}', Keyword),
        ]
    }
