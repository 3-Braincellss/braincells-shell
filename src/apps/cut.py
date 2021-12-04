"""
cut
===
Module representing the cut application
Usage in shell: cut -b [RANGES] [FILES]...

Example:
    `cut -b 0-23 rick-roll.txt`
"""

from getopt import getopt, GetoptError
from apps import App
from exceptions import RunError, ContextError
from common.tools import read_lines_from_file


class CutApp(App):
    """A class representing the cut shell instruction

    Args:
        args (:obj:`list`): Contains all the arguments and options
            of the instruction

    """

    def __init__(self, args):
        super().__init__(args)
        try:
            self.options, self.args = getopt(args, "b:")
        except GetoptError as error:
            raise ContextError("cut", str(error)) from None

    def run(self, inp, out):
        """Executes the cut command on the given arguments.

        Removes the bytes not specified in the -b option.
        If no arguments are given then the bytes are taken from stdin.

        Args:
            inp (:obj:`deque`, *optional*): The input args of the command,
                only used for piping and redirects.
            out (:obj:`deque`): The output deque, used to store
                the result of execution.

        Returns:
            ``deque``: The deque will contain the contents of the file,
                seperated by line after removing bytes.

        Raises:
            RunError: If the intervals specified by the -b option
                are invalid. Or the paths specified do not exist.
        """

        intervals = self._get_intervals()
        if inp:
            self._run(inp, intervals, out)
            return out
        if not self.args:
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
        for pos, char in enumerate(string):
            if pos + 1 in new_intervals:
                new_string += char
        return new_string

    @staticmethod
    def _unfold(intervals, length):
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
        :raises RunError: If an interval is invalid.
        :returns new_interval: The new interval
        """
        try:
            start, end = interval.split("-")
        except ValueError:
            raise RunError(
                "cut", f"Invalid option argument: {interval}") from None

        new_interval = []
        try:
            new_interval.append(self._get_boundary(start, False))
        except ValueError:
            raise RunError("cut", f"Invalid interval value: {start}") from None
        try:
            new_interval.append(self._get_boundary(end, True))
        except ValueError:
            raise RunError("cut", f"Invalid interval value: {end}") from None
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

    @staticmethod
    def _validate_int(num):
        """
        Determines whether a number can be represented as a positive integer.
        :param num: The string to be checked.
        :raises RunError: If the string given is invalid (not a positive
        integer)
        """
        digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        for char in num:
            if char not in digits:
                raise RunError("cut", "Invalid option argument {num}")
        if num == "0":
            raise RunError("cut", "Cut intervals are 1 indexed.")

    @staticmethod
    def _validate_interval(interval):
        """
        Ensures the interval is increasing.
        :param interval: The interval to be checked.
        :raises RunError: If the interval is not increasing
        """
        if interval[1] != "end" and interval[0] > interval[1]:
            raise RunError(
                "cut",
                f"Invalid decreasing interval: {interval[0]}-{interval[1]}")

    def validate_args(self):
        """Ensures the options are valid.

        Raises:
            AppRunException: If -b option is missing.
        """
        if not self.options:
            raise ContextError("cut", "Missing option: -b [INTERVAL],.. >=[")
