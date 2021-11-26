import os

from lark import Lark
from lark.visitors import Transformer

from operations import OperationFactory
from exceptions import AppNotFoundException, AppContextException



class ShellTransformer(Transformer):
    UNQUOTED = str
    DOUBLE_QUOTE_CONTENT = str
    BACKQUOTED = str

    def command(self, args):
        returnargs = [x for x in args if x is not None]
        return returnargs
    
    def seq(self, args):
        op_factory = OperationFactory()
        data = {"op1": args[0][0], "op2": args[1][0]}
        try:
            seq = op_factory.get_operation("seq", data)
            return seq
        except AppNotFoundException as anfe:
            raise anfe
        except AppContextException as ace:
            raise ace

    def pipe(self, args):
        op_factory = OperationFactory()
        data = {"op1": args[0], "op2": args[1]}
        try:
            pipe = op_factory.get_operation("pipe", data)
            return pipe
        except AppNotFoundException as anfe:
            raise anfe
        except AppContextException as ace:
            raise ace

    def call(self, args):
        returnargs = [x for x in args if x is not None]
        op_factory = OperationFactory()
        data = {"app": returnargs[0], "args": returnargs[1]}
        try:
            call = op_factory.get_operation("call", data)
            return call
        except AppNotFoundException as anfe:
            raise anfe
        except AppContextException as ace:
            raise ace

    def arguments(self, args):
        returnargs = [x for x in args if x is not None]
        return "".join(returnargs)
    
    def quoted(self, args):
        return args[0]

    def double_quoted(self, args):

        returnargs = [x for x in args if x is not None]
        return "".join(returnargs)
    
    def single_quoted(self, args):
        returnargs = [x for x in args if x is not None]
        return "".join(returnargs)

    def back_quoted(self, args):
        from shell import Shell

        s = Shell()
        thing = "".join(s.execute(args[0])).strip()
        return thing

    def WHITESPACE(self, tok):
        pass
    


def run_parser(text):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "grammar.lark")
    with open(filename, encoding="utf-8") as grammar:

        lark_parser = Lark(grammar.read(), start="command")

    tree = lark_parser.parse(text)
    return ShellTransformer(visit_tokens=True).transform(tree)
