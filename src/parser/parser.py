from lark import Lark


def run_parser(text):
    with open("parser/grammar.lark", encoding="utf-8") as grammar:
        LP = Lark(grammar.read(), start="command")

    tree = LP.parse(text)
    return tree
