"""
rm
====
Module representing the mkdir application
Usage in shell: rm [OPTIONS] [PATH]+

Example:
    ``rm useless_file``
"""

import os
from shutil import rmtree
from getopt import getopt, GetoptError

from apps.app import App
from exceptions import ContextError


class RmApp(App):
    """A class representing the rm shell instruction.

    Args:
        args (:obj:`list`): Contains all the arguments and options
            of the instruction.

    Raises:
        ContextError: If any invalid options are given.

    """
    def __init__(self, args):
        super().__init__(args)
        try:
            self.options, self.args = getopt(args, "r")
        except GetoptError as error:
            raise ContextError("rm", str(error)) from None

    def run(self, inp, out):
        """Executes the rm command on the given path.

        Deletes a directory/file for each argument specified.

        Args:
            inp (:obj:`deque`, *optional*): The input args of the command,
                only used for piping and redirects. Not used in this
                application.
            out (:obj:`deque`): The output deque, used to store
                the result of execution, in this case the deque will not
                be altered.

        Returns:
        ``deque``: The output deque will contain each of the files that
        matched the specified pattern
        """
        for arg in self.args:
            if os.path.isfile(arg):
                os.remove(arg)
            else:
                if self.options:
                    rmtree(arg, ignore_errors=True)
                else:
                    try:
                        os.rmdir(arg)
                    except OSError as error:
                        raise ContextError("rm", str(error)) from None
        return out

    @staticmethod
    def _valid_path(arg):
        split_args = arg.split("/")
        path_to = ("/".join(split_args[:-1])
                   if split_args[-1] != "" else "/".join(arg.split("/")[:-2]))
        if not path_to or os.path.exists(path_to):
            return True
        return False

    def validate_args(self):
        """Ensures all arguments are valid paths.

        Raises:
            ContextError: If the path to the path does not exist.
        """

        for arg in self.args:
            if not self._valid_path(arg):
                raise ContextError(
                    "rm",
                    (f"cannot delete directory '{arg}': "
                     "No such file or directory"),
                )
        if not self.args:
            raise ContextError("rm", "Missing operand.")
