from hypothesis import given, settings
from hypothesis.extra.lark import from_lark

from parser import CommandTransformer, ShellParser, ShellParser

from shell_test_interface import ShellTestCase

from commands import Call, Pipe, Sequence, Command
from exceptions import ShellSyntaxError, ShellError

PARSER = ShellParser()


class TestParser(ShellTestCase):
    def setUp(self):
        super().setUp()
        self.parser = PARSER
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
        tree = self.parser.parse("echo ' text '")
        out = self.transformer.transform(tree)
        self.assertIsInstance(out, Call)

    def test_doublequote(self):
        tree = self.parser.parse('echo " text "')
        out = self.transformer.transform(tree)
        self.assertIsInstance(out, Call)

    def test_backquote_call(self):
        tree = self.parser.parse('echo "`echo text`"')
        out = self.transformer.transform(tree)
        self.assertIsInstance(out, Call)

    def test_raisesyntaxerror(self):
        with self.assertRaises(ShellSyntaxError):
            self.parser.parse(";")

    @settings(deadline=400)
    @given(from_lark(PARSER))
    def test_random(self, s):

        correct = False
        tree = PARSER.parse(s)

        try:
            out = self.transformer.transform(tree)
            correct = isinstance(out, Command)
        except ShellError:
            correct = True

        self.assertTrue(correct)
