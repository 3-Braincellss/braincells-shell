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

__all__ = ["CatApp"]


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
        except GetoptError as error:
            raise ContextError("cat", str(error)) from None

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
        if not self.args:
            result = inp if inp else self._get_input()
            out.extend(result)
            return out

        self._run(self.args, out)

        return out

    @classmethod
    def _run(cls, paths, out):
        for path in paths:
            contents = read_lines_from_file(path, "cat")
            for line in contents:
                out.append(line.rstrip())
        return out

    @staticmethod
    def _get_input():
        text = [""]
        while True:
            try:
                text.append(input())
            except KeyboardInterrupt:
                return text

    def validate_args(self):
        pass
