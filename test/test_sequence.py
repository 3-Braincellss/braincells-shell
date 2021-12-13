import unittest

from collections import deque

from operations import Sequence

from dummies import DummyOperation
from shell_test_interface import ShellTestCase


class TestSequence(ShellTestCase):
    def setUp(self):
        super().setUp()

        ctx = {
            "op1": DummyOperation(),
            "op2": DummyOperation(),
        }

        self.op = Sequence(ctx)

    def test_run(self):
        self.op.op1.custom_output = ["Hello", "World"]
        self.op.op2.custom_output = ["Goodbye", "World"]

        out = []
        out = self.op.run(None, out)
        expected = ["Hello", "World", "Goodbye", "World"]

        self.assertEqual(out, expected)
