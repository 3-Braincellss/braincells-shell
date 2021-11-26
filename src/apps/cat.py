from apps import App
from getopt import getopt
from glob import glob
from common.tools import read_lines_from_file
from exceptions import AppRunException


class CatApp(App):
    """
    Application representing the bash command:
    cat [FILES]...
    """

    allowed_options = {}

    def __init__(self, args):
        self.options, self.args = getopt(args, "")

    def run(self, inp, out):
        """
        Executes that cat command on the given arguments.
        :param inp: The input args of the command, only used for piping
        and redirects.
        :param out: The output queue.
        :return: Returns the output queue.
        """
        if inp:
            out.extend(inp)
            return out

        if not self.args:
            out.append(input())
            return out

        for path in self.args:
            if path == "-":
                out.append(input())
                continue
            paths = glob(path)
            if not paths:
                raise AppRunException(
                    "cat",
                    f"{path} No such file or directory \
                :/",
                )
            out.extend(self._run(paths))
        return out

    def _run(self, paths):
        """
        Reads all the contents in the given list of paths.
        :param paths: The paths to read from.
        :return out: The text of all the files.
        """
        out = []
        for path in paths:
            contents = map(str.strip, read_lines_from_file(path, "tail"))
            out.extend(contents)
        return out

    def validate_args(self):
        """
        Ensures the options are valid.
        :raises AppRunException: If any option is given.
        """
        for option in self.options:
            raise AppRunException("cat", f"{option}: is an unsupported option \
            :(")
