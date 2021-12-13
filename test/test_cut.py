import os
import unittest

from hypothesis import given
from hypothesis import strategies as st
from shell_test_interface import ShellTestCase

from apps import CutApp
from common.tools import read_lines_from_file
from exceptions import ContextError, RunError

IPSUM_MAX = 592
TEST_TEXT_PATH = "./dir_files/file-5"


class TestCut(ShellTestCase):
    @given(st.integers(1, IPSUM_MAX), st.integers(1, IPSUM_MAX))
    def test_cut(self, x, y):
        interval = (min(x, y), max(x, y))
        lines = read_lines_from_file(TEST_TEXT_PATH, "cut_test")
        expected = [
            (lambda line: line[interval[0] - 1:interval[1]].rstrip())(line)
            for line in lines
        ]
        args = ["-b", f"{interval[0]}-{interval[1]}", TEST_TEXT_PATH]
        app = CutApp(args)
        out = []
        out = app.run(None, out)
        self.assertEqual(out, expected)

    @given(st.integers(1, IPSUM_MAX))
    def test_cut_open_start_interval(self, x):
        lines = read_lines_from_file(TEST_TEXT_PATH, "cut_test")
        expected = [(lambda line: line[:x].rstrip())(line) for line in lines]
        args = ["-b", f"-{x}", TEST_TEXT_PATH]
        app = CutApp(args)
        out = []
        out = app.run(None, out)
        self.assertEqual(out, expected)

    @given(st.integers(1, IPSUM_MAX))
    def test_cut_open_end_interval(self, x):
        lines = read_lines_from_file(TEST_TEXT_PATH, "cut_test")
        expected = [(lambda line: line[x - 1:].rstrip())(line)
                    for line in lines]
        args = ["-b", f"{x}-", TEST_TEXT_PATH]
        app = CutApp(args)
        out = []
        out = app.run(None, out)
        self.assertEqual(out, expected)

    @given(
        st.lists(st.integers(1, IPSUM_MAX),
                 min_size=1,
                 max_size=IPSUM_MAX,
                 unique=True))
    def test_cut_individual_interval(self, x):
        string_intervals = [str(val) for val in x]
        lines = read_lines_from_file(TEST_TEXT_PATH, "cut_test")

        expected = self.my_cut(lines, set(x))

        args = ["-b", f"{','.join(string_intervals)}", TEST_TEXT_PATH]
        out = []
        CutApp(args).run(None, out)
        self.assertEqual(out, expected)

    def test_cut_open_interval(self):
        lines = read_lines_from_file(TEST_TEXT_PATH, "cut_test")
        expected = [(lambda line: line.rstrip())(line) for line in lines]
        args = ["-b", "-", TEST_TEXT_PATH]
        app = CutApp(args)
        out = []
        out = app.run(None, out)
        self.assertEqual(out, expected)

    @given(st.integers(1, IPSUM_MAX), st.integers(1, IPSUM_MAX))
    def test_cut_input_redirection(self, x, y):
        interval = (min(x, y), max(x, y))
        lines = read_lines_from_file(TEST_TEXT_PATH, "cut_test")
        expected = [
            (lambda line: line[interval[0] - 1:interval[1]].rstrip())(line)
            for line in lines
        ]
        args = ["-b", f"{interval[0]}-{interval[1]}"]
        app = CutApp(args)
        out = []
        out = app.run(lines, out)
        self.assertEqual(out, expected)

    @given(st.integers(1, IPSUM_MAX), st.integers(1, IPSUM_MAX))
    def test_decreasing_interval_raises_exception(self, x, y):
        if x == y:
            return
        interval = (max(x, y), min(x, y))
        args = ["-b", f"{interval[0]}-{interval[1]}", TEST_TEXT_PATH]
        app = CutApp(args)
        with self.assertRaises(RunError):
            app.run(None, [])

    @given(st.integers(1, IPSUM_MAX), st.integers(1, IPSUM_MAX),
           st.integers(1, IPSUM_MAX))
    def test_invalid_interval_raises_exception(self, x, y, z):
        if x == y:
            return
        interval = [x, y, z]
        args = [
            "-b", f"{interval[0]}-{interval[1]}-{interval[2]}", TEST_TEXT_PATH
        ]
        app = CutApp(args)
        with self.assertRaises(RunError):
            app.run(None, [])

    @given(st.integers(1, IPSUM_MAX), st.floats(1, IPSUM_MAX))
    def test_non_int_interval_raises_exception(self, x, y):
        if x == y:
            return
        interval = (min(x, y), max(x, y))
        args = ["-b", f"{interval[0]}-{interval[1]}", TEST_TEXT_PATH]
        app = CutApp(args)
        with self.assertRaises(RunError):
            app.run(None, [])

    @given(st.integers(0, 0), st.integers(1, IPSUM_MAX))
    def test_interval_starting_with_zero_raises_exception(self, x, y):
        if x == y:
            return
        interval = (x, y)
        args = ["-b", f"{interval[0]}-{interval[1]}", TEST_TEXT_PATH]
        app = CutApp(args)
        with self.assertRaises(RunError):
            app.run(None, [])

    @given(st.from_regex("(-(A|a|[c-z]|[C-Z]))|(^(?![\s\S]))", fullmatch=True))
    def test_invalid_option_raises_exception(self, char):
        args = [f"{char}", f"{0}-{10}", TEST_TEXT_PATH]
        with self.assertRaises(ContextError):
            CutApp(args).validate_args()

    @staticmethod
    def my_cut(lines, intervals):
        out = []
        for line in lines:
            str = ""
            for pos, char in enumerate(line):
                if pos + 1 in intervals:
                    str += char
            out.append(str.rstrip())
        return out
