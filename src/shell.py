from lark import Lark
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
            #Create parse tree from input
            grammar = Lark.open(self.PATH_TO_GRAMMAR)
            abstract_tree = grammar.parse(text)
            #Decorate tree with transformer
            #Execute
            print(text)


if __name__ == "__main__":
    sh = Shell()
    sh.run()
