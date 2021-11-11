from lark import Lark
from parser import parser
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

    def run(self):

        while True:
            text = input(self.PREFIX)
            out = self.execute(text)
            print(out)

    def execute(self, input_str):
        #Create parse tree from input

        command = parser.run_parser(input_str)
        #Decorate tree with transformer
        #Execute
        
        return command.run(None)

if __name__ == "__main__":
    sh = Shell()
    sh.run()
