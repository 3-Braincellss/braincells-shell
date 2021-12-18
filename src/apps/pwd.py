"""
pwd
===
Module representing the pwd application
Usage in shell: pwd

Example:
    `pwd`

"""
import os

from apps.app import App
from exceptions import ContextError


class PwdApp(App):
    """A class representing the pwd shell instruction

    Args:
        args (:obj:`list`): Contains all the arguments and options of
            the instruction, which should be empty.

    """
    def __init__(self, args):
        super().__init__(args)
        self.args = args

    def run(self, inp, out):
        """Executes the pwd command.

        Prints the path to the current working directory from root.

        Args:
            inp (:obj:`deque`, *optional*): The input args of the command, only
                used for piping and redirects. In context of this specific
                application, it does not support piping and will therefore
                be ignored.
            out (:obj:`deque`): The output deque, used to store the result
                of execution.

        Returns:
            ``deque``: Will contain the current working directory.
        """
        self.validate_args()
        out.append(os.path.abspath("."))
        return out

    def validate_args(self):
        """Ensures that no arguments are passed to the application.

        Raises:
            ContextError: If any argument is passed to the application.
        """
        if self.args:
            raise ContextError(
                "pwd", "This application does not accept any arguments")
