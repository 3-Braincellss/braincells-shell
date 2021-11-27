"""
An operation primitive that contains an up that it runs.
"""
from operations import Operation
from apps import AppFactory
from collections import deque
from common.tools import read_lines_from_file


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
            _inp = deque(map(str.rstrip, lines))

        if self.right_red is not None:
            _out = deque()
            with open(self.right_red, "w") as f:
                self.app.validate_args()
                _out = self.app.run(_inp, _out)
                for line in out:
                    f.write(line)
                    f.write("\n")
                return deque()
        else:
            self.app.validate_args()
            self.app.run(_inp, _out)
        return _out
