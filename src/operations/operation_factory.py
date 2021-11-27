from operations import (
    Call,
    Pipe,
    Sequence,
    Operation,
)


class OperationFactory:
    """A class that is used to create operations objects

    Attributes
    ----------
    operations: dict
        Maps operation names to concrete operation classes

    Methods
    -------

    get_operation(op_str, data): Operation
        Returns an operation object given the operation name and context data


    """

    operations = {
        "call": Call,
        "pipe": Pipe,
        "seq": Sequence,
    }

    @staticmethod
    def get_operation(op_str: str, data: dict) -> Operation:
        """Returns an operation object given the operation name and context data

        Parameters
        ----------

        op_str: str
            name of the operation

        data: dict
            a dictionary containing information required for initialisation of a
            certain concrete Operation object
            Maps property name to arbitrarily typed data.
        """
        return OperationFactory.operations[op_str](data)
