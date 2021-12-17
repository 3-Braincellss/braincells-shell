"""
Highlight Transformer
=====================

Converts the **AST** into a formatted text instance.

Any mention of **formatted text** in this document means:

A list of tuples of the following format:

.. code:: python

    [("style_str1", "text_1"), ("style_str2", "text_2"), ...]


Possible style classes are
- ``oper``: operation style (``|``, ``;``)

- ``arg``: Arguments that weren't affected by context changes.

- ``app``: Apps that are recognised by AppFactory will be styled accordingly.

- ``path``: If an argument is an existing path.

- ``err``: Apps that are not recognised by appfactory or general error style.

- ``unsafe``: Unsafe apps that are recognised by AppFactory

- ``redir``: redirections (``<``, ``>``)

- ``quotes``: Any quotes.

- ``space``: whitespaces.
"""

import os

from lark.exceptions import VisitError
from lark.visitors import Transformer

from apps import AppFactory
from exceptions import ShellSyntaxError

__all__ = [
    "HighlightTransformer",
]


class HighlightTransformer(Transformer):
    def __init__(self):
        super().__init__(visit_tokens=True)

    def transform(self, tree):
        """
        Overriding transform method to support
        our exceptions.

        Parameters:
            tree: Abstract Syntax tree produced by lark.
        Returns:
            :obj:`list`: Formatted text.


        """
        try:
            form_text = super().transform(tree)
        except VisitError:
            raise ShellSyntaxError("Cannot tranform")
        return form_text

    def command(self, oper):
        """Transforms a command nonterminal to formatted text.

        Parameters:
            oper(:obj:`list`): Either formatted text, or a single
            formatted token.

        Returns:
            :obj:`list`: Formatted text.
        """
        if isinstance(oper[0], list):
            return oper[0]
        else:
            return oper

    def seq(self, opers):
        """
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
        """
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
            args(:obj:`list`): A list of formatted text instances or
            singular tokens.

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
        """Takes in an optional whitespace and arguments.
        
        Parameters:
            args(:obj:`list`): First value of args can either
                be a tuple for a whitespace or the could be no
                whitespace at all and it's just arguments formatted
                text
        """

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
                print(arg)
                body = body + arg[1]
            else:
                body = body + arg
        return f"`{body}`"

    def UNQUOTED(_, x):
        return ("class:arg", str(x))

    DOUBLE_QUOTE_CONTENT = str
    SINGLE_QUOTE_CONTENT = str
    BACKQUOTED = str

    def WHITESPACE(_, x):
        return ("class:space", str(x))
