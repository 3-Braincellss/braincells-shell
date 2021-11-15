"""
An operation primitive that contains an up that it runs.
"""
from operations import Operation


class Call(Operation):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def run(self, inp, out):
        out = self.app.run(inp, out)
        return out
