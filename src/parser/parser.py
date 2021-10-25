from lark import Lark

with open("grammar.lark",encoding="utf-8") as grammar:
    LP = Lark(grammar.read(),start="sentence")

tree = LP.parse("cat /path/ & cd /path/")
print(tree.pretty())