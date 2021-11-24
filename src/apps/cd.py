"""
This module represents the cd bash command
"""
import os

from apps import App
from exceptions import AppContextException, AppRunException


class CdApp(App):
    """
    Application representing the bash command:
    cd [DIRECTORY]
    """

    def __init__(self, args):
        self.args = args

    def run(self, inp, out):
        """
        Changes current working directory

        If a FULL DIRECTORY is supplied changes current directory to the given
        one

        If a RELATIVE DIRECTORY is supplied changed current directory to the
        given one

        If NO DIRECTORY is given changes directory to the root
        """
        if len(self.args) == 0:
            os.chdir("/")
        else:
            try:
                os.chdir(self.args[0])
            except OSError:
                raise AppRunException("cd", f"{self.args[0]} is not a directory\
                .")
        return out

    def validate_args(self):
        """
        Check that the number of arguments is greater than 1
        and if the given path exists.
        """

        if len(self.args) > 1:
            raise AppContextException("cd", "Wrong number of arguments")
        if not os.path.exists(self.args[0]):
            raise AppContextException("cd", f"path '{self.args[0]}' doesn't \
            exist")
