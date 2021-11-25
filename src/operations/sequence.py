from operations.operation import Operation

"""
Sequence operation denoted as ';' will sequentially call 2 commands in a row.

"""


class Sequence(Operation):
    def __init__(self, cm1, cm2):
        self.cm1 = cm1
        self.cm2 = cm2

    def run(self, inp, out):

        # None is passed since it's impossible to pass an input to a sequence
        out = self.cm1.run(None, out)
        return self.cm2.run(None, out)
