from hypothesis import given, strategies as st
import unittest
from apps import PwdApp
from exceptions import ContextError
import os


class TestPwd(unittest.TestCase):
    def test_pwd(self):
        expected = os.path.abspath(".")
        out = []
        PwdApp([]).run(None, out)
        self.assertEqual(out[0], expected)

    def test_giving_args_raises_error(self):
        args = ["-e", "I", "will", "throw", "an", "error.txt"]
        with self.assertRaises(ContextError):
            PwdApp(args).run(None, [])
