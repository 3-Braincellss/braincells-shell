from operations.operation import Operation

"""
Sequence operation denoted as ';' will sequentially call 2 commands in a row.

"""


class Sequence(Operation):
    def __init__(self, data):
        self.op1 = data["op1"]
        self.op2 = data["op2"]

    def run(self, inp, out):

        # None is passed since it's impossible to pass an input to a sequence
        out = self.op1.run(None, out)
        return self.op2.run(None, out)
