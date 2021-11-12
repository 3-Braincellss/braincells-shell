from apps.app import App
from exceptions.app_context import AppContextException

import os


class CdApp(App):
    """
    Changes current working directory
    """

    def __init__(self, args):
        self.args = args

    def run(self, inp):
        """
        cd [DIRECTORY]

        If a FULL DIRECTORY is supplied changes current directory to the given one

        If a RELATIVE DIRECTORY is supplied changed current directory to the given one

        If NO DIRECTORY is given changes directory to the root
        """
        if len(self.args) == 0:
            os.chdir("/")
        else:
            os.chdir(self.args[0])
        return ""

    def validate_args(self):
        """
        Check that the number of arguments is greater than 1.

        Check that the path exists
        """

        if len(self.args) > 1:
            raise AppContextException("cd", "Wrong number of arguments")
        elif len(self.args) == 1:
            if not os.path.exists(self.args[0]):
                raise AppContextException("cd", f"path '{self.args[0]}' doesn't exist")
