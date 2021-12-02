from apps.app import App
import os
from glob import glob
from getopt import gnu_getopt
from exceptions import RunError, ContextError


class FindApp(App):
    """ """

    def __init__(self, args):
        for i in range(len(args)):
            if args[i] == "-name":
                args[i] = "--name"
                break
        self.options, self.args = gnu_getopt(args, "", ["name="])

    def run(self, inp, out):
        """ """
        root = "" if not self.args else self.args[0]
        self.pattern = self.options[0][1]
        self._run(root, out)
        return out

    def _run(self, root, out):
        try:
            matched_files = glob(f"./{root}/**/{self.pattern}", recursive=True)
        except OSError:
            raise RunError("find", f"{root}: No such file or directory")
        for file in matched_files:
            if not os.path.isdir(file):
                if root != "":
                    out.append(file[2:])  # Omit the ./
                else:
                    out.append(file)

    def validate_args(self):
        if not self.options:
            raise ContextError(
                "find",
                "No pattern supplied. usage: find \
            [PATH] -name PATTERN ",
            )
        if len(self.args) > 1:
            raise ContextError(
                "find",
                "Too many arguments supplied usage: \
            find [PATH] -name PATTERN",
            )
