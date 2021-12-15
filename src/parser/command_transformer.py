"""
Command Transformer
===================

Module which handles parsing and transforming the parse tree
"""
import os

from lark import Lark
from lark.exceptions import UnexpectedInput, VisitError
from lark.visitors import Transformer

from exceptions import ShellError, ShellSyntaxError
from commands import CommandFactory

__all__ = [
    "CommandTransformer",
]


class CommandTransformer(Transformer):
    """Custom transformer inheriting lark.visitors.Transformer

    Takes in the AST and transforms it into a single ``Operation`` object with
    potentially multiple ``Operation`` and ``App`` objects nested in that object.

    Each method corresponds to how each non-terminal in the AST is transformed.

    Attributes define how each terminal is transformed.

    """
    def __init__(self):
        super().__init__(visit_tokens=True)

    def transform(self, tree):
        """ Overriding transform method
        to support our exception interface

        Parameters:
            tree: Abstract syntax tree
        Returns:
            Operation: operaion object.
        Raises:
            ShellSyntaxError: whenever tranforming cannot happen
                for whatever reason
            
            ShellError: propagated errors from the subshell that
                is run in the backquotes.
        """

        try:
            oper = super().transform(tree)
        except VisitError as err:
            # Visit error doesn't properly propagate
            # underlying errors, so we have to do this trick
            # to bring shell errors higher.
            if isinstance(err.__context__, ShellError):
                raise err.__context__
            raise ShellSyntaxError("cannot transform")
        return oper

    def command(self, args):
        """Starting point of grammar

        Parameters:
            args (list): List of possible `None` and a single operation
                object to be executed

        Returns:
            Operation: Operation object to be executed

        """

        # Removes `None`
        returnargs = [x for x in args if x is not None]
        return returnargs[0]

    def seq(self, args):
        """Proccesses data for sequence operation object and creates the object

        Parameters:
            args (list): List of two operation objects

        Returns:
            Operation: A sequence operation object

        """
        data = {"op1": args[0], "op2": args[1]}
        seq = CommandFactory.get_command("seq", data)

        return seq

    def pipe(self, args):
        """Proccesses data for pipe operation object and creates the object

        Parameters:
            args (list): List of two operation objects

        Returns:
            Operation: A pipe operation object

        """
        data = {"op1": args[0], "op2": args[1]}
        pipe = CommandFactory.get_command("pipe", data)

        return pipe

    def call(self, args):
        """Processes data for the call operation and created the call
        operation object

        Parameters:
            args (list): List of strings possible `None` and possible `tuple`

        Returns:
            Operation: A call operation object.
        """

        # Removes `None` and `tuple`

        returnargs = [
            x for x in args if x is not None and not isinstance(x, tuple)
        ]
        right_string = [
            x for x in args
            if x is not None and isinstance(x, tuple) and x[0] == "right_red"
        ]
        left_string = [
            x for x in args
            if x is not None and isinstance(x, tuple) and x[0] == "left_red"
        ]

        if len(right_string) != 0:
            right_red = right_string[0][1]
        else:
            right_red = None

        if len(left_string) != 0:
            left_red = left_string[0][1]
        else:
            left_red = None

        data = {
            "app": returnargs[0],
            "args": returnargs[1:],
            "left_red": left_red,
            "right_red": right_red,
        }
        call = CommandFactory.get_command("call", data)

        return call

    def redirection(self, args):
        """Passes redirection type and path higher up the parse tree

        Parameters:
            args (list): List of single tuple

        Returns:
            tuple: (str: redirection type, str: path)

        """
        return args[0]

    def l_redirection(self, args):
        """Handles input redirection

        Parameters:
            args (list): List of a possible `None` and file input string

        Returns:
            tuple: ("left_red", str: path)

        """

        # Removes whitespaces (which are `None`)
        returnargs = [x for x in args if x is not None]
        return ("left_red", returnargs[0])

    def r_redirection(self, args):
        """Handles output redirection

        Parameters:
            args (list): List of a possible `None` and file output string

        Returns:
            tuple: ("right_red", str: path)

        """

        # Removes whitespaces (which are `None`)
        returnargs = [x for x in args if x is not None]
        return ("right_red", returnargs[0])

    def arguments(self, args):
        """Passes a string that was quoted or unquoted higher up the parse tree

        Parameters:
            args (list): A list of a single string

        Returns:
            str: the string that was in the list
        """
        return "".join(args)

    def quoted(self, args):
        """Passes on the string that was inside any type of quote higher up
        the parse tree

        Parameters:
            args (list): A list of a single string of the text inside the
                quotes

        Returns:
            str: the string that was in the quotes
        """
        return args[0]

    def double_quoted(self, args):
        """Returns the string of what was in the double quotes

        Parameters:
            args (list): A list of a strings of the text inside the double
                quotes and possibly output from backquote calls

        Returns:
            str: the string that was in the double quotes
        """
        return "".join(args)

    def single_quoted(self, args):
        """Returns the string of what was in the single quotes

        Parameters:
            args (list): A list of a single string of the text inside the
                single quotes

        Returns:
            str: the string that was in the single quotes
        """
        return args[0]

    def back_quoted(self, args):
        """Created a Shell instance and executes the string that
        was inside the back quotes

        Parameters:
            args (list): A list of a single string of the text inside the
                back quotes

        Returns:
            str: the output string from the command that was run
        """

        # Putting this at top level causes circular import
        from shell import Shell  # pylint: disable=import-outside-toplevel
        sh = Shell()
        string = " ".join(sh.execute(args[0]).split("\n"))
        return string

    def WHITESPACE(self, tok):  # pylint: disable=invalid-name
        """Replaces any amount of whitespace with a None

        Parameters:
            tok (str): the whitespace string
        """
        pass

    UNQUOTED = str
    DOUBLE_QUOTE_CONTENT = str
    SINGLE_QUOTE_CONTENT = str
    BACKQUOTED = str
