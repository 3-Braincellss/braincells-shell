"""
cat
===
Module representing the cat application:
Usage in shell: cat [FILES]...

Example:
    cat bee-movie-script.txt
"""

from getopt import GetoptError, getopt

from apps import App
from common.tools import read_lines_from_file
from exceptions import ContextError


class CatApp(App):
    """A class representing the cat command line instruction

    Args:
        args (:obj:`list`): Contains all the arguments and options of the cat
            instruction

    """

    def __init__(self, args):
        super().__init__(args)
        try:
            self._options, self.args = getopt(self.args, "")
        except GetoptError as e:
            raise ContextError("cat", str(e)) from None

    def run(self, inp, out):
        """Executes the cat command on the given arguments.

        Args:
            inp (:obj:`deque`, optional): The input args of the command, only
                used for piping and redirects.
            out (:obj:`deque`): The output deque, used to store the result of
                execution.

        Returns:
            ``deque``: Each value of this ``deque`` will be a single line from
            the input file or piped data.

        """
        if inp:
            out.extend(inp)
            return out

        if not self.args:
            out.append("")
            while True:
                try:
                    out.append(input())
                except KeyboardInterrupt:
                    return out

        self._run(self.args, out)

        return out

    @classmethod
    def _run(cls, paths, out):
        for path in paths:
            contents = read_lines_from_file(path, "cat")
            for line in contents:
                out.append(line.rstrip("\n"))
        return out

    def validate_args(self):
        pass
