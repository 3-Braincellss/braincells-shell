import re
import os

from apps import App
from getopt import getopt
from exceptions import RunError
from common.tools import read_lines_from_file


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

            lines = inp if inp else [input()]
            self._run(lines, out)
            return out
        paths = self.args[1:]
        for path in paths:
            if path == "-":  # nani?
                self._run([input()], out)
                continue
            contents = read_lines_from_file(path, "grep")
            self._run(contents, out, path, len(paths) > 1)
        return out

    def _run(self, lines, out, path=None, multiple=False):
        for line in lines:
            if re.search(self.pattern, line):
                if multiple:
                    x = f"{path}:{line.rstrip()}"
                else:
                    x = line.rstrip()
                out.append(x)

    def validate_args(self):
        if not self.args:
            raise AppContextException("grep", "Usage: grep [PATTERN] [FILE]...")
