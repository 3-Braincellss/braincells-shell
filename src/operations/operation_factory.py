from operations.call import Call
from functools import singledispatch

"""
Operation object creation will be handled with this module.
"""


class OperationFactory:
    def __init__(self):
        self.apps = {
            "call": self._call,
        }

    def get_operation(self, app_str, args):
        return self.apps[app_str](args)

    """ Creates a call object"""

    def _call(self, app_string):
        app = AppFactory.get_app(app_str, args)
