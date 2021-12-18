"""
tail
====
Module representing the tail application
Usage in shell: tail [OPTIONS] [FILE]

Example:
    `tail some-file.py`
"""
from getopt import GetoptError, getopt

from apps.app import App
from common.tools import read_lines_from_file
from exceptions import ContextError


class TailApp(App):
    """
    A class representing the tail shell command

    Args:
        args (:obj:`list`): Contains all the arguments and options of
            the instruction.

    """
    def __init__(self, args):
        super().__init__(args)
        try:
            self.options, self.args = getopt(args, "n:")
        except GetoptError as error:
            raise ContextError("tail", str(error)) from None

    def run(self, inp, out):
        """Executes the tail command on the given arguments.

        Returns the last few lines of a file. The amount is specified by
        the -n option. If this option is not supplied it is defaulted to 10.

        Args:
            inp (:obj:`deque`, *optional*): The input args of the command,
                only used for piping and redirects.
            out (:obj:`deque`): The output deque, used to store
                the result of execution.

        Returns:
            ``deque``: The deque will contain the last few lines of the file.

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
        if len(self.args) > 1:
            for arg in self.args:
                out.append("\n--> " + arg + " <--\n")
                contents = read_lines_from_file(arg, "tail")
                self._run(contents, lines, out)
        else:
            contents = read_lines_from_file(self.args[0], "tail")
            self._run(contents, lines, out)
        return out

    def _run(self, text, lines, out):
        start = 0 if len(text) - lines < 0 else len(text) - lines
        for i in range(start, len(text)):
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
                raise ContextError("tail", str(err)) from err
