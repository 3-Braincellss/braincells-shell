from abc import abstractmethod, ABC

"""
This module provides an interface for an App.
"""


class App(metaclass=ABC):

    args = {}
    value = {}

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
