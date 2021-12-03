"""
call
====
An operation primitive that contains an up that it runs.
"""
from operations import Operation
from apps import AppFactory
from collections import deque
from common.tools import read_lines_from_file


class Call(Operation):
    def __init__(self, ctx):
        self.app = AppFactory.get_app(
            ctx["app"],
            ctx["args"],
        )
        self.left_red = ctx["left_red"]
        self.right_red = ctx["right_red"]

    def run(self, inp, out):
        _inp = inp
        if self.left_red is not None and not inp:
            lines = deque(read_lines_from_file(self.left_red, "redirect"))
            _inp = deque(map(str.rstrip, lines))

        if self.right_red is not None:
            _out = deque()
            with open(self.right_red, "w") as f:
                self.app.validate_args()
                _out = self.app.run(_inp, _out)
                for line in _out:
                    f.write(line)
                    f.write("\n")
        else:
            self.app.validate_args()
            self.app.run(_inp, out)
        return out

    def validate_context(self, ctx):
        pass
