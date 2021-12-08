import unittest

from shell_test_interface import ShellTestCase
from shell import Shell
from exceptions import (
    AppNotFoundError,
    ContextError,
    RunError,
    ShellSyntaxError,
)


class TestShell(ShellTestCase):
    def test_execute_simple(self):

        command_text = "echo hello"
        out = Shell.execute(command_text)
        result = "\n".join(out)

        self.assertEqual(result, "hello")

    def test_run_app_not_found(self):
        sh = Shell()

        with self.assertRaises(AppNotFoundError):
            sh.run("gcc make file")

    def test_run_context(self):
        sh = Shell()

        with self.assertRaises(ContextError):
            sh.run("ls one two three")

    def test_run_app_run_error(self):
        sh = Shell()

        with self.assertRaises(RunError):
            sh.run("cat wakanadaaaaaaaaaaaaaaaaa")

    def test_run_syntax_error(self):
        sh = Shell()
        with self.assertRaises(ShellSyntaxError):
            sh.run(";;;")
