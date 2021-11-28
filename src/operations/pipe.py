from operations.operation import Operation
from collections import deque


class Pipe(Operation):
    """
    Standard pipe that redirects the output of one program to the input of
    another.
    """

    def __init__(self, data):
        self.op1 = data["op1"]
        self.op2 = data["op2"]

    def run(self, inp, out):
        out = self.op1.run(inp, out)
        new_out = deque()
        return self.op2.run(out, new_out)
