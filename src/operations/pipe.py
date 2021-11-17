from operations.operation import Operation
from collections import deque


class Pipe(Operation):
    """
    Standard pipe that redirects the output of one program to the input of another.
    """

    def __init__(self, cm1, cm2):
        self.cm1 = cm1
        self.cm2 = cm2

    def run(self, inp, out):
        out = self.cm1.run(inp, out)
        new_out = deque()
        return self.cm2.run(out, new_out)
