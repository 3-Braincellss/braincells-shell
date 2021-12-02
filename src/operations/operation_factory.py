"""Operation Factory is used to create operation objects on given string."""

from operations import (
    Call,
    Pipe,
    Sequence,
)


class OperationFactory:
    """A class that is used to create operations objects"""

    operations = {
        "call": Call,
        "pipe": Pipe,
        "seq": Sequence,
    }
    """Operations ``dict`` that maps operation names to their classes"""

    @classmethod
    def get_operation(cls, op_str):
        """Returns an operation object given the operation name and context data

        Parameters:
            op_str(:obj:`str`): Name of the operation.
            ctx(:obj:`dict`):a context dictionary containing information required
                for initialisation of a certain concrete ``Operation`` object
                Maps property name to arbitrarily typed data.

        Returns:
            Operation: Concrete operation object.
        """
        return cls.operations[op_str](ctx)
