import os

from shell_test_interface import ShellTestCase

from apps import RmApp
from exceptions import ContextError


class TestRm(ShellTestCase):
    def test_rm(self):
        app = RmApp(["dir_empty"])
        app.validate_args()
        app.run(None, [])
        self.assertFalse(os.path.isdir("dir_empty"))

    def test_rm_file(self):
        app = RmApp(["dir_files/file-3"])
        app.validate_args()
        app.run(None, [])
        self.assertFalse(os.path.isdir("dir_files/file-3"))

    def test_rm_multiple(self):
        paths = ["dir_empty", "dir_out"]
        app = RmApp(paths)
        app.validate_args()
        app.run(None, [])
        for dir in paths:
            self.assertFalse(os.path.isdir(dir))

    def test_rm_no_args_raises_exception(self):
        with self.assertRaises(ContextError):
            RmApp([]).validate_args()

    def test_rm_recursive(self):
        app = RmApp(["-r", "dir_nested"])
        app.validate_args()
        app.run(None, [])
        self.assertFalse(os.path.isdir("dir_nested"))

    def test_rm_non_existant_path_raises_exception(self):
        with self.assertRaises(ContextError):
            RmApp(["oh_no/help/me"]).validate_args()

    def test_rm_recursive_on_non_empty_dir_raises_exception(self):
        with self.assertRaises(ContextError):
            RmApp(["dir_nested"]).run(None, [])

    def test_rm_with_invalid_option_raises_exception(self):
        with self.assertRaises(ContextError):
            RmApp(["-a", "dir_nested"]).run(None, [])
