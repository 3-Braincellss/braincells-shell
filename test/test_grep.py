import unittest

from shell_test_interface import ShellTestCase

from apps import GrepApp
from common.tools import read_lines_from_file
from exceptions import ContextError, RunError

TEST_PATH_5 = "dir_files/file-5"
TEST_PATH_1 = "dir_files/file-1"


class TestGrep(ShellTestCase):
    def test_grep_empty_string_returns_everything(self):
        expected = list(
            map(str.rstrip, read_lines_from_file(TEST_PATH_5, "grep_test")))
        out = []
        GrepApp(["", TEST_PATH_5]).run(None, out)
        self.assertEqual(expected, out)

    def test_normal_grep(self):
        expected = ["AAA", "I don't know any more letters"]
        out = []
        app = GrepApp(["a|A", TEST_PATH_5])
        app.validate_args()
        app.run(None, out)
        self.assertEqual(expected, out)

    def test_no_args_raises_exception(self):
        with self.assertRaises(ContextError):
            GrepApp([]).validate_args()

    def test_multifile_grep(self):
        expected = [
            "dir_files/file-1:AA", "dir_files/file-5:AAA",
            "dir_files/file-5:I don't know any more letters"
        ]
        out = []
        GrepApp(["a|A", TEST_PATH_1, TEST_PATH_5]).run(None, out)
        self.assertEqual(expected, out)

    def test_grep_accepts_no_options(self):
        with self.assertRaises(ContextError):
            GrepApp(["-b", "uh oh", "error.txt"])

    def test_redirection(self):
        inp = ["gee wizz", "i wish i was a", "bee wizz", "green."]
        out = []
        expected = ["gee wizz", "bee wizz", "green."]
        GrepApp(["ee"]).run(inp, out)
        self.assertEqual(expected, out)
