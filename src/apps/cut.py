from apps import App
from getopt import getopt
from exceptions import RunError, ContextError
from common.tools import read_from_file, read_lines_from_file


class CutApp(App):
    """
    Executes bash application cut:
    cut -b [INTERVALS] [PATHS]*
    If paths is empty or '-' stdin is used
    """

    def __init__(self, args):
        self.options, self.args = getopt(args, "b:")

    def run(self, inp, out):
        """
        Executes the cut command extracting specified bytes from text.
        :param inp: The string text to cut bytes from.
        :param out: The deque used to store the result of the application
        """

        intervals = self._get_intervals()
        if inp:
            self._run(inp, intervals, out)
            return out
        elif not self.args:
            self._run([input()], intervals, out)
            return out
        for arg in self.args:
            if arg == "-":
                self._run([input()], intervals, out)
            else:
                contents = read_lines_from_file(arg, "cut")
                self._run(contents, intervals, out)
        return out

    def _run(self, strings, intervals, out):
        """
        Extracts bytes from each string in "strings".
        :param strings: All the strings that the cut app will be used on.
        :intervals: The intervals of the strings that should be extracted.
        :param out: The deque where all resultant strings are stored.
        """
        for string in strings:
            cut_str = self._cut_from_string(string, intervals).rstrip()
            out.append(cut_str)

    def _cut_from_string(self, string, intervals):
        """
        Creates a new string only consisting of the specified intervals.
        :param string: The string to extract bytes from.
        :param intervals: The of the string to be included in the new string.
        :return new_string: The string with extracted bytes.
        """
        new_string = ""
        new_intervals = self._unfold(intervals, len(string))
        for i in range(len(string)):
            if i + 1 in new_intervals:
                new_string += string[i]
        return new_string

    def _unfold(self, intervals, length):
        """
        Takes in a list of intervals and spreads them out to a set of integers.
        :param intervals: The intervals to be unfolded.
        :param length: The length of the string.
        :returns new_intervals: A set consisting of all byte intervals that
        should be extracted from the string
        """
        new_intervals = set()
        for interval in intervals:
            if isinstance(interval, list):
                low = interval[0]
                if interval[1] == "end":
                    high = length
                else:
                    high = interval[1]
                for i in range(low, high + 1):
                    new_intervals.add(i)
            else:
                new_intervals.add(interval)
        return new_intervals

    def _get_intervals(self):
        """
        Splits the intervals given as a string into a list of intervals.
        """
        string_intervals = self.options[0][1].split(",")
        intervals = []
        for interval in string_intervals:
            if "-" in interval:
                intervals.append(self._get_interval(interval))
            else:
                self._validate_int(interval)
                intervals.append(int(interval))
        return intervals

    def _get_interval(self, interval):
        """
        Converts an interval into a tuple consisting of ints or 'end'
        :param interval: The interval being converted into a tuple.
        :raises AppRunException: If an interval is invalid.
        :returns new_interval: The new interval
        """
        try:
            start, end = interval.split("-")
        except ValueError:
            raise RunError("cut", f"Invalid option argument: {interval}")
        new_interval = []
        try:
            new_interval.append(self._get_boundary(start, False))
        except ValueError:
            raise RunError("cut", f"Invalid interval value: {start}")
        try:
            new_interval.append(self._get_boundary(end, True))
        except ValueError:
            raise RunError("cut", f"Invalid interval value: {end}")
        self._validate_interval(new_interval)
        return new_interval

    def _get_boundary(self, num, is_end):
        """
        Converts a string interval value into an int or the string "end"
        :param num: The value to be converted.
        :param is_end: Whether or not the interval value is the last element of
        the interval
        :returns num: The converted value.
        """
        if num == "" and is_end:
            return "end"
        if num == "" and not is_end:
            return 1
        self._validate_int(num)
        return int(num)

    def _validate_int(self, num):
        """
        Determines whether a number can be represented as a positive integer.
        :param num: The string to be checked.
        :raises AppRunException: If the string given is invalid (not a positive
        integer)
        """
        digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        for char in num:
            if char not in digits:
                raise RunError("cut", "Invalid option argument {num}")
        if num == "0":
            raise RunError("cut", "Cut intervals are 1 indexed.")

    def _validate_interval(self, interval):
        """
        Ensures the interval is increasing.
        :param interval: The interval to be checked.
        :raises AppRunException: If the interval is not increasing
        """
        if interval[1] != "end" and interval[0] > interval[1]:
            raise RunError(
                "cut", f"Invalid decreasing interval: {interval[0]}-{interval[1]}"
            )

    def validate_args(self):
        """
        Ensures the options are valid.
        :raises AppRunException: If -b option is missing or -b is not the only
        option.
        """
        if not self.options:
            raise ContextError("cut", "Missing option: -b [INTERVAL],.. >=[")
        if len(self.options) != 1:
            raise ContextError("cut", "Invalid number of options >=[")
        if self.options[0][0] != "-b":
            raise ContextError("cut", f"Invalid option: {self.options[0][0]}")
