from lark import Lark
from parser import parser
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
            print(out, end="")
        else:
            while True:
                print(self.PREFIX, end="")
                text = input()
                out = self.execute(text)
                print(out)

    def execute(self, input_str):
        # Create parse tree from input

        command = parser.run_parser(input_str)
        # Decorate tree with transformer
        # Execute

        return command.run(None)


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
