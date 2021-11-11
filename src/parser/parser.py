from lark import Lark
from lark.visitors import Transformer

class T(Transformer):
    UNQUOTED = str
    WHITESPACE = str

    def call_body(self, args):
        print(args[0])
        pass




def run_parser(text):
    with open("parser/grammar.lark", encoding="utf-8") as grammar:
        LP = Lark(grammar.read(), start="command")

    tree = LP.parse(text)
    print(tree)
    print()
    print(T(visit_tokens=True).transform(tree))
    return tree
