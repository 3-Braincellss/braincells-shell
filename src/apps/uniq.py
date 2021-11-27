from apps import App
from getopt import getopt
from exceptions import AppRunException
from common.tools import read_lines_from_file


class UniqApp(App):
    """ """

    def __init__(self, args):
        self.options, self.args = getopt(args, "i")

    def run(self, inp, out):
        """
        Executes that uniq command on the given arguments.
        :param inp: The input args of the command, only used for piping
        and redirects.
        :param out: The output deque.
        :return: Returns the output deque.
        """
        case = False if self.options else True
        if inp:
            contents = inp
        elif not self.args:
            contents = [input()]
        else:
            contents = read_lines_from_file(self.args[0], "uniq")
        if case:
            self._run(contents, out)
        else:
            self._run_unsensitive(contents, out)
        return out

    def _run(self, lines, out):
        """
        Removes duplicate lines and appends each line to the
        output deque.
        :param lines: The lines to filter through.
        :param deque: The output deque
        """
        out.append(lines[0].strip("\n"))
        prev = lines[0]
        for i in range(1, len(lines)):
            if lines[i] != prev:
                prev = lines[i]
                out.append(lines[i].strip("\n"))

    def _run_unsensitive(self, lines, out):
        """
        Removes duplicate lines (irrespective of case) and appends each line to the
        output deque.
        :param lines: The lines to filter through.
        :param deque: The output deque
        """
        out.append(lines[0])
        prev = lines[0]
        for i in range(1, len(lines)):
            if lines[i].upper() != prev.upper():
                prev = lines[i]
                out.append(lines[i])

    def validate_args(self):
        """
        Ensures the options are valid.
        :raises AppRunException: If any other option other than -i is
        given, or multiple paths are given as args
        """
        if len(self.args) > 1:
            raise AppRunException("uniq", "too many arguments")
        if len(self.options) > 1:
            raise AppRunException("uniq", "too many options")
        if self.options and self.options[0][0] != "-i":
            raise AppRunException("uniq", f"invalid option {option}")
