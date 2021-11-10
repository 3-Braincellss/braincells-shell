from operations.operation import Operation

"""
An operation primitive that contains an up that it runs.
"""
from operations.operation import Operation


class Call(Operation):
    def __init__(self):
        super().__init__()

    def run(self, inp):
        return self.app.run(inp)
