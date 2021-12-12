import unittest
from shell_test_interface import ShellTestCase
from apps import UniqApp
from exceptions import ContextError, RunError


class TestUniq(ShellTestCase):

    def setUp(self):
        super().setUp()
        with open("dir_files/file-3", "w") as file:
            file.writelines(["AAA\n", "aaa\n", "BBB\n", "BBB\n", "bBb"])

    def test_uniq_no_changes(self):
        expected = ["AAA", "BBB", "DDD", "I don't know any more letters"]
        out = []
        UniqApp(["dir_files/file-5"]).run(None, out)
        self.assertEqual(expected, out)

    def test_uniq(self):
        expected = ["AAA", "aaa", "BBB", "bBb"]
        out = []
        UniqApp(["dir_files/file-3"]).run(None, out)
        self.assertEqual(out, expected)
        pass

    def test_uniq_case_insensitive(self):
        expected = ["AAA", "BBB"]
        out = []
        UniqApp(["-i", "dir_files/file-3"]).run(None, out)
        self.assertEqual(out, expected)
        pass

    def test_uniq_redirection(self):
        expected = ["AAA", "aaa", "BBB", "bBb"]
        inp = ["AAA", "aaa", "BBB", "BBB", "bBb"]
        out = []
        UniqApp(["dir_files/file-3"]).run(inp, out)
        self.assertEqual(out, expected)
        pass

    def test_invalid_args_raises_exception(self):
        with self.assertRaises(ContextError):
            UniqApp(["-b", "oh-no.txt"])
