from lark import Lark
from lark.visitors import Transformer
from operations.operation_factory import OperationFactory
from shell import Shell

from exceptions.app_not_found import AppNotFoundException
from exceptions.app_context import AppContextException

import os


class T(Transformer):
    UNQUOTED = str
    DOUBLE_QUOTE_CONTENT = str

    def command(self, args):
        return args[0]

    def call(self, args):
        opFactory = OperationFactory()
        data = {"app": args[0][0], "args": args[0][1]}
        try:
            call = opFactory.get_operation("call", data)
            return call
        except AppNotFoundException as anfe:
            raise anfe
        except AppContextException as ace:
            raise ace

    def arguments(self, args):
        returnargs = [x for x in args if x is not None]
        return (returnargs[0], returnargs[1:])

    def word(self, args):
        return args[0]

    def quoted(self, args):
        return args[0]

    def double_quoted(self, args):
        returnargs = [x for x in args if x is not None]
        return "".join(returnargs)

    def backquoted_call(self, args):
        out = args[0].run(None)
        return out

    def WHITESPACE(self, tok):
        pass


def run_parser(text):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "grammar.lark")
    with open(filename, encoding="utf-8") as grammar:

        LP = Lark(grammar.read(), start="command")

    tree = LP.parse(text)
    return T(visit_tokens=True).transform(tree)
