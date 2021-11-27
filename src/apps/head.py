from apps.app import App
from getopt import getopt
from exceptions.app_run import AppRunException
from common.tools import read_lines_from_file


class HeadApp(App):
    """
    head [OPTIONS] [FILE]
    """

    def __init__(self, args):
        self.options, self.args = getopt(args, "n:")

    def run(self, inp, out):
        """ """
        if self.options:
            lines = int(self.options[0][1])
        else:
            lines = 10
        if inp:
            self._run(inp, lines, out)
            return out
        if not self.args:
            for _ in range(lines):
                out.append(input())
            return out
        if len(self.args) > 1:
            for arg in self.args:
                out.extend("\n--> " + arg + " <--\n")
                contents = read_lines_from_file(arg, "head")
                self._run(contents, lines, out)
        else:
            contents = read_lines_from_file(self.args[0], "head")
            self._run(contents, lines, out)
        return out

    def _run(self, text, lines, out):
        for i in range(0, lines):
            if i == len(text):
                break
            out.append(text[i].strip("\n"))

    def validate_args(self):
        # if not self.args:
        #     raise AppRunException(
        #         "head", "Missing option: [FILE]")
        if self.options:
            if self.options[0][0] != "-n":
                raise AppRunException("head", f"Invalid option: {self.options[0][0]}")
