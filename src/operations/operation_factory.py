from apps import AppFactory

from operations import (
    Call,
    Pipe,
    Sequence,
)


class OperationFactory:

    """
    Operation object creation will be handled with this module.
    """

    def __init__(self):
        self.ops = {
            "call": self._call,
            "pipe": self._pipe,
            "seq": self._seq,
        }

    def get_operation(self, op_str, data):
        return self.ops[op_str](data)

    def _call(self, data):
        app_str = data["app"]
        args = data["args"]
        af = AppFactory()
        try:
            app = af.get_app(app_str, args)

        except Exception as e:
            raise e

        return Call(app)

    def _pipe(self, data):
        op1 = data["op1"]
        op2 = data["op2"]
        return Pipe(op1, op2)

    def _seq(self, data):
        op1 = data["op1"]
        op2 = data["op2"]
        return Sequence(op1, op2)
