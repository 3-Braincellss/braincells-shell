"""
Pipe
====

Pipe command. Denoted as ``|``. Will redirect the output of the first
command as the input to the second.

"""
from collections import deque

from commands import Command

__all__ = [
    "Pipe",
]


class Pipe(Command):
    """Pipe Class

    Attributes:
        op1(Command): A Command that is run first.
            Its output will be piped to the second command.
        op2(Command): A Command that is run second.
            Its input will be the output of the first command.
    """
    def __init__(self, ctx):
        super().__init__(ctx)
        self.op1 = ctx["op1"]
        self.op2 = ctx["op2"]

    def run(self, inp, out):
        out = self.op1.run(inp, out)
        new_out = deque()
        return self.op2.run(out, new_out)
