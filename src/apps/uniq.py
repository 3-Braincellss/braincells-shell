"""
uniq
====
Module representing the uniq application
Usage in shell: uniq [OPTIONS] [FILE]..

Example:
    `uniq -i test-ans.txt`

"""
from getopt import GetoptError, getopt

from apps import App
from common.tools import read_lines_from_file
from exceptions import ContextError

__all__ = ["UniqApp"]


class UniqApp(App):
    """Class representing the uniq shell application

    Args:
        args (:obj:`list`): Contains all the arguments and options
            of the instruction
    """
    def __init__(self, args):
        super().__init__(args)
        try:
            self.options, self.args = getopt(args, "i")
        except GetoptError as error:
            raise ContextError("uniq", str(error)) from None

    def run(self, inp, out):
        """Executes the uniq command on the given arguments.

        Args:
            inp (:obj:`deque`, *optional*): The input args of the command,
                only used for piping and redirects.
            out (:obj:`deque`): The output deque, used to store
                the result of execution.

        Returns:
            ``deque``: The deque will contain all lines of the file that are
            identical to the previous line in the file.

        Raises:
            RunError: If any of the paths specified do not exist.
        """
        case = not bool(self.options)
        if inp:
            contents = inp
        elif not self.args:
            contents = [input()]
        else:
            contents = read_lines_from_file(self.args[0], "uniq")
        if case:
            self._run(contents, out)
        else:
            self._run_unsensitive(contents, out)
        return out

    def _run(self, lines, out):
        """Removes duplicate lines and appends each line to the
        output deque.

        Args:
            lines (:obj: `list`, *optional*): The lines to filter through.
            out (:obj:`deque`): The output deque, used to store
                the result of execution.
        """
        prev = lines[0]
        out.append(prev.rstrip())
        for i in range(1, len(lines)):
            if lines[i].rstrip() != prev.rstrip():
                prev = lines[i]
                out.append(lines[i].rstrip())

    def _run_unsensitive(self, lines, out):
        """Removes duplicate lines (irrespective of case) and appends
        each line to the output deque.

        Args:
            lines (:obj: `list`, *optional*): The lines to filter through.
            out (:obj:`deque`): The output deque, used to store
                the result of execution.
        """
        prev = lines[0]
        out.append(prev.rstrip())
        for i in range(1, len(lines)):
            if lines[i].rstrip().upper() != prev.rstrip().upper():
                prev = lines[i]
                out.append(lines[i].rstrip())

    def validate_args(self):
        """No args need to be checked for this application"""
