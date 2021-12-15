"""
Operation
=========
This is an interface definition for an Operation class.
"""

from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    """Interface for an operation

    Operations are created on the transforming stage.
    Operations are either a ``Call`` or some connective that
    combines multiple operations such as ``Pipe``.

    """
    def __init__(self, ctx):
        self.ctx = ctx

    @abstractmethod
    def run(self, inp, out):
        """Runs the operation

        Parameters:
            inp(:obj:`deque`): Piped input to the operation.
            out(:obj:`out`): output of all operations that were
                run before the current one
        """
