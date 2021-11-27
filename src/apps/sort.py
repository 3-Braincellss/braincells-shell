import os

from getopt import getopt, GetoptError

from apps import App
from exceptions import AppContextException, AppRunException
from common.tools import read_lines_from_file


class SortApp(App):
    """
    Sorts the contents of a file/stdin line by line and prints the result to stdout.

    sort [OPTIONS] [FILE]

    OPTIONS:

        -r sorts lines in reverse order

    FILE is the name of the file. If not specified, uses stdin.
    """

    def __init__(self, args):
        self.args = args

    def run(self, inp, out):
        """ """

        opts = self.args[0]
        args = self.args[1]

        # Reverse order when -r option is provided
        rev = True if opts else False

        # if args array is non zero then use file as the input
        if args:
            contents = read_lines_from_file(args[0], "sort")
            self._run(contents, rev, out)
        elif inp:
            self._run(inp, rev, out)

        return out

    def _run(self, text, rev, out):
        lines = sorted(text, reverse=rev)
        for line in lines:
            out.append(line.rstrip())

    def validate_args(self):

        # possible number of args: 0 - 2
        if len(self.args) > 2:
            raise AppContextException("sort", "too many arguments")

        # check options and arguments
        try:
            opts, args = getopt(self.args, "r")

        except GetoptError as goe:
            raise AppContextException("sort", "bad options")

        # after splitting self.args into opts and args
        self.args = opts, args
