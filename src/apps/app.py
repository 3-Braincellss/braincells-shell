from abc import abstractmethod, ABCMeta

"""
This module provides an interface for an App.
"""


class App(metaclass=ABCMeta):

    allow = {}

    def __init__(self):

        pass

    """ Raises context error """

    @abstractmethod
    def validate_args(self):

        pass

    """ Raises runtime error """

    @abstractmethod
    def run(self):

        pass
