from apps.app import App
from exceptions.app_run import AppRunException
from getopt import getopt


class CutApp(App):
    """
    """

    def __init__(self, args):
        self.options, self.args = getopt(args, "b:")
        pass

    def run(self, inp, out):
        """
        """
        ## TODO: implement cutting out bytes from specified ranges
        self._get_ranges()
        out.append(self.args)
        return out

    def _get_ranges(self):
        string_ranges = self.options[0][1].split(",")
        ranges = []
        for range in string_ranges:
            if "-" in range:
                ranges.append(self._get_range(range))
            else:
                ranges.append(self._get_singleton(range)) ## TODO: implement this
        print(ranges)
        return ranges

    def _get_range(self, range):
        try:
            start, end = new_range.split("-")
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
        return new_range

    def _get_boundary(self, num, is_end):
        if num == "" and is_end:
            return "end"
        if num == "" and not is_end:
            return 0
        if not self._validate_int(num):
            raise ValueError
        return int(num)

    def _validate_int(self, num):
        digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for char in num:
            if char not in digits:
                return False
        return True

    def validate_args(self):
        if not self.options:
            raise AppRunException(
                "cut", "Missing option: -b byte_cut_start-byte_cut_end,.. >=[")
        if len(self.options) != 1:
            raise AppRunException("cut", "Invalid number of options >=[")
        if self.options[0][0] != '-b':
            raise AppRunException(
                "cut", f"Invalid option: {self.options[0][0]}")
