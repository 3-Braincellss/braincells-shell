from operations.call import Call
from functools import singledispatch
from apps.app_factory import AppFactory

"""
Operation object creation will be handled with this module.
"""


class OperationFactory:
    def __init__(self):
        self.apps = {
            "call": self._call,
        }

    def get_operation(self, op_str, data):
        return self.apps[op_str](data)

    """ Creates a call object"""

    def _call(self, data):
        app_str = data["app"]
        args = data["args"]

        app = AppFactory.get_app(app_str, args)

    def _pipe(self, app_string):
        pass
