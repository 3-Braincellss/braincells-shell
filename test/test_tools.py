import unittest
from shell_test_interface import ShellTestCase
from common.tools import *
from exceptions import RunError


class TestTools(ShellTestCase):
    def test_read_contents(self):
        expected = "AAA\nBBB\nDDD\nI don't know any more letters"
        out = read_from_file("dir_files/file-5", "tool_test")
        self.assertEqual(out, expected)

    def test_reading_contents_from_non_existant_file_raises_exception(self):
        with self.assertRaises(RunError):
            out = read_from_file("dir_files/file-6", "tool_test")

    def test_reading_contents_from_a_directory_raises_exception(self):
        with self.assertRaises(RunError):
            out = read_from_file("dir_files", "tool_test")

    def test_read_lines(self):
        expected = ["AAA\n", "BBB\n", "DDD\n", "I don't know any more letters"]
        out = read_lines_from_file("dir_files/file-5", "tool_test")
        self.assertEqual(out, expected)

    def test_reading_lines_from_non_existant_file_raises_exception(self):
        with self.assertRaises(RunError):
            out = read_lines_from_file("dir_files/file-6", "tool_test")

    def test_reading_lines_from_a_directory_raises_exception(self):
        with self.assertRaises(RunError):
            out = read_lines_from_file("dir_files", "tool_test")

    def test_pretty_path(self):
        expected = "h/t/i/m/p/path.txt"
        path = "/hello/this/is/my/pretty/path.txt"
        out = prettify_path(path)
        self.assertEqual(out, expected)
