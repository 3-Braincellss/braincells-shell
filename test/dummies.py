"""
Dummies
=======

In order to test modules independently of conrete implementations
We have created a set of dummy classes that will help focusing
our testing on specific parts of our code.
"""

from collections import deque

from apps import App
from commands import Command


class DummyCommand(Command):
    """A dummy Operation"""
    def __init__(self, custom_output: deque = None):
        self.custom_output = custom_output

    def run(self, inp, out):
        """ Will just extend output by provided input
        
        Will also output whatever was passed with the
        custom output during the initialisation.
        """
        if self.custom_output is not None:
            out.extend(self.custom_output)

        if inp:
            out.extend(inp)

        return out


class DummyApp(App):
    """DummyApp class made to make Call
    independent of the App class
    """
    def __init__(self):
        pass

    def run(self, inp, out):
        """ Will just extend output by provided input"""
        if inp:
            out.extend(inp)
        return out

    def validate_args(self):
        """ Doesn't raise any errors"""
        return
