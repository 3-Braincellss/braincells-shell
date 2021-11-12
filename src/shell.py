from lark import Lark
from lark.exceptions import VisitError
from parser import parser
from exceptions.app_not_found import AppNotFoundException

import sys

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
                print(self.PREFIX, end="")
                text = input()
                try: 
                    out = self.execute(text)
                    print(out)
                except AppNotFoundException as anfe:
                    print(anfe.message)


    def execute(self, input_str):
        # Create parse tree from input
        try:
            command = parser.run_parser(input_str)
            return command.run(None)
        except VisitError as ve:
            if isinstance(ve.__context__, AppNotFoundException):
                raise ve.__context__
            
            
            

        



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
