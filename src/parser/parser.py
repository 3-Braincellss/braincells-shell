from lark import Lark


def run_parser(text):
    with open("grammar.lark", encoding="utf-8") as grammar:
        LP = Lark(grammar.read(), start="sentence")

    tree = LP.parse(text)
    return tree
