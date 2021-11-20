from apps.app import App
from getopt import getopt
from exceptions.app_run import AppRunException
from common.tools import read_lines_from_file
from collections import deque


class HeadApp(App):
    """
    head [OPTIONS] [FILE]
    """

    def __init__(self, args):
        self.options, self.args = getopt(args, "n:")

    def run(self, inp, out):
        """
        """
        out = deque()
        if self.options:
            lines = int(self.options[0][1])
        else:
            lines = 10


        if len(self.args) > 1:
            for arg in self.args:
                out.extend("\n--> " + arg + " <--\n")
                out.extend(read_lines_from_file(arg, "head")[:lines])
        else:
            out.extend(read_lines_from_file(self.args[0], "head")[:lines])
        return out

    def validate_args(self):
        if not self.args:
            raise AppRunException(
                "head", "Missing option: [FILE]")
        if self.options:
            if self.options[0][0] != '-n':
                raise AppRunException(
                    "head", f"Invalid option: {self.options[0][0]}")
