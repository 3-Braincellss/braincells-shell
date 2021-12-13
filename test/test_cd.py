import os
import unittest

from hypothesis import given
from hypothesis import strategies as st
from shell_test_interface import ShellTestCase

from apps import CdApp
from exceptions import ContextError, RunError

TEST_PATH = os.getcwd() + "/_test"


class TestCd(ShellTestCase):
    def tearDown(self):
        os.chdir(TEST_PATH)
        super().tearDown()

    def test_cd_no_args_goes_home(self):
        app = CdApp([])
        app.run([], [])
        self.assertEqual(os.path.expanduser("~"), os.getcwd())

    def test_change_dir(self):
        app = CdApp(["dir_empty"])
        app.validate_args()
        app.run([], [])
        self.assertEqual(TEST_PATH + "/dir_empty", os.getcwd())

    def test_too_many_args_raises_exception(self):
        with self.assertRaises(ContextError):
            CdApp(["dir_empty", "dir_files"]).validate_args()

    def test_directory_does_not_exist(self):
        with self.assertRaises(ContextError):
            CdApp(["what_is_my_purpose"]).validate_args()

    def test_cd_into_file_raises_exception(self):
        with self.assertRaises(RunError):
            CdApp(["dir_files/file_1"]).run([], [])
