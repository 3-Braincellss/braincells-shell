from lark import Lark
from lark.exceptions import VisitError
from parser import parser

from exceptions.app_not_found import AppNotFoundException
from exceptions.app_context import AppContextException
from exceptions.app_run import AppRunException
from common.tools import prettify_path

import sys
import os

"""
Shell class where the code execution starts.
All major "Shell" logic happens here.
"""


class Shell:
    PREFIX = "~~> "
    PATH_TO_GRAMMAR = "./parser/grammar.lark"

    def __init__(self):

        pass

    """ Starts up the shell """

    def run(self, command=None):
        if command:
            out = self.execute(command)
            print(out)
        else:
            while True:
                print(prettify_path(os.getcwd()) + " " + self.PREFIX, end="")
                text = input()
                try:
                    out = self.execute(text)
                    print(out, end="")
                except AppNotFoundException as anfe:
                    print(anfe.message)
                except AppContextException as ace:
                    print(ace.message)
                except AppRunException as are:
                    print(are.message)

    def execute(self, input_str):
        # Create parse tree from input
        try:
            command = parser.run_parser(input_str)
            output = command.run(None)
            return output
        except VisitError as ve:
            if isinstance(ve.__context__, AppNotFoundException):
                raise ve.__context__
            if isinstance(ve.__context__, AppContextException):
                raise ve.__context__
            else:
                raise ve
        except AppRunException as are:
            raise are


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
