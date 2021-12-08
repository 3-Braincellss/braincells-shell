from pygments.lexer import RegexLexer
from pygments.token import Keyword
from apps import AppFactory


class KeyWordLexer(RegexLexer):

    apps = "|".join(AppFactory().apps.keys())

    tokens = {
        "root": [
            (f'{apps}', Keyword),
        ]
    }
