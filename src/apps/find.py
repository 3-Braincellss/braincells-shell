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

    def run(self, inp, out):
        """
        """
        pass

    def validate_args(self):

        pass
