"""
Shell
=====

Shell module where the code execution starts.
All major "Shell" logic happens here.
"""

import sys
import os
import getpass
import socket

from collections import deque
from lark.exceptions import VisitError

from shellparser import run_parser
from exceptions import ShellError
from common.tools import prettify_path


class Shell:
    @staticmethod
    def execute(input_str):
        """Parses and executes the input string

        Parameters:
            input_str (:obj:`str`): input string representing a command.

        Returns:
            ``deque``: a deque object each value of which is a single line
            of the output.

        Raises:
            ShellError: in case parsing fails, our a command cannot be run.
        """

        out = deque()

        command = run_parser(input_str + " ")
        if command:
            out = command.run(None, out)

        return out


if __name__ == "__main__":
    ARGS_NUM = len(sys.argv) - 1
    sh = Shell()
    if ARGS_NUM > 0:
        if ARGS_NUM != 2:
            raise ValueError("wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {sys.argv[1]}")

        sh.run(sys.argv[2])
    else:
        sh.run()
