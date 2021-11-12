import unittest

from shell import Shell


class TestShell(unittest.TestCase):
    def test_shell(self):
        shell = Shell()
        out = shell.execute("echo hello world")
        self.assertEqual(out, "hello world")


if __name__ == "__main__":
    unittest.main()
