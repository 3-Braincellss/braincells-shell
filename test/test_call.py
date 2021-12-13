import unittest
from collections import deque

from dummies import DummyApp
from shell_test_interface import ShellTestCase

from operations import Call


class TestCall(ShellTestCase):
    def setUp(self):
        super().setUp()
        # Just to make the constructor happy
        # TODO:
        # Move appfactory up a level
        # so that I don't have to use an existing app
        # while testing call
        ctx = {
            "app": "ls",
            "args": [],
            "left_red": None,
            "right_red": None,
        }

        self.call = Call(ctx)
        self.call.app = DummyApp()

    def test_run_no_redirects(self):

        self.assertIsInstance(self.call.run(None, deque()), deque)

    def test_run_left_redirect(self):
        self.call.left_red = "toplevel.txt"

        out = deque()
        self.call.run(None, out)
        self.assertEqual(out.popleft(), self.DIR_TREE["toplevel.txt"])

    def test_run_right_redirect(self):
        self.call.right_red = "output.out"
        self.call.left_red = "toplevel.txt"

        out = deque()
        self.call.run(None, out)

        with open("output.out", "r", encoding="utf-8") as outf:
            line = outf.readline().strip()
            self.assertEqual(line, self.DIR_TREE["toplevel.txt"])

    def test_run_input(self):

        inp = deque(["A", "B", "C"])
        out = deque()
        self.call.run(inp, out)

        result = set(out)

        self.assertEqual(result, set(["A", "B", "C"]))
