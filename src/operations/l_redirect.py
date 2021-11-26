import os

from operations import Operation
from collections import deque


class LeftRedirect(Operation):
    def __init__(self, fname, cm):
        self.fname = fname
        self.cm = cm

    def run(self, inp, out):
        if os.path.isfile(fname):


    
