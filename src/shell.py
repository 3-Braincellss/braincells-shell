"""
Shell class where the code execution starts.
All major "Shell" logic happens here.
"""

import sys
import os

from collections import deque
from lark.exceptions import VisitError

from shellparser import run_parser
from exceptions import AppException
from common.tools import prettify_path


class Shell:
    """Main shell class which can start the execution."""

    PREFIX = "~~> "
    """ String that separates current directory section from user input"""

    def run(self, command=None):
        """Runs the shell.

        This method can be run in 2 ways.
        1) In case no arguments are passed, shell will run in an **interactive mode**.

        2) If a string is passed, then shell will interpret the string as a command,
        execute this command and print output to **stdout**.

        Parameters:
            command (:obj:`str`): a string representation of a command to execute.
        """

        if command:
            out = self.execute(command)
            while len(out) > 0:
                print(out.popleft())
        else:
            while True:
                print(prettify_path(os.getcwd()) + " " + self.PREFIX, end="")
                text = input()

                try:
                    out = self.execute(text)
                except AppException as err:
                    out = deque()
                    out.append(err.message)

                except VisitError as err:
                    # Lark's Visit error hides all other exceptions in the context
                    # So to check for our defined exceptions we check the context of the visit error
                    if isinstance(err.__context__, AppException):
                        out = deque()
                        out.append(err.__context__.message)
                    else:
                        raise err

                while len(out) > 0:
                    print(out.popleft())

    @staticmethod
    def execute(input_str):
        """Create parse tree from input"""
        out = deque()

        command = run_parser(input_str + " ")

        if command:
            out = command[0].run(None, out)

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
