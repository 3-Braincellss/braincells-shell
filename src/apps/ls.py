from apps import App
from exceptions import AppContextException, AppRunException


import os


class LsApp(App):
    """
    Lists all apps in the current or given directory
    """

    def __init__(self, args):
        self.args = args

    def run(self, inp, out):

        """
        ls [DIRECTORY]

        if NO ARGUMENTS provided print files in the current directory

        if ONE OR MORE ARGUMENTS provided print files in directories specified
        """
        out.append("\n")
        if len(self.args) == 0:
            ls_dirs = [os.getcwd()]
        else:
            ls_dirs = self.args

        for path in ls_dirs:
            files = sorted([each for each in os.listdir(path) if each[0] != "."])
            out.append("\n".join(files) + "\n")
        out.append("\n")
        return out

    def validate_args(self):
        """
        Check is all paths in args exist.
        :raises: AppContextException if the path given does not exist.
        """

        if len(self.args) > 1:
            raise AppContextException("ls", "too many arguments")
        if len(self.args) == 1:
            if not os.path.exists(self.args[0]):
                raise AppContextException("ls", f"{self.args[0]}: not a directory")
