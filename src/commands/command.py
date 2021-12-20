"""
Command
=======
This is an interface definition for an Command class.
"""

from abc import ABCMeta, abstractmethod

__all__ = [
    "Command",
]


class Command(metaclass=ABCMeta):
    """Interface for a command

    Commands are created on the transforming stage.
    Commands are either a ``Call`` or some connective that
    combines multiple commands such as ``Pipe``.

    """
    def __init__(self, ctx):
        self.ctx = ctx

    @abstractmethod
    def run(self, inp, out):
        """Runs the command

        Parameters:
            inp(:obj:`deque`): Piped input to the command.
            out(:obj:`out`): output of all commands that were
                run before the current one
        """
