"""
mkdir
=====
Module representing the mkdir application
Usage in shell: mkdir [PATH]+

Example:
    ``mkdir mega_dir ultra_dir turbo_dir``
"""

import os

from apps.app import App
from exceptions import ContextError


class MkdirApp(App):
    """A class representing the mkdir shell instruction.

    Args:
    args (:obj:`list`): Contains all the arguments and options
    of the instruction.

    """
    def __init__(self, args):
        super().__init__(args)
        self.args = args

    def run(self, inp, out):
        """Executes the mkdir command on the given path.

        Creates a directory for each argument specified.

        Args:
            inp (:obj:`deque`, *optional*): The input args of the command,
                only used for piping and redirects. Not used in this
                application.m
            out (:obj:`deque`): The output deque, used to store
                the result of execution, in this case the deque will not
                be altered.

        Returns:
        ``deque``: The output deque will contain each of the files that
        matched the specified pattern
        """
        for arg in self.args:
            os.mkdir(arg)
        return out

    @staticmethod
    def _valid_path(arg):
        split_args = arg.split("/")
        path_to = ("/".join(split_args[:-1]) if
                   (split_args[-1] != "") else "/".join(arg.split("/")[:-2]))
        if not path_to or os.path.exists(path_to):
            return True
        return False

    def validate_args(self):
        """Ensures all arguments either represent a valid path
        or a single new directory name.

        Raises:
            ContextError: If the path to the path being added does not exist.
        """

        if not self.args:
            raise ContextError("mkdir", "Missing operands")
        for arg in self.args:
            if not self._valid_path(arg):
                raise ContextError("mkdir",
                                   f"'{arg}': No such file or directory")
            if os.path.exists(arg):
                raise ContextError("mkdir", f"'{arg}':Path already exists")
