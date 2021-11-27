import os
from typing import Tuple

from lark import Lark
from lark.visitors import Transformer

from operations import OperationFactory


class ShellTransformer(Transformer):
    UNQUOTED = str
    DOUBLE_QUOTE_CONTENT = str
    BACKQUOTED = str

    def command(self, args):
        returnargs = [x for x in args if x is not None]
        return returnargs

    def seq(self, args):
        data = {"op1": args[0][0], "op2": args[1][0]}
        seq = OperationFactory.get_operation("seq", data)

        return seq

    def pipe(self, args):

        data = {"op1": args[0], "op2": args[1]}
        pipe = OperationFactory.get_operation("pipe", data)

        return pipe
    
    def redirection(self, args):
        return args[0]
    def l_redirection(self, args):
        returnargs = [x for x in args if x is not None]
        return ("left_red", returnargs[0])
    def r_redirection(self, args):
        returnargs = [x for x in args if x is not None]
        return ("right_red", returnargs[0])

    def call(self, args):
        print(args)
        returnargs = [x for x in args if x is not None and not isinstance(x, tuple)]
        right_string = [x for x in args if x is not None and isinstance(x, tuple) and x[0] == 'right_red']
        left_string = [x for x in args if x is not None and isinstance(x, tuple) and x[0] == 'left_red']

        if (len(right_string) != 0):
            right_red = right_string[0][1]
        else:
            right_red = None

        if (len(left_string) != 0):
            left_red = left_string[0][1]
        else: 
            left_red = None

        data = {
            "app": returnargs[0], 
            "args": returnargs[1:], 
            "left_red": left_red, 
            "right_red": right_red
        }
        call = OperationFactory.get_operation("call", data)

        return call

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
        thing = " ".join(s.execute(args[0])).strip()
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
