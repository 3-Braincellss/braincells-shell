from hypothesis import given, settings
from hypothesis.extra.lark import from_lark
from prompt_toolkit.document import Document

from parser import ShellParser
from prompt import ShellHighlighter

from shell_test_interface import ShellTestCase

PARSER = ShellParser()


class TestShellHighlighter(ShellTestCase):
    @settings(deadline=400)
    @given(from_lark(PARSER))
    def test_random_invariant(self, s):
        PARSER.parse(s)
        hlr = ShellHighlighter()
        document = Document(s)
        out = hlr.lex_document(document)(0)
        for each in out:
            self.assertIsInstance(each, tuple)
            self.assertIsInstance(each[0], str)
            self.assertIsInstance(each[1], str)
