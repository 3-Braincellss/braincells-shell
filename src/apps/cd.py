"""
cd
==
Module representing the cd application
Usage in shell: cd PATH

Example:
    `cd foo/bar/baz`
"""
import os

from apps import App
from exceptions import ContextError, RunError


class CdApp(App):
    """A class representing the cd shell instruction

    Args:
        args (:obj:`list`): Contains all the arguments and options of
            the instruction.

    """
    def run(self, inp, out):
        """Executes the cd command on the given arguments.

        If no arguments are given, the current directory is changed to the
        users **HOME** directory. If not the users current working directory
        is changed to the directory given. This path can be relative or
        absolute.

        Args:
            inp (:obj:`deque`, *optional*): The input args of the command, only
                used for piping and redirects. In context of this specific
                application, it does not support piping and will therefore
                be ignored.
            out (:obj:`deque`): The output deque, used to store the result
                of execution.

        Returns:
            ``deque``: Since the cd application does not return anything,
            output will be unaltered.

        Raises:
            RunError: If the path supplied is not a directory.

        """
        if len(self.args) == 0:
            os.chdir(os.path.expanduser("~"))
        else:
            try:
                os.chdir(self.args[0])
            except OSError:
                raise RunError(
                    "cd",
                    f"{self.args[0]} is not a directory",
                ) from None
        return out

    def validate_args(self):
        """Check that the number of arguments is greater than 1 and if
        the given path exists.

        Raises:
            ContextError: If more than one argument is supplied or
                the path given does not exist.
        """
        if len(self.args) > 1:
            raise ContextError("cd", "Wrong number of arguments")
        if self.args and not os.path.exists(self.args[0]):
            raise ContextError(
                "cd",
                f"path '{self.args[0]}' doesn't exist",
            )
