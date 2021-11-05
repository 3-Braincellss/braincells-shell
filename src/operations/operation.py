from abc import abstractmethod, ABC

"""
This is an interface definition for an Operation class
"""


class Operation(metaclass=ABC):
    def __init__(self):
        pass

    @abstractmethod
    def exec(inp, out):

        pass
