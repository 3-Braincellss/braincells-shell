from abc import abstractmethod, ABCMeta

"""
This module provides an interface for an App.
"""


class App(metaclass=ABCMeta):

    args = {}
    value = {}

    def __init__(self):

        pass

    """ Raises context error """

    @abstractmethod
    def validate_args(self):

        pass

    @abstractmethod
    def run(self, inp):
        """ """

        pass
