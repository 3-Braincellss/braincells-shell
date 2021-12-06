from hypothesis import given, strategies as st
import unittest
from apps import CutApp
from common.tools import read_lines_from_file
from exceptions import RunError, ContextError

IPSUM_MAX = 592


class TestCut(unittest.TestCase):

    @given(st.integers(1, IPSUM_MAX), st.integers(1, IPSUM_MAX))
    def test_cut(self, x, y):
        interval = (min(x, y), max(x, y))
        lines = read_lines_from_file("lorem_ipsum.txt", "cut_test")
        expected = [(lambda line: line[interval[0] - 1:interval[1]].rstrip())(line)
                    for line in lines]
        args = ["-b", f"{interval[0]}-{interval[1]}", "lorem_ipsum.txt"]
        app = CutApp(args)
        out = []
        out = app.run(None, out)
        self.assertEqual(out, expected)

    @given(st.integers(1, IPSUM_MAX))
    def test_cut_open_start_interval(self, x):
        lines = read_lines_from_file("lorem_ipsum.txt", "cut_test")
        expected = [(lambda line: line[:x].rstrip())(line)
                    for line in lines]
        args = ["-b", f"-{x}", "lorem_ipsum.txt"]
        app = CutApp(args)
        out = []
        out = app.run(None, out)
        self.assertEqual(out, expected)

    @given(st.integers(1, IPSUM_MAX))
    def test_cut_open_end_interval(self, x):
        lines = read_lines_from_file("lorem_ipsum.txt", "cut_test")
        expected = [(lambda line: line[x - 1:].rstrip())(line)
                    for line in lines]
        args = ["-b", f"{x}-", "lorem_ipsum.txt"]
        app = CutApp(args)
        out = []
        out = app.run(None, out)
        self.assertEqual(out, expected)

    def test_cut_open_interval(self):
        lines = read_lines_from_file("lorem_ipsum.txt", "cut_test")
        expected = [(lambda line: line.rstrip())(line)
                    for line in lines]
        args = ["-b", "-", "lorem_ipsum.txt"]
        app = CutApp(args)
        out = []
        out = app.run(None, out)
        self.assertEqual(out, expected)

    @given(st.integers(1, IPSUM_MAX), st.integers(1, IPSUM_MAX))
    def test_cut_input_redirection(self, x, y):
        interval = (min(x, y), max(x, y))
        lines = read_lines_from_file("lorem_ipsum.txt", "cut_test")
        expected = [(lambda line: line[interval[0] - 1:interval[1]].rstrip())(line)
                    for line in lines]
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
        args = ["-b", f"{interval[0]}-{interval[1]}", "lorem_ipsum.txt"]
        app = CutApp(args)
        with self.assertRaises(RunError):
            app.run(None, [])

    @given(st.integers(0, 0), st.integers(1, IPSUM_MAX))
    def test_interval_starting_with_zero_raises_exception(self, x, y):
        if x == y:
            return
        interval = (x, y)
        args = ["-b", f"{interval[0]}-{interval[1]}", "lorem_ipsum.txt"]
        app = CutApp(args)
        with self.assertRaises(RunError):
            app.run(None, [])

    @given(st.from_regex("(A|a|[c-z]|[C-Z])", fullmatch=True))
    def test_invalid_option_raises_exception(self, char):
        args = ["-{char}", f"{0}-{10}", "lorem_ipsum.txt"]
        with self.assertRaises(ContextError):
            CutApp(args)
