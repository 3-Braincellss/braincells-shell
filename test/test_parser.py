from shell_test_interface import ShellTestCase

from exceptions import ShellSyntaxError
from commands import Call, Pipe, Sequence
from parser import CommandTransformer, ShellParser


class TestParser(ShellTestCase):
    def setUp(self):
        super().setUp()
        self.parser = ShellParser()
        self.transformer = CommandTransformer()

    def test_command(self):
        tree = self.parser.parse("echo ")
        out = self.transformer.transform(tree)
        self.assertIsInstance(out, Call)

    def test_seq(self):
        tree = self.parser.parse("echo ; echo ")
        out = self.transformer.transform(tree)
        self.assertIsInstance(out, Sequence)

    def test_pipe(self):
        tree = self.parser.parse("echo | echo ")
        out = self.transformer.transform(tree)
        self.assertIsInstance(out, Pipe)

    def test_redirects(self):
        tree = self.parser.parse("echo < file1 > file2")
        out = self.transformer.transform(tree)
        self.assertIsInstance(out, Call)

    def test_singlequote(self):
        tree = self.parser.parse("echo \' text \'")
        out = self.transformer.transform(tree)
        self.assertIsInstance(out, Call)

    def test_doublequote(self):
        tree = self.parser.parse("echo \" text \"")
        out = self.transformer.transform(tree)
        self.assertIsInstance(out, Call)

    def test_backquote_call(self):
        tree = self.parser.parse("echo \"`echo text`\"")
        out = self.transformer.transform(tree)
        self.assertIsInstance(out, Call)

    def test_raisesyntaxerror(self):
        with self.assertRaises(ShellSyntaxError):
            self.parser.parse(";")
