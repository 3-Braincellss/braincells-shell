from apps.app import App
import os
from glob import glob
from getopt import getopt
from exceptions import AppRunException


class FindApp(App):
    """
    """

    def __init__(self, args):
        if args:
            args[0] = "-"+args[0]
        self.options, self.args = getopt(args, "", ["name="])

    def run(self, inp, out):
        """
        """
        root = None if not self.args else self.args[0]
        self.pattern = self.options[0][1]
        self._run(root, out)
        return out

    def _run(self, root, out):
        original_path = os.getcwd()
        try:
            if root:
                os.chdir(root)
        except OSError:
            raise AppRunException("find", f"{root}: No such file or directory")
        matched_files = glob(f"**/{self.pattern}", recursive=True)
        for file in matched_files:
            if not os.path.isdir(file):
                out.append(file)
        os.chdir(original_path)

    def validate_args(self):
        if not self.options:
            raise AppRunException("find", "No pattern supplied. usage: find \
            [PATH] -name PATTERN ")
        if len(self.args) > 1:
            raise AppRunException("find", "Too many arguments supplied usage: \
            find [PATH] -name PATTERN")
