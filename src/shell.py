"""
Shell
=====

Contains the execute function to run shell on a given input string.
"""

from collections import deque

from parser import ShellParser, CommandTransformer

__all__ = [
    "Shell",
]



class Shell:
    """ Main shell class

    Initialises parser and transformer instances.

    """

    def __init__(self):
        self.parser = ShellParser()
        self.transformer = CommandTransformer(visit_tokens=True)

        
    def execute(self, input_str):
        """Parses and executes the input string

        Parameters:
            input_str (:obj:`str`): input string representing a command.

        Returns:
            (:obj:`str`): output as a string
        """

        out = deque()
        out_str = ""
        if len(input_str.strip()) != 0:
            tree = self.parser.parse(input_str)
            command = self.transformer.transform(tree)
            out = command.run(None, out)
            out_str = "\n".join(out)
            
        return out_str
