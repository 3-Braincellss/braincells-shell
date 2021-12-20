"""
ls
==
Module representing the ls application
Usage in shell: ls [PATH]

Example:
    `ls super/secret/directory`
"""
import os

from apps import App
from exceptions import ContextError, RunError

__all__ = [
    "LsApp"
]


class LsApp(App):
    """A class representing the ls shell instruction

    Lists all files and directory in the specified directories. If none is
    given, lists the files and directories in the current directory.

    Args:
        args (:obj:`list`): Contains all the arguments and options of the
        instruction.
    """

    def __init__(self, args):
        super().__init__(args)
        self.args = args

    def run(self, inp, out):
        """Executes the ls command on the given argument.

        Lists all files/directories in a specified directory. If none is
        given, lists the files/directories in the current directory.

        Args:
            inp (:obj:`deque`, *optional*): The input args of the command, only
                used for piping and redirects.
            out (:obj:`deque`): The output deque, used to store the result of
                execution.

        Returns:
            ``deque``: Contains all of the files in the specified and current
            directory.

        Raises:
            ContextError: If the path supplied is not a directory.

        """

        if len(self.args) == 0:
            ls_dirs = [os.getcwd()]
        else:
            ls_dirs = self.args

        for path in ls_dirs:
            try:
                files = sorted(
                    [each for each in os.listdir(path) if each[0] != "."])
                out.extend(files)
            except OSError as error:
                raise RunError("ls", str(error)) from None

        return out

    def validate_args(self):
        """Ensures at most one valid path is given.

        Raises:
            ContextError if too many paths are given.
        """

        if len(self.args) > 1:
            raise ContextError("ls", "too many arguments")
        if len(self.args) == 1:
            if not os.path.exists(self.args[0]):
                raise ContextError("ls", f"{self.args[0]}: not a directory")
