from dummies import DummyCommand
from shell_test_interface import ShellTestCase

from commands import Sequence


class TestSequence(ShellTestCase):
    def setUp(self):
        super().setUp()

        ctx = {
            "op1": DummyCommand(),
            "op2": DummyCommand(),
        }

        self.op = Sequence(ctx)

    def test_run(self):
        self.op.op1.custom_output = ["Hello", "World"]
        self.op.op2.custom_output = ["Goodbye", "World"]

        out = []
        out = self.op.run(None, out)
        expected = ["Hello", "World", "Goodbye", "World"]

        self.assertEqual(out, expected)
