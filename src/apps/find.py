"""
find
====
Module representing the find application.
Usage in shell: find -name [PATTERN] [PATH]

Example:
    ``find -name *.py project/spaghetti-code``
"""
import os
from getopt import gnu_getopt
from glob import glob

from apps.app import App
from exceptions import ContextError, RunError

__all__ = ["FindApp"]


class FindApp(App):
    """A class representing the find shell instruction

    Args:
        args (:obj:`list`): Contains all the arguments and options
        of the instruction

    """
    def __init__(self, args):
        super().__init__(args)
        for i in range(len(args)):
            if args[i] == "-name":
                args[i] = "--name"  # getopt only recognises long options with
                break  # a -- prefix
        self.options, self.args = gnu_getopt(args, "", ["name="])

    def run(self, inp, out):
        """Executes the find command on the given path.

        Will match all files with the pattern supplied in the name option.
        If no path is supplied the current directory is used.

        Args:
            inp (:obj:`deque`, *optional*): The input args of the command,
                only used for piping and redirects.
            out (:obj:`deque`): The output deque, used to store
                the result of execution.

        Returns:
        ``deque``: The output deque will contain each of the files that
        matched the specified pattern

        Raises:
            RunError: If the root path supplied does not exist.
        """
        root = "" if not self.args else self.args[0]
        self.pattern = self.options[0][1]
        self._run(root, out)
        return out

    def _run(self, root, out):
        matched_files = glob(f"./{root}/**/{self.pattern}", recursive=True)
        for file in matched_files:
            if root != "":
                out.append(file[2:])  # Omit the ./
            else:
                out.append(file)

    def validate_args(self):
        """Ensures that the -name option is present and only one argument is
        given

        Raises:
            ContextError: If more than one argument is given or the -name
                option is missing.
        """
        if not self.options:
            raise ContextError(
                "find",
                "No pattern supplied. usage: find [PATH] -name PATTERN ",
            )
        if len(self.args) > 1:
            raise ContextError(
                "find",
                "Too many arguments supplied usage: find [PATH] -name PATTERN",
            )
        if self.args and not os.path.exists(self.args[0]):
            raise RunError(
                "find", f"{self.args[0]}: No such file or directory") from None
