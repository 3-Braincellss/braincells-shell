from apps import App
from getopt import getopt
from exceptions import AppRunException
from common.tools import read_lines_from_file

class UniqApp(App):
    """
    """

    def __init__(self, args):
        self.options, self.args = getopt(args, "i")

    def run(self, inp, out):
        """
        """
        case = False if self.options else True
        if not self.args:
            contents = [input()]
        else:
            contents = read_lines_from_file(self.args[0])
        if case:
            self._run_unsensitive(contents, out)
        else:
            self._run(contents, out)
        return out

    def _run(self, lines, out):
        out.append(lines[0])
        prev = lines[0]
        for i in range(1,len(lines)):
            if lines[i] != prev:
                prev = lines[i]
                out.append(lines[i])

    def _run_unsensitive(self, lines, out):
        out.append(lines[0])
        prev = lines[0]
        for i in range(1,len(lines)):
            if lines[i].upper() != prev.upper():
                prev = lines[i]
                out.append(lines[i])


    def validate_args(self):
        if len(self.args) > 1:
            raise AppRunException("uniq", "too many arguments")
        pass
