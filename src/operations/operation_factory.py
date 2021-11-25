from functools import singledispatch
from apps import AppFactory

from exceptions import AppNotFoundException, AppContextException

from operations import (
    Call,
    Pipe,
    Sequence,
)

"""
Operation object creation will be handled with this module.
"""


class OperationFactory:
    def __init__(self):
        self.apps = {
            "call": self._call,
            "pipe": self._pipe,
            "seq": self._seq,
        }

    def get_operation(self, op_str, data):
        return self.apps[op_str](data)

    def _call(self, data):
        app_str = data["app"]
        args = data["args"]
        af = AppFactory()
        try:
            app = af.get_app(app_str, args)
            return Call(app)
        except AppNotFoundException as anfe:
            raise anfe
        except AppContextException as ace:
            raise ace

    def _pipe(self, data):
        op1 = data["op1"]
        op2 = data["op2"]
        return Pipe(op1, op2)

    def _seq(self, data):
        op1 = data["op1"]
        op2 = data["op2"]
        return Sequence(op1, op2)
