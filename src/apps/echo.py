"""
This module represents the echo bash command.
"""
from apps.app import App


class EchoApp(App):
    """
    echo [INPUT] [INPUT] ...
    """

    def __init__(self, args):
        self.args = args

    def run(self, inp, out):
        """
        Returns all the input args as a space seperated string.
        """

        out.append(" ".join(self.args))
        return out

    def validate_args(self):
        """
        Checks whether the given arguments are valid.
        """
