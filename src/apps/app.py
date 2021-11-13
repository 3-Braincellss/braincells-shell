"""
This module provides an interface for an App.
"""
from abc import abstractmethod, ABCMeta

from exceptions.app_context import AppContextException


class App(metaclass=ABCMeta):
    """
    An abstract class representing the format of all Apps.
    """
    allowed_options = {}

    def __init__(self):
        pass

    @abstractmethod
    def validate_args(self):
        """
        Checks whether the given args are appropriate for the application.
        """
        pass

    @abstractmethod
    def run(self):
        """
        Runs the application.
        """
        pass
