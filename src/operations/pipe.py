"""
Pipe
====
"""
from collections import deque

from operations.operation import Operation


class Pipe(Operation):
    """Pipe Class

    Attributes:
        op1(Operation): An Operation that is run first.
            Its output will be piped to the second operation.
        op2(Operation): An Operation that is run second.
            Its input will be the output of the first operation.
    """
    def __init__(self, ctx):
        super().__init__(ctx)
        self.op1 = ctx["op1"]
        self.op2 = ctx["op2"]

    def run(self, inp, out):
        out = self.op1.run(inp, out)
        new_out = deque()
        return self.op2.run(out, new_out)
