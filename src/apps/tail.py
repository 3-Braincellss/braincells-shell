from apps.app import App
from getopt import getopt
from exceptions import AppRunException
from common.tools import read_lines_from_file
from collections import deque


class TailApp(App):
    """
    head [OPTIONS] [FILE]
    """

    def __init__(self, args):
        self.options, self.args = getopt(args, "n:")

    def run(self, inp, out):
        """ """
        out = deque()
        if self.options:
            lines = int(self.options[0][1])
        else:
            lines = 10
        if inp:
            self._run(inp, lines, out)
            return out
        if len(self.args) > 1:
            for arg in self.args:
                out.extend("\n--> " + arg + " <--\n")
                contents = read_lines_from_file(arg, "tail")
                self._run(contents, lines, out)
        else:
            contents = read_lines_from_file(self.args[0], "tail")
            self._run(contents, lines, out)
        return out

    def _run(self, text, lines, out):
        start = 0 if len(text) - lines < 0 else len(text) - lines
        for i in range(start, len(text)):
            out.append(text[i].strip("\n"))

    def validate_args(self):
        # if not self.args:
        #     raise AppRunException(
        #         "tail", "Missing option: [FILE]")
        if self.options:
            if self.options[0][0] != "-n":
                raise AppRunException("tail", f"Invalid option: {self.options[0][0]}")
