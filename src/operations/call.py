from operations.operation import Operation

"""
An operation primitive that contains an up that it runs.
"""
from operations.operation import Operation


class Call(Operation):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def run(self, inp):
        return self.app.run(inp)
