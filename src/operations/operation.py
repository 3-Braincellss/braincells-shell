"""
operation
=========
This is an interface definition for an Operation class.
"""

from abc import abstractmethod, ABCMeta


class Operation(metaclass=ABCMeta):
    """Interface for an operation

    Operations are created on the transforming stage.
    Operations are either a ``Call`` or some connective that
    combines multiple operations such as ``Pipe``.

    """
    def __init__(self, ctx):
        pass

    @abstractmethod
    def run(self, inp, out):
        """Runs the operation

        Parameters:
            inp(:obj:`deque`): Piped input to the operation.
            out(:obj:`out`): output of all operations that were run before the current one
        """

    @abstractmethod
    def validate_context(self, ctx):
        """Checks if context of the operation is valid.

        Parameters:
            ctx(:obj:`dict`): Dictionary that maps value string to some arbitrarily typed data

        Raises:
            ContextError: If the context provided doesn't contain the correct keys or the values
                of the dictionary are not properly typed

        """
