from apps.app import App
import os
from glob import glob
from getopt import getopt
from exceptions import AppRunException


class FindApp(App):
    """
    """

    def __init__(self, args):
        self.options, self.args = getopt(args, "name:")
        print(self.args)

    def run(self, inp, out):
        """
        """
        root = os.getcwd() if self.args is None else self.args[0]
        self.pattern = self.options[0][1]
        self._run(root, out)
        return out

    def _run(self, root, out):
        matched_files = glob(root+"/"+self.pattern, recursive=True)
        for file in matched_files:
            out.append(file)

    def validate_args(self):
        if not self.options:
            raise AppRunException("find", "No pattern supplied. usage: find \
            [PATH] -name PATTERN ")
        if len(self.args) > 1:
            raise AppRunException("find", "Too many arguments supplied usage: \
            find [PATH] -name PATTERN")
