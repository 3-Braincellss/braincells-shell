from operations.call import Call
from operations.pipe import Pipe
from functools import singledispatch
from apps.app_factory import AppFactory

from exceptions.app_not_found import AppNotFoundException

"""
Operation object creation will be handled with this module.
"""


class OperationFactory:
    def __init__(self):
        self.apps = {
            "call": self._call,
            "pipe": self._pipe,
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




    def _pipe(self, data):
        op1 = data["op1"]
        op2 = data["op2"]
        return Pipe(op1, op2)
