"""
sort
====
Module representing the sort application
Usage in shell: sort [OPTIONS] [FILE]

Example:
    `sort my-life.txt`

"""

from getopt import getopt, GetoptError

from apps import App
from exceptions import ContextError
from common.tools import read_lines_from_file


class SortApp(App):
    """A class representing the sort shell instruction.

    Args:
        args (:obj:`list`): Contains all the arguments and options of
            the instruction.

    """
    def __init__(self, args):
        super().__init__(args)
        try:
            self.opts, self.args = getopt(args, "r")
        except GetoptError as goe:
            raise ContextError("sort", str(goe)) from None

    def run(self, inp, out):
        """Executes the sort command on the given arguments.

        Sorts the contents of a file/stdin line by line and prints the result
        to stdout. If the -r option is present then the result is reversed.
        If no file is supplied, sorts the text supplied by stdin.

        Args:
            inp (:obj:`deque`, *optional*): The input args of the command, only
                used for piping and redirects.
            out (:obj:`deque`): The output deque, used to store the result
                of execution.

        Returns:
            ``deque``: Contains the file, sorted by line.

        Raises:
            RunError: If the path supplied is not a directory.

        """

        # Reverse order when -r option is provided
        rev = bool(self.opts)

        # if args array is non zero then use file as the input
        if self.args:
            contents = read_lines_from_file(self.args[0], "sort")
            self._run(contents, rev, out)
        elif inp:
            self._run(inp, rev, out)
        else:
            raise ContextError("sort", f"No input arguments supplied")

        return out

    def _run(self, text, rev, out):
        lines = sorted(text, reverse=rev)
        for line in lines:
            out.append(line.rstrip())

    def validate_args(self):
        """Ensures that the correct amount of arguments are supplied.

        Raises:
            ContextError: If too many arguments are given.

        """
        if len(self.args) > 1:
            raise ContextError("sort", "too many arguments")
