from apps.app import App
import os

class PwdApp(App):
    """
    """

    def __init__(self, args):
        ## TODO: handle options 
        pass

    def run(self, inp):
        """
        """
        return os.path.abspath(".") + "\n"

    def validate_args(self):

        pass
