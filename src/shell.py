"""
Shell
=====

Contains the execute function to run shell on a given input string.
"""

from collections import deque

from shellparser import run_parser

__all__ = [
    "execute",
]


def execute(input_str):
    """Parses and executes the input string

    Parameters:
        input_str (:obj:`str`): input string representing a command.

    Returns:
        (:obj:`str`): output as a string
    """

    out = deque()
    out_str = ""
    if len(input_str.strip()) != 0:
        command = run_parser(input_str)
        out = command.run(None, out)
        out_str = "\n".join(out)

    return out_str
