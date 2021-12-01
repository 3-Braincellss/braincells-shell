"""
This module provides an interface for an App.
"""
from abc import abstractmethod, ABCMeta


class App(metaclass=ABCMeta):
    """
    An abstract class representing the format of all Apps.
    """

    @abstractmethod
    def validate_args(self):
        """
        Checks whether the given args are appropriate for the application.
        """
        pass

    @abstractmethod
    def run(self, inp, out):
        """
        Runs the application.
        """
        pass
