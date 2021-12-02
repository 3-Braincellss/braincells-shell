"""Module representing the shell cd application
Usage in shell: cd PATH

Example:
    `cd foo/bar/baz`
"""
import os

from exceptions import ContextError, RunError
from apps import App


class CdApp(App):
    """A class representing the cd shell instruction

    Args:
        args (:obj: `list`): Contains all the arguments and options of the instruction

    """

    def __init__(self, args):
        self._args = args

    def run(self, inp, out):
        """Executes the cd command on the given arguments.

        If no arguments are given, the current directory is changed to the users root directory.
        If not the users current working directory is changed to the directory given. This path
        can be relative or absolute.

        Args:
            inp (:obj: `deque`, optional): The input args of the command, only used for piping
                and redirects. In context of this specific application, it does not support
                piping and will therefore be ignored.
            out (:obj: `deque`): The output deque, used to store the result of execution.

        Returns:
            ``deque``: The deque filled with the results of application execution. Since the
                cd application does not return anything, this will be unaltered.

        Raises:
            AppRunException: If the path supplied is not a directory.
        """
        if len(self._args) == 0:
            os.chdir("/")
        else:
            try:
                os.chdir(self._args[0])
            except OSError:
                raise RunError(
                    "cd",
                    f"{self._args[0]} is not a directory\
                .",
                ) from None
        return out

    def validate_args(self):
        """Check that the number of arguments is greater than 1 and if the given path exists.

        Raises:
            AppContextException: If more than one argument is supplied or the path given does
                not exist.
        """
        if len(self._args) > 1:
            raise ContextError("cd", "Wrong number of arguments")
        if self._args and not os.path.exists(self._args[0]):
            raise ContextError(
                "cd",
                f"path '{self._args[0]}' doesn't \
            exist",
            )
