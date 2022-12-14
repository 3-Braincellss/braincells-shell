"""
app
===
This module provides an interface for an App.
"""
from abc import ABCMeta, abstractmethod

__all__ = ["App"]


class App(metaclass=ABCMeta):
    """An abstract class representing the format of all Apps.

    Args:
        args (:obj:`list`): Contains all the arguments and options of
            the application.
    """
    def __init__(self, args):
        self.args = args

    @abstractmethod
    def validate_args(self):
        """
        Checks whether the given args are appropriate for the application.

        Does **NOT** affect actual execution behaviour
        """

    @abstractmethod
    def run(self, inp, out):
        """Executes the application on the given arguments.

        Args:
            inp (:obj:`deque`, *optional*): The input args of the command,
                only used for piping and redirects.
            out (:obj:`deque`): The output deque, used to store the
                result of execution.

        Returns:
            ``deque``: The deque filled with the results of application
            execution.

        """
