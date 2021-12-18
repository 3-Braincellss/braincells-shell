import os

from shell_test_interface import ShellTestCase

from apps import MkdirApp
from exceptions import ContextError


class TestMkdir(ShellTestCase):
    def test_mkdir(self):
        app = MkdirApp(["cool_dir"])
        app.validate_args()
        app.run(None, [])
        self.assertTrue(os.path.isdir("cool_dir"))

    def test_mkdir_multiple(self):
        paths = ["dir_empty/deception", "cool_dir", "less_cool_dir"]
        app = MkdirApp(paths)
        app.validate_args()
        app.run(None, [])
        for dir in paths:
            self.assertTrue(os.path.isdir(dir))

    def test_mkdir_no_args_raises_exception(self):
        with self.assertRaises(ContextError):
            MkdirApp([]).validate_args()

    def test_mkdir_existant_raises_exception(self):
        with self.assertRaises(ContextError):
            MkdirApp(["dir_empty"]).validate_args()

    def test_mkdir_non_existant_path_raises_exception(self):
        with self.assertRaises(ContextError):
            MkdirApp(["oh_no/help/me"]).validate_args()
