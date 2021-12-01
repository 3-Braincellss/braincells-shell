"""Module representing the cat application:
Usage in shell: cat [FILES]...
"""

from getopt import getopt
from common.tools import read_lines_from_file
from exceptions import AppContextException
from apps import App


class CatApp(App):
    """ A class representing the cat command line instruction

        Args:
            args (:obj: `list`): Contains all the arguments and options of the cat instruction

    """

    def __init__(self, args):
        self._options, self._args = getopt(args, "")

    def run(self, inp, out):
        """Executes the cat command on the given arguments.

        Args:
            inp (:obj: `deque`, optional): The input args of the command, only used for piping
                and redirects.
            out (:obj: `deque`): The output deque, used to store the result of execution.

        Returns:
            ``deque``: The deque filled with the results of application execution.

        """
        if inp:
            out.extend(inp)
            return out

        if not self._args:
            out.append(input())
            return out

        self._run(self._args, out)

        return out

    @classmethod
    def _run(cls, paths, out):
        for path in paths:
            out.extend(map(str.rstrip, read_lines_from_file(path, "cat")))
        return out

    def validate_args(self):
        """Ensures that no options have been supplied to the application.

            Raises:
                AppContextError: If an option has been supplied to the application.
        """
        for option in self._options:
            raise AppContextException(
                "cat",
                f"{option}: is an unsupported option \
            :(",
            )
