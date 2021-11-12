from abc import abstractmethod, ABCMeta

"""
This is an interface definition for an Operation class
"""


class Operation(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def run(inp, out):

        pass
