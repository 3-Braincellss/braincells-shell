from operations.operation import Operation

"""
Standard pipe that redirects the output of one program to the input of another.
"""


class Pipe(Operation):
    def __init__(self, cm1, cm2):
        self.cm1 = cm1
        self.cm2 = cm2

    def run(self, inp):
        out = self.cm1.run(inp)
        return self.cm2.run(out)
