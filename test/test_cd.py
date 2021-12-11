from hypothesis import given, strategies as st
import unittest
from shell_test_interface import ShellTestCase
from apps import CdApp
import os


class TestCd(ShellTestCase):

    def test_cd_no_args_goes_home(self):
        app = CdApp([])
        app.run([], [])
        print(os.getcwd())
