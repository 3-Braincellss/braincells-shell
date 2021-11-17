from apps.app import App
from exceptions.app_context import AppContextException
from exceptions.app_run import AppRunException
import os

class PwdApp(App):
    """
    """

    allowed_options = {"-L", "-P"}

    def __init__(self, args):
        ## TODO: handle options
        self.args = args
        pass

    def run(self, inp):
        """
        """
        self.validate_args()
        return os.path.abspath(".") + "\n"

    def validate_args(self):
        for option in self.args:
            if option not in PwdApp.allowed_options:
                raise AppRunException("pwd", f"{option}: invalid option")
