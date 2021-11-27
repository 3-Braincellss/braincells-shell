from collections import deque
import os
from operations import Operation

from common.tools import read_lines_from_file


class LeftRedirect(Operation):
    def __init__(self, data):
        self.fname = data["fname"]
        self.op = data["op"]

    def run(inp, out):
        # if fname exists we write to that
        lines = deque(read_lines_from_file(path, "redirect"))
        self.op.run(lines, out)

        return out
