"""Module representing the cat application:
Usage in shell: cat [FILES]...

Example:
    cat bee-movie-script.txt
"""

from getopt import getopt
from common.tools import read_lines_from_file
from exceptions import ContextError
from apps import App


class CatApp(App):
    """A class representing the cat command line instruction

    Args:
        args (:obj:`list`): Contains all the arguments and options of the cat instruction

    """

    def __init__(self, args):
        super().__init__(args)
        self._options, self.args = getopt(self.args, "")

    def run(self, inp, out):
        """Executes the cat command on the given arguments.

        Args:
            inp (:obj:`deque`, optional): The input args of the command, only used for piping
                and redirects.
            out (:obj:`deque`): The output deque, used to store the result of execution.

        Returns:
            ``deque``: Each value of this ``deque`` will be a single line from the input file
            or piped data.

        """
        if inp:
            out.extend(inp)
            return out

        if not self.args:
            out.append(input())
            return out

        self._run(self.args, out)

        return out

    @classmethod
    def _run(cls, paths, out):
        for path in paths:
            out.extend(map(str.rstrip, read_lines_from_file(path, "cat")))
        return out

    def validate_args(self):
        """Ensures that no options have been supplied to the application.

        Raises:
            ContextError: If an option has been supplied to the application.
        """
        for option in self._options:
            raise ContextError(
                "cat",
                f"{option}: is an unsupported option \
            :(",
            )
