"""
Shell class where the code execution starts.
All major "Shell" logic happens here.
"""

from collections import deque
from shellparser import run_parser
import sys
import os

from lark.exceptions import VisitError
from exceptions import AppNotFoundException, AppRunException, AppContextException

from common.tools import prettify_path


class Shell:
    PREFIX = "~~> "

    def __init__(self):
        """Starts up the shell"""
        pass

    def run(self, command=None):
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

                except AppRunException as are:
                    out = deque()
                    out.append(are.message)

                except VisitError as ve:
                    # Lark's Visit error hides all other exceptions in the context
                    # So to check for our defined exceptions we check the context of the visit error
                    if isinstance(
                        ve.__context__,
                        (AppContextException, AppNotFoundException, AppRunException),
                    ):
                        out = deque()
                        out.append(ve.__context__.message)
                    else:
                        raise ve
                        
                while len(out) > 0:
                    print(out.popleft())

    def execute(self, input_str):
        """Create parse tree from input"""
        out = deque()

        command = run_parser(input_str + " ")

        if command:
            out = command[0].run(None, out)

        return out


if __name__ == "__main__":
    args_num = len(sys.argv) - 1
    sh = Shell()
    if args_num > 0:
        if args_num != 2:
            raise ValueError("wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {sys.argv[1]}")

        sh.run(sys.argv[2])
    else:
        sh.run()
