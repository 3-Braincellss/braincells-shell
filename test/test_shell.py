import unittest

from shell_test_interface import ShellTestCase
from shell import execute
from exceptions import (
    AppNotFoundError,
    ContextError,
    RunError,
    ShellSyntaxError,
)


class TestShell(ShellTestCase):
    def test_execute_simple(self):
        text = "echo hello"
        out = execute(text)
        self.assertEqual(out, "hello")

    def test_run_app_not_found(self):

        with self.assertRaises(AppNotFoundError):
            execute("gcc make file")

    def test_run_context(self):

        with self.assertRaises(ContextError):
            execute("ls one two three")

    def test_run_app_run_error(self):

        with self.assertRaises(RunError):
            execute("cat wakanadaaaaaaaaaaaaaaaaa")

    def test_run_syntax_error(self):
        with self.assertRaises(ShellSyntaxError):
            execute(";;;")

    def test_execute_empty(self):
        text = "    "
        out = execute(text)
        self.assertEqual(out, "")
