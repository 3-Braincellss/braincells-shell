from shell_test_interface import ShellTestCase

from exceptions import (AppNotFoundError, ContextError, RunError,
                        ShellSyntaxError)
from shell import Shell


class TestShell(ShellTestCase):
    def setUp(self):
        super().setUp()
        self.shell = Shell()

    def test_execute_simple(self):
        text = "echo hello"
        out = self.shell.execute(text)
        self.assertEqual(out, "hello")

    def test_execute_sequence(self):
        text = "echo hello; cat dir_files/file-4"
        out = self.shell.execute(text)
        self.assertEqual(out, "hello\ndepression")

    def test_run_app_not_found(self):

        with self.assertRaises(AppNotFoundError):
            self.shell.execute("gcc make file")

    def test_run_context(self):

        with self.assertRaises(ContextError):
            self.shell.execute("ls one two three")

    def test_run_app_run_error(self):

        with self.assertRaises(RunError):
            self.shell.execute("cat wakanadaaaaaaaaaaaaaaaaa")

    def test_run_syntax_error(self):
        with self.assertRaises(ShellSyntaxError):
            self.shell.execute(";;;")

    def test_execute_empty(self):
        text = "    "
        out = self.shell.execute(text)
        self.assertEqual(out, "")
