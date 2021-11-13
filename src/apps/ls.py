from apps.app import App
from exceptions.app_context import AppContextException
from exceptions.app_run import AppRunException


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
            if len(ls_dirs) > 1:
                ret = ret + f"{path}:\n\n"
            files = sorted([each for each in os.listdir(path) if each[0] != '.'])
            out.append("\n".join(files) + "\n")
        out.append("\n")
        return out

    def validate_args(self):
        """
        Check is all paths in args exist.
        :raises: AppContextException if the path given does not exist.
        """

        if len(self.args) >= 1:
            for path in self.args:
                if not os.path.exists(path):
                    raise AppContextException("ls", f"path '{path}' does not exist")
