import unittest
import subprocess

from shell import Shell
from exceptions import AppNotFoundError, ContextError, RunError


class TestShell(unittest.TestCase):
    def run_command(self, command):
        args = [
            "sudo",
            "docker",
            "run",
            "--rm",
            "/comp0010/sh",
            "-c",
            command,
        ]

        p = subprocess.run(args, capture_output=True)

        return p.stdout.decode()

    def test_non_interactive(self):
        output = self.run_command("echo hello")
        res = output.strip()
        self.assertEqual(res, "hello")

    def test_execute_simple(self):

        command_text = "echo hello"
        out = Shell.execute(command_text)
        result = "\n".join(out)

        self.assertEqual(result, "hello")

    def test_run_app_not_found(self):
        sh = Shell()

        with self.assertRaises(AppNotFoundError):
            sh.run("gcc make file")

    def test_run_app_context(self):
        sh = Shell()

        with self.assertRaises(ContextError):
            sh.run("ls one two three")

    def test_run_app_run_exception(self):
        sh = Shell()

        with self.assertRaises(RunError):
            sh.run("cat wakanadaaaaaaaaaaaaaaaaa")
