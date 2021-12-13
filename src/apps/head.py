"""
head
====
Module representing the head application
Usage in shell: head [OPTIONS] [FILE]

Example:
    `head -n 12 text.txt`
"""
from getopt import GetoptError, getopt

from apps.app import App
from common.tools import read_lines_from_file
from exceptions import ContextError


class HeadApp(App):
    """A class representing the head shell application

    Args:
        args (:obj:`list`): Contains all the arguments and options
            of the instruction
    """

    def __init__(self, args):
        super().__init__(args)
        try:
            self.options, self.args = getopt(args, "n:")
        except GetoptError as err:
            raise ContextError("head", str(err)) from err

    def run(self, inp, out):
        """Executes the head command on the given arguments.

        Returns the first few lines of a file. The amount is specified by
        the -n option. If this option is not supplied it is defaulted to 10.

        Args:
            inp (:obj:`deque`, *optional*): The input args of the command,
                only used for piping and redirects.
            out (:obj:`deque`): The output deque, used to store
                the result of execution.

        Returns:
            ``deque``: The deque will contain the first few lines of the file.

        Raises:
            RunError: If any of the paths specified do not exist.
        """
        if self.options:
            lines = int(self.options[0][1])
        else:
            lines = 10
        if inp:
            self._run(inp, lines, out)
            return out
        if not self.args:
            for _ in range(lines):
                out.append(input())
            return out
        if len(self.args) > 1:
            for arg in self.args:
                out.append("\n--> " + arg + " <--\n")
                contents = read_lines_from_file(arg, "head")
                self._run(contents, lines, out)
        else:
            contents = read_lines_from_file(self.args[0], "head")
            self._run(contents, lines, out)
        return out

    def _run(self, text, lines, out):
        for i in range(0, lines):
            if i == len(text):
                break
            out.append(text[i].strip("\n"))

    def validate_args(self):
        """Ensures the options are valid.

        Raises:
            ContextError:
        """
        if self.options:
            try:
                int(self.options[0][1])
            except ValueError as err:
                raise ContextError("head", str(err)) from err
