"""
Command Factory
=================
Command Factory is used to create operation objects on given string."""

from commands import Call, Pipe, Sequence

__all__ = [
    "CommandFactory",
]


class CommandFactory:
    """A class that is used to create operations objects"""

    commands = {
        "call": Call,
        "pipe": Pipe,
        "seq": Sequence,
    }
    """Commands ``dict`` that maps operation names to their classes"""
    @classmethod
    def get_command(cls, op_str, ctx):
        """Returns an operation object given the operation name and context data

        Parameters:
            op_str(:obj:`str`): Name of the operation.
            ctx(:obj:`dict`):a context dictionary containing information
                required for initialisation of a certain concrete ``Command``
                object. Maps property name to arbitrarily typed data.

        Returns:
            Command: Concrete operation object.
        """
        return cls.commands[op_str](ctx)
