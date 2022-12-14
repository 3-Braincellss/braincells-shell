"""
Sequence
========

Sequence command denoted as ``;`` will sequentially call 2 commands in a row.
"""
from commands import Command

__all__ = [
    "Sequence",
]


class Sequence(Command):
    """Sequence Class

    Attributes:
        op1(Command): Command that is run first.
        op2(Command): Command that is run second.
    """
    def __init__(self, ctx):
        super().__init__(ctx)
        self.op1 = ctx["op1"]
        self.op2 = ctx["op2"]

    def run(self, inp, out):
        """Runs 2 commands in sequence.

        Each command runs with an empty input.
        """

        # None is passed since it's impossible to pass an input to a sequence

        out = self.op1.run(None, out)
        out = self.op2.run(None, out)
        return out
