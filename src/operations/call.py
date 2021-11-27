"""
An operation primitive that contains an up that it runs.
"""
from operations import Operation
from apps import AppFactory
from deque import deque


class Call(Operation):
    def __init__(self, data):
        self.app = AppFactory.get_app(
            data["app"],
            data["args"],
        )
        self.left_red = data["left_red"]
        self.right_red = data["right_red"]

    def run(self, inp, out):
        _inp = inp
        _out = out
        if self.left_red is not None and not inp:
            lines = deque(read_lines_from_file(self.left_red, "redirect"))
            _inp = deque(lines)

        if self.right_red is not None:
            _out = deque()
            with open(self.fname, "w") as f:
                out = self.op.run(inp, out)
                for line in out:
                    f.write(line)
                    f.write("\n")

        self.app.validate_args()
        out = self.app.run(_inp, _out)
        return out
