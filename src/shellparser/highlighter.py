import os

from lark import Lark
from lark.exceptions import UnexpectedInput, VisitError
from lark.visitors import Transformer
from prompt_toolkit.document import Document
from prompt_toolkit.lexers import Lexer

from apps import AppFactory

__all__ = [
    "HighlightTransformer",
    "ShellHighlighter",
]


class HighlightTransformer(Transformer):
    def command(self, oper):
        """Syntax:

        ```
        command : pipe | seq | call | WHITESPACE
        ```
        
        Parameters:
            oper(:obj:`list`): Either formatted text, or a single formatted token.

        Returns:
            :obj:`list`: Formatted text as a list of tuples.
        """
        if isinstance(oper[0], list):
            return oper[0]
        else:
            return oper

    def seq(self, opers):
        """Syntax:

        ```
        seq : command ";" command
            | command ";"
        ```

        Parameters:
            opers(:obj:`list`): 1 or 2 Formatted text instances.
        Returns:
            :obj:`list`: Formatted text.
        """
        new_args = []
        new_args.extend(opers[0])
        new_args.append(("class:oper", ";"))
        if len(opers) > 1:
            new_args.extend(opers[1])

        return new_args

    def pipe(self, opers):
        """Syntax:
        
        ```
        pipe : call "|" call
             | pipe "|" call

        ```

        Parameters:
            op1(:obj:`list`): Formatted text.

            op1(:obj:`list`): Formatted text.

        Returns:
            :obj:`list`: Formatted text.
        """

        new_args = []
        new_args.extend(opers[0])
        new_args.append(("class:oper", "|"))
        new_args.extend(opers[1])

        return new_args

    def call(self, args):
        """Transforms a list of arguments into formatted text.

        Parameters:
            args(:obj:`list`): A list of formatted text instances or singular tokens.

        Returns:
            :obj:`list`: Formatted text.

        """
        new_args = []
        for arg in args:
            if isinstance(arg, list):
                new_args.extend(arg)

            else:
                new_args.append(arg)

        for i, arg in enumerate(new_args):
            if arg[0] == "class:arg":
                style, app = arg
                style = "class:app"
                app_u = app
                if app[0] == "_":
                    app_u = app[1:]
                    style = "class:unsafe"

                style = style if app_u in AppFactory.apps else "class:err"
                new_args[i] = (style, app)
                break

        return new_args

    def redirection(self, redirect):
        """Just simply forwards a redirection."""

        return redirect[0]

    def l_redirection(self, args):
        """Takes in an optional whitespace and arguments."""

        new_args = []
        new_args.append(("class:redir", "<"))
        paths = args[0]

        if isinstance(args[0], tuple):
            whitespace = args[0]
            new_args.append(whitespace)
            args.pop(0)
            paths = args[0]

        new_args.extend(paths)

        return new_args

    def r_redirection(self, args):
        new_args = []
        new_args.append(("class:redir", ">"))
        paths = args[0]

        if isinstance(args[0], tuple):
            whitespace = args[0]
            new_args.append(whitespace)
            args.pop(0)
            paths = args[0]

        new_args.extend(paths)

        return new_args

    def arguments(self, args):
        new_args = []
        for style, path in args:

            if style == "class:arg":
                style = "class:path" if os.path.exists(path) else "class:arg"
            new_args.append((style, path))

        return new_args

    def quoted(self, args):
        return ("class:quotes", args[0])

    def double_quoted(self, args):
        body = ""
        for arg in args:
            if isinstance(arg, tuple):
                body = body + arg[1]
            else:
                body = body + arg
        return f"\"{body}\""

    def single_quoted(self, args):
        body = ""
        for arg in args:
            if isinstance(arg, tuple):
                body = body + arg[1]
            else:
                body = body + arg
        return f"'{body}'"

    def back_quoted(self, args):
        body = ""
        for arg in args:
            if isinstance(arg, tuple):
                body = body + arg[1]
            else:
                body = body + arg
        return f"`{body}`"

    UNQUOTED = lambda _, x: ("class:arg", str(x))
    DOUBLE_QUOTE_CONTENT = str
    SINGLE_QUOTE_CONTENT = str
    BACKQUOTED = str
    WHITESPACE = lambda _, x: ("class:space", str(x))


class ShellHighlighter(Lexer):
    def __init__(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "grammar.lark")
        with open(filename, encoding="utf-8") as grammar:
            self.parser = Lark(grammar.read(), start="command")

    def lex_document(self, document):
        text = document.lines[0]
        default = lambda _: [("class:err", text)]

        try:
            tree = self.parser.parse(text)

        except UnexpectedInput:
            return default

        try:
            highlighted = HighlightTransformer(
                visit_tokens=True).transform(tree)
        except VisitError as err:
            return default

        return lambda _: highlighted
