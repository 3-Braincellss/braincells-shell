from lark import Lark
from lark.visitors import Transformer
from operations.operation_factory import OperationFactory
from shell import Shell
import os

grammar = r"""
%import common.LETTER

command : pipe | seq | call
pipe    : call "|" call 
        | pipe "|" call
seq     : command ";" command
call        : WHITESPACE? (redirection WHITESPACE)* arguments (WHITESPACE redirection)* WHITESPACE?
arguments     : word (WHITESPACE word)* 

word    : (quoted | UNQUOTED)
redirection : "<" WHITESPACE word
            | ">" WHITESPACE word

quoted        : single_quoted | double_quoted | BACKQUOTED
double_quoted : "\"" (backquoted_call | DOUBLE_QUOTE_CONTENT)* "\""
backquoted_call    : "`" call "`" 
single_quoted : "'" SINGLE_QUOTE_CONTENT* "'"

BACKQUOTED           : /[`][^\n`]*[`]/
DOUBLE_QUOTE_CONTENT : /[^\n"`]+/
SINGLE_QUOTE_CONTENT : /[^\n']+/
UNQUOTED             : /[^\s"'`\n;|<>]+/
WHITESPACE           : /[\s]+/
"""


class T(Transformer):
    UNQUOTED = str
    DOUBLE_QUOTE_CONTENT = str

    def command(self, args):
        return args[0]

    def call(self, args):
        opFactory = OperationFactory()
        data = {"app": args[0][0], "args": args[0][1]}
        return opFactory.get_operation("call", data)

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

    LP = Lark(grammar, start="command")

    tree = LP.parse(text)
    return T(visit_tokens=True).transform(tree)
