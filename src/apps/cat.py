from apps.app import App
from getopt import getopt
from glob import glob
from exceptions.app_run import AppRunException
class CatApp(App):
    """
    """

    allowed_options = {}

    def __init__(self, args):
        self.options, self.args = getopt(args, "")
        pass

    def run(self, inp, out):
        """
        Executes that cat command on the given arguments.
        :param inp: The input args of the command, only used for piping
        and redirects.
        :param out: The output queue.
        :return: Returns the output queue.
        """
        if inp:
            self.args = inp.split(" ")
        if not self.args:
            return input()
        for path in self.args:
            if path == "-":
                out.append(input())
                continue
            paths = glob(path)
            if not paths:
                raise AppRunException("cat", f"{path} No such file or directory :/")
            out.append(self._run(paths))
        return out

    def _run(self,paths):
        out = ""
        for path in paths:
            try:
                with open(path, "r") as f:
                    out += f.read()
            except IsADirectoryError:
                raise AppRunException("cat", f"{path}: Is a directory")
        return out



    def validate_args(self):

        pass
