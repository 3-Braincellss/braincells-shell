import unittest
from shell_test_interface import ShellTestCase
from apps import LsApp
from exceptions import ContextError, RunError
import os


class TestLs(ShellTestCase):
    def test_ls(self):
        expected = sorted([
            "dir_empty", "dir_files", "dir_nested", "dir_out", "no_extension",
            "other_extension.py", "toplevel.txt"
        ])
        out = []
        app = LsApp([])
        app.validate_args()
        app.run(None, out)
        self.assertEqual(out, expected)

    def test_ls_after_changing_dir(self):
        expected = sorted(["file-1", "file-2", "file-3", "file-4", "file-5"])
        out = []
        app = LsApp(["dir_files"])
        app.validate_args()
        app.run(None, out)
        self.assertEqual(out, expected)

    def test_ls_with_non_exsistant_path_raises_exception(self):
        with self.assertRaises(ContextError):
            LsApp(["bruh"]).validate_args()

    def test_ls_with_too_many_args_raises_exception(self):
        with self.assertRaises(ContextError):
            LsApp(["bruh", "moment"]).validate_args()

    def test_ls_on_file_raises_exception(self):
        with self.assertRaises(RunError):
            LsApp(["dir_files/file-1"]).run([], [])
