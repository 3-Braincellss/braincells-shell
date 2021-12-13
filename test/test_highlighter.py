import os

from hypothesis import given, strategies as st
from hypothesis.extra.lark import from_lark

from lark import Lark
from prompt_toolkit.document import Document
from shellparser import HighlightTransformer, ShellHighlighter

from shell_test_interface import ShellTestCase

dirname = os.path.join(os.path.dirname(__file__), '..')
filename = os.path.join(dirname, 'src/shellparser/grammar.lark')
with open(filename, "r", encoding="utf-8") as grammar:
    g = grammar.read()
    GRAMMAR = Lark(g, start="command")


class TestHighlighter(ShellTestCase):
    def setUp(self):
        super().setUp()
        self.tran = HighlightTransformer(visit_tokens=True)

    @staticmethod
    def form_text(styles=None):
        n = 10
        if styles is not None:
            n = len(styles)
        return [("class:arg", "A") for i in range(n)]

    @staticmethod
    def form_token():
        return ("class:space", "B")

    def test_command(self):
        ftext = self.form_text()
        inp = [ftext]
        self.assertEqual(self.tran.command(inp), ftext)

    def test_command_whitespace(self):
        ftext = [self.form_token()]
        self.assertEqual(self.tran.command(ftext), ftext)

    def test_seq_single_command(self):
        command = [self.form_text()]
        res = self.tran.seq(command)

        new_com = command[0].copy()
        new_com.append(("class:oper", ";"))
        self.assertEqual(res, new_com)

    def test_seq_double_command(self):
        command1 = self.form_text()
        command2 = self.form_text()
        inp = [command1, command2]
        res = self.tran.seq(inp)

        expected = []
        expected.extend(command1)
        expected.append(("class:oper", ";"))
        expected.extend(command2)

        self.assertEqual(res, expected)

    def test_pipe(self):
        command1 = self.form_text()
        command2 = self.form_text()
        inp = [command1, command2]
        res = self.tran.pipe(inp)

        expected = []
        expected.extend(command1)
        expected.append(("class:oper", "|"))
        expected.extend(command2)

        self.assertEqual(res, expected)

    def test_call(self):
        thing1 = self.form_text([
            "class:arg",
            "class:arg",
        ])

        thing1[0] = ("class:arg", "ls")

        thing2 = self.form_token()
        thing3 = self.form_text([
            "class:arg",
            "class:path",
            "class:arg",
            "class:arg",
        ])

        inp = [thing1, thing2, thing3]
        res = self.tran.call(inp)

        thing = thing1.copy()
        thing[0] = ("class:app", thing[0][1])

        expected = []
        expected.extend(thing)
        expected.append(thing2)
        expected.extend(thing3)

        self.assertEqual(res, expected)

    def test_call_unsafe(self):
        inp = self.form_text()
        inp[0] = ("class:arg", "_ls")

        res = self.tran.call(inp)

        expected = inp.copy()
        expected[0] = ("class:unsafe", "_ls")

        self.assertEqual(res, expected)

    def test_redirection(self):
        inp = [self.form_text()]
        res = self.tran.redirection(inp)
        expected = inp[0]
        self.assertEqual(res, expected)

    def test_l_redirection(self):
        whitespace = self.form_token()
        paths = self.form_text()

        inp = [whitespace, paths]

        res = self.tran.l_redirection(inp)

        expected = []
        expected.append(("class:redir", "<"))
        expected.append(whitespace)
        expected.extend(paths)
        self.assertEqual(res, expected)

    def test_r_redirection(self):
        whitespace = self.form_token()
        paths = self.form_text()

        inp = [whitespace, paths]

        res = self.tran.r_redirection(inp)

        expected = []
        expected.append(("class:redir", ">"))
        expected.append(whitespace)
        expected.extend(paths)
        self.assertEqual(res, expected)

    def test_arguments(self):
        args = self.form_text()
        args.append(("class:arg", "toplevel.txt"))

        res = self.tran.arguments(args)

        expected = args.copy()
        expected[-1] = ("class:path", "toplevel.txt")

        self.assertEqual(res, expected)

    def test_quoted(self):
        inp = ["hello"]
        res = self.tran.quoted(inp)
        expected = ("class:quotes", "hello")
        self.assertEqual(res, expected)

    def test_double_quoted(self):
        inp = self.form_text()
        inp[0] = "B"
        inp[2] = "C"
        res = self.tran.double_quoted(inp)
        expected = "\"BACAAAAAAA\""
        self.assertEqual(res, expected)

    def test_single_quoted(self):
        inp = self.form_text()
        inp[0] = "B"
        inp[2] = "C"
        res = self.tran.single_quoted(inp)
        expected = "'BACAAAAAAA'"
        self.assertEqual(res, expected)

    def test_back_quoted(self):
        inp = self.form_text()
        inp[0] = "B"
        inp[2] = "C"
        res = self.tran.back_quoted(inp)
        expected = "`BACAAAAAAA`"
        self.assertEqual(res, expected)

    @given(from_lark(GRAMMAR))
    def test_random_invariant(self, s):
        """Testing invariant with random testing

        One assumption here that must hold true for
        everything to work is:
        
        Output of the transformer MUST be a list
        of tuples of 2 strings.

        if that's not the case, prompt_toolkit
        will get VERY angry so we want to avoid it at all costs.
        """
        tree = GRAMMAR.parse(s)

        out = self.tran.transform(tree)
        for each in out:
            self.assertIsInstance(each, tuple)
            self.assertIsInstance(each[0], str)
            self.assertIsInstance(each[1], str)



class TestShellHighlighter(ShellTestCase):

    @given(from_lark(GRAMMAR))
    def test_random_invariant(self, s):
        tree = GRAMMAR.parse(s)
        hlr = ShellHighlighter()
        document = Document(s)
        out = hlr.lex_document(document)(0)
        for each in out:
            self.assertIsInstance(each, tuple)
            self.assertIsInstance(each[0], str)
            self.assertIsInstance(each[1], str)

        
        
        
        

        

        
        
        
