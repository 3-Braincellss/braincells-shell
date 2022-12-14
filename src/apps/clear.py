"""
clear
=====

Module representing the clear application.

Usage in shell: ``clear``
"""

import os
from collections import deque

from apps import App
from exceptions import ContextError

__all__ = ["ClearApp"]


class ClearApp(App):
    """A class representing the clear application.

    Args:
        args (:obj:`list`): Contains all the arguments and options of
            the instruction.

    """
    def run(self, inp, out):
        """Clears the terminal"""

        command = "cls" if os.name in ["nt", "dos"] else "clear"

        os.system(command)

        out = deque()

        return out

    def validate_args(self):
        """clear is not expecting any arguments"""
        if self.args:
            raise ContextError("clear", "Too many arguments")
