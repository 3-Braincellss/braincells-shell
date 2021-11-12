from abc import abstractmethod, ABCMeta

from exceptions.app_context import AppContextException

"""
This module provides an interface for an App.
"""


class App(metaclass=ABCMeta):

    allow = {}

    def __init__(self):
        pass

    @abstractmethod
    def validate_args(self):
        pass

    @abstractmethod
    def run(self):

        pass
