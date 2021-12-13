import unittest
from collections import deque

from dummies import DummyOperation
from shell_test_interface import ShellTestCase

from operations import Pipe


class TestPipe(ShellTestCase):
    def setUp(self):
        super().setUp()

        ctx = {
            "op1": DummyOperation(),
            "op2": DummyOperation(),
        }

        self.op = Pipe(ctx)

    def test_run(self):
        self.op.op1.custom_output = deque(["Hello", "World"])

        out = deque()
        out = self.op.run(None, out)
        result = set(out)
        expected = set(["Hello", "World"])

        self.assertEqual(result, expected)
