from apps import App
from getopt import getopt
from exceptions import AppRunException
from common.tools import read_lines_from_file
import re


class GrepApp(App):

    """
    Application representing the bash command:
    grep [PATTERN] [FILE]*
    """

    def __init__(self, args):
        self.option, self.args = getopt(args, "")

    def run(self, inp, out):
        """
        Performs the grep operation on all specified paths.
        :param inp: The input args of the command, only used for piping
        and redirects.
        """
        self.pattern = self.args[0]

        if len(self.args) == 1:

            lines = "".join(inp).split("\n") if inp else [input()]
            self._run(lines, out)
            return out
        paths = self.args[1:]
        for path in paths:
            if path == "-":
                self._run([input()], out)
                continue
            contents = read_lines_from_file(path, "grep")
            self._run(contents, out)
        return out

    def _run(self, lines, out):
        for line in lines:
            if re.search(self.pattern, line):
                x = line
                if x[-1] != "\n":
                    x += "\n"
                out.append(x)

    def validate_args(self):
        if not self.args:
            raise AppRunException("grep", "Usage: grep [PATTERN] [FILE]...")
