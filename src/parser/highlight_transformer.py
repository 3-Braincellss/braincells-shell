"""
Highlight Transformer
=====================

Converts the **Lark AST** into a formatted text instance.

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
    """Custom transformer inheriting lark.visitore.Transformer

    Takes in the Lark AST and transforms it into Formatted Text.
    """
    def __init__(self):
        super().__init__(visit_tokens=True)

    def transform(self, tree):
        """
        Overriding transform method to support
        our exceptions.

        Parameters:
            tree: Abstract Syntax tree produced by lark.
        Returns:
            :obj:`list`: Formatted Text.
        """
        try:
            form_text = super().transform(tree)
        except VisitError as err:
            raise ShellSyntaxError("Cannot tranform") from err
        return form_text

    def command(self, oper):
        """Transforms a command nonterminal to formatted text.

        Parameters:
            oper(:obj:`list`): [Formatted Text]

        Returns:
            :obj:`list`: Formatted text.
        """
        return oper[0]

    def seq(self, opers):
        """Transforms a sequence non-terminal to formatted text.

        Parameters:
            opers(:obj:`list`): 1 or 2 Formatted Text instances.
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
        """Transforms a pipe non-terminal to formatted text.

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
        """Transforms a call non-terminal into Formatted Text.
        Adjusts style for existing and unsafe apps.

        Parameters:
            args(:obj:`list`): A list of formatted text instances.

        Returns:
            :obj:`list`: Formatted text.

        """
        new_args = []
        for arg in args:
            new_args.extend(arg)

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
        """Just simply forwards a redirection.

        Parameters:
            args(:obj:`list`): [Formatted Text]
        Returns:
            :obj:`list`: Formatted Text
        """
        return redirect[0]

    def l_redirection(self, args):
        """Combines left redirection children into
        Formatted Text.

        Parameters:
            args(:obj:`list`): [Formatted Text]
        Returns:
            :obj:`list`: Formatted Text
        """
        return self._redir("<", args)

    def r_redirection(self, args):
        """Combines right redirection children into
        Formatted Text.

        Parameters:
            args(:obj:`list`): [Formatted Text]

        Returns:
            :obj:`list`: Formatted Text
        """
        return self._redir(">", args)

    def arguments(self, args):
        """Adjusts style of the argument if its a path
        and returns a formatted text.

        Parameters:
            args(:obj:`list`): Formatted Text

        Returns:
            :obj:`list`: Formatted Text
        """
        new_args = []
        for style, path in args:
            if style == "class:arg":
                style = "class:path" if os.path.exists(path) else "class:arg"
            new_args.append((style, path))

        return new_args

    def quoted(self, args):
        """Converts quote string into tuple of
        Formatted Text.

        Parameters:
            args(:obj:`list`): [:obj:`str`]

        Returns:
            :obj:`tuple`: Formated Tuple
        """
        return ("class:quotes", args[0])

    def double_quoted(self, args):
        """Adds quoting to double quote content.

        Parameters:
            args(:obj:`list`): [:obj:`str`]

        Returns:
            :obj:`str`: string with double quotes
        """
        return self._quoting('"', args)

    def single_quoted(self, args):
        """Adds quoting to single quote content.

        Parameters:
            args(:obj:`list`): [:obj:`str`]

        Returns:
            :obj:`str`: string with single quotes
        """
        return self._quoting("'", args)

    def back_quoted(self, args):
        """Adds quoting to back quote content.

        Parameters:
            args(:obj:`list`): [:obj:`str`]

        Returns:
            :obj:`str`: string with back quotes
        """
        return self._quoting("`", args)

    DOUBLE_QUOTE_CONTENT = str
    SINGLE_QUOTE_CONTENT = str
    BACKQUOTED = str

    def UNQUOTED(self, x):  # pylint: disable=C0103
        """Converts UNQUOTED lark token into Formatted Tuple.

        Parameters:
            x: UNQUOTED Lark Token.
        Returns:
            :obj:`tuple`: Formatted Tuple.
        """
        return ("class:arg", str(x))

    def WHITESPACE(self, x):  # pylint: disable=C0103
        """Converts WHITESPACE lark token into Formatted Tuple.

        Parameters:
            x: WHITESPACE Lark Token.
        Returns:
            :obj:`list`: Formatted Text.

        """
        return [("class:space", str(x))]

    @staticmethod
    def _quoting(quote, args):
        text = ""
        if args:
            text = "".join(args)
        return f"{quote}{text}{quote}"

    @staticmethod
    def _redir(direction, args):
        new_args = []
        new_args.append(("class:redir", direction))
        for each in args:
            new_args.extend(each)

        return new_args
