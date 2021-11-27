"""
An operation primitive that contains an up that it runs.
"""
from operations import Operation
from apps import AppFactory


class Call(Operation):
    def __init__(self, data):
        self.app = AppFactory.get_app(data["app"], data["args"])

    def run(self, inp, out):
        out = self.app.run(inp, out)
        return out
