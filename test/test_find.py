from hypothesis import given, strategies as st
import unittest
from apps import FindApp
from exceptions import ContextError, RunError
from shell_test_interface import ShellTestCase


class TestFind(ShellTestCase):
    def test_find_from_current_dir(self):
        out = []
        app = FindApp(["-name", "f*"])
        app.run(None, out)
        self.assertEqual(
            set([
                "./dir_files/file-1", "./dir_files/file-2",
                "./dir_files/file-3", "./dir_files/file-4",
                "./dir_files/file-5"
            ]), set(out))

    def test_find_from_dir(self):
        out = []
        app = FindApp(["-name", "dir*", "dir_nested"])
        app.run(None, out)
        self.assertEqual(
            set([
                "dir_nested/dir_nested.txt",
                "dir_nested/nest_1/dir_nested_1.txt",
                "dir_nested/nest_2/dir_nested_2.txt"
            ]), set(out))

    def test_no_options_raises_exception(self):
        with self.assertRaises(ContextError):
            FindApp([]).validate_args()

    def test_too_many_options_raises_exceptions(self):
        with self.assertRaises(ContextError):
            FindApp(["-name", "dir*", "dir_nested",
                     "dir_files"]).validate_args()

    def test_non_existant_path_raises_exception(self):
        with self.assertRaises(RunError):
            FindApp(["-name", "dir*", "dir_jested"]).validate_args()
