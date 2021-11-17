from apps.app import App
from exceptions.app_run import AppRunException
from getopt import getopt
from common.tools import read_from_file, read_lines_from_file


class CutApp(App):
    """
    """

    def __init__(self, args):
        self.options, self.args = getopt(args, "b:")

    def run(self, inp, out):
        """
        """
        if inp:
            self.options, self.args = getopt(args, "b:")
        positions = self._get_positions()
        if not self.args:
            out.append(self._cut_from_string(input(), positions))
            return out
        for arg in self.args:
            if arg == "-":
                cut_str = (self._cut_from_string(input(), positions))
            else:
                contents = read_lines_from_file(arg, "cut")
                self._run(contents, positions, out)
        return out


    def _run(self, strings, positions, out):
        new_string = ""
        for string in strings:
            cut_str = self._cut_from_string(string, positions)
            if cut_str != "":
                out.append(cut_str)
        return new_string

    def _cut_from_string(self, string, positions):
        new_string = ""
        new_positions = self._unfold(positions, len(string))
        for i in range(len(string)):
            if i+1 in new_positions:
                new_string +=  string[i]
        return new_string

    def _unfold(self, positions, length):
        new_ranges = set()
        for position in positions:
            if isinstance(position, list):
                if position[1] == "end":
                    position[1] = length
                for i in range(position[0], position[1]+1):
                    new_ranges.add(i)
            else:
                new_ranges.add(position)
        return new_ranges

    def _get_positions(self):
        string_ranges = self.options[0][1].split(",")
        positions = []
        for range in string_ranges:
            if "-" in range:
                positions.append(self._get_range(range))
            else:
                positions.append(self._get_singleton(range))
        return positions

    def _get_range(self, range):
        try:
            start, end = range.split("-")
        except ValueError:
            raise AppRunException("cut", f"Invalid option argument: {range}")
        new_range = []
        try:
            new_range.append(self._get_boundary(start, False))
        except ValueError:
            raise AppRunException("cut", f"Invalid range value: {start}")
        try:
            new_range.append(self._get_boundary(end, True))
        except ValueError:
            raise AppRunException("cut", f"Invalid range value: {end}")
        return self._validate_range(new_range)

    def _get_boundary(self, num, is_end):
        if num == "" and is_end:
            return "end"
        if num == "" and not is_end:
            return 1
        self._validate_int(num)
        return int(num)

    def _get_singleton(self, num):
        self._validate_int(num)
        return int(num)

    def _validate_int(self, num):
        digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        for char in num:
            if char not in digits:
                raise AppRunException("cut", "Invalid option argument {num}")
        if num == "0":
            raise AppRunException("cut", "Cut ranges are 1 indexed.")

    def _validate_range(self, vals):
        if vals[1] != "end" and vals[0] > vals[1]:
            raise AppRunException(
                "cut", f"Invalid decreasing range: {vals[0]}-{vals[1]}")
        return vals

    def validate_args(self):
        if not self.options:
            raise AppRunException(
                "cut", "Missing option: -b [RANGE],.. >=[")
        if len(self.options) != 1:
            raise AppRunException("cut", "Invalid number of options >=[")
        if self.options[0][0] != '-b':
            raise AppRunException(
                "cut", f"Invalid option: {self.options[0][0]}")
