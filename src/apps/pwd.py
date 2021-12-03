"""
pwd
===
"""
from apps.app import App
from exceptions import RunError
import os


class PwdApp(App):
    """ """

    allowed_options = {"-L", "-P"}

    def __init__(self, args):
        ## TODO: handle options
        self.args = args
        pass

    def run(self, inp, out):
        """ """
        self.validate_args()
        out.append(os.path.abspath(".") + "\n")
        return out

    def validate_args(self):
        for option in self.args:
            if option not in PwdApp.allowed_options:
                raise AppContextException("pwd", f"{option}: invalid option")
