from collections import deque
import os
from operations import Operation


class RightRedirect(Operation):
    def __init__(self, data):
        self.fname = data["fname"]
        self.op = data["op"]

    def run(inp, out):
        # if fname exists we write to that

        with open(self.fname, "w") as f:
            out = self.op.run(inp, out)
            for line in out:
                f.write(line)
                f.write("\n")

        return deque()
