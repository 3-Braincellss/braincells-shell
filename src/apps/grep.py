"""
grep
====
Module representing the grep application
Usage in shell: grep [PATTERN] [FILE]*

Example:
    grep BARRY! bee-movie.txt
"""

import re

from apps import App
from getopt import getopt, GetoptError
from exceptions import ContextError
from common.tools import read_lines_from_file


class GrepApp(App):
    """A class representing the grep shell intstruction

    Args:
        args (:obj:`list`): Contains all the arguments and options
        of the instruction
    """
    def __init__(self, args):
        super().__init__(args)
        try:
            self.option, self.args = getopt(args, "")
        except GetoptError as error:
            raise ContextError("grep", str(error)) from None

    def run(self, inp, out):
        """Executes the grep command on the given arguments.

        Reads the specified files and returns all lines that match a specified
        regex pattern. If no files are given, stdin is grepped instead.

        Args:
            inp (:obj:`deque`, *optional*): The input args of the command,
                only used for piping and redirects.
            out (:obj:`deque`): The output deque, used to store
                the result of execution.

        Returns:
            ``deque``: The deque will contain the lines of the files,
            which match the pattern supplied.

        Raises:
            RunError: If the path specified does not exist/is not a valid file.

        """
        self.pattern = self.args[0]

        if len(self.args) == 1:

            lines = inp if inp else input().split("\n")
            self._run(lines, out)
            return out
        paths = self.args[1:]
        for path in paths:
            if path == "-":  # nani?
                self._run(input().split("\n"), out)
                continue
            contents = read_lines_from_file(path, "grep")
            self._run(contents, out, path, len(paths) > 1)
        return out

    def _run(self, lines, out, path=None, multiple=False):
        for line in lines:
            if re.search(self.pattern, line):
                if multiple:
                    x = f"{path}:{line.rstrip()}"
                else:
                    x = line.rstrip()
                out.append(x)

    def validate_args(self):
        """Ensures that arguments are supplied to the application.

        Raises:
            ContextError: If no arguments are supplied.
        """
        if not self.args:
            raise ContextError("grep", "Usage: grep [PATTERN] [FILE]...")
