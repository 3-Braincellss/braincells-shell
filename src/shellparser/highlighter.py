import os

from lark import Lark
from lark.visitors import Transformer
from lark.exceptions import UnexpectedInput, VisitError

from apps import AppFactory
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.document import Document


class HighlightTransformer(Transformer):
    def command(self, args):
        return args[0]

    def seq(self, args):
        new_args = []

        if isinstance(args[0], list):
            new_args.extend(args[0])
        else:
            new_args.append(args[0])

        new_args.append(("class:oper", ";"))

        if isinstance(args[1], list):
            new_args.extend(args[1])
        else:
            new_args.append(args[1])

        return new_args

    def pipe(self, args):
        new_args = []
        if isinstance(args[0], list):
            new_args.extend(args[0])
        else:
            new_args.append(args[0])

        new_args.append(("class:oper", "|"))

        if isinstance(args[1], list):
            new_args.extend(args[1])
        else:
            new_args.append(args[1])
        return new_args

    def call(self, args):
        first = True
        new_args = []
        for arg in args:
            if isinstance(arg, list):
                new_args.extend(arg)
            elif arg[0] == "class:arg" and first:
                first = False
                style, app = arg
                style = "class:app" if app in AppFactory.apps else "class:err"
                new_args.append((style, app))
            else:
                new_args.append(arg)

        return new_args

    def redirection(self, args):
        return args[0]

    def l_redirection(self, args):
        new_args = []
        new_args.append(("class:redir", "<"))

        for arg in args:
            if arg[0] == "class:arg":
                style, path = arg
                check = os.getcwd() + f"/{path}"
                style = "class:path" if os.path.exists(check) else "class:err"
                new_args.append((style, path))
            else:
                new_args.append(arg)

        return new_args

    def r_redirection(self, args):
        new_args = []
        new_args.append(("class:redir", ">"))

        for arg in args:
            if arg[0] == "class:arg":
                style, path = arg
                style = "class:path"
                new_args.append((style, path))
            else:
                new_args.append(arg)

        return new_args

    def arguments(self, args):
        return args[0]

    def quoted(self, args):
        return ("class:quotes", args[0])

    def double_quoted(self, args):
        if args:
            return f"\"{args[0]}\""
        else:
            return "\"\""

    def single_quoted(self, args):
        if args:
            return f"'{args[0]}'"
        else:
            return "''"

    def back_quoted(self, args):
        return f"`{args[0]}`"

    UNQUOTED = lambda _, x: ("class:arg", str(x))
    DOUBLE_QUOTE_CONTENT = str
    SINGLE_QUOTE_CONTENT = str
    BACKQUOTED = str
    WHITESPACE = lambda _, x: ("class:space", str(x))


def highlight(text):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "grammar.lark")
    with open(filename, encoding="utf-8") as grammar:
        parser = Lark(grammar.read(), start="command")

    tree = parser.parse(text)

    print(HighlightTransformer(visit_tokens=True).transform(tree))


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
            print(err)
            return default

        return lambda _: highlighted
