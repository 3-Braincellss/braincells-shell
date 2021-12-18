
from parser import HighlightTransformer, ShellParser

from hypothesis import given, settings
from hypothesis.extra.lark import from_lark
from prompt_toolkit.document import Document
from shell_test_interface import ShellTestCase

PARSER = ShellParser()


class TestHighlighter(ShellTestCase):
    def setUp(self):
        super().setUp()
        self.tran = HighlightTransformer()

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

        thing2 = self.form_text([
            "class:arg",
            "class:path",
            "class:arg",
            "class:arg",
        ])

        inp = [thing1, thing2]
        res = self.tran.call(inp)

        expected = []
        expected.extend(thing1)
        expected.extend(thing2)
        expected[0] = ("class:app", "ls")

        self.assertEqual(res, expected)

    def test_call_unsafe(self):
        a = self.form_text([
            "class:arg",
            "class:arg",
        ])
        a[0] = ("class:arg", "_ls")

        b = self.form_text([
            "class:arg",
            "class:arg",
        ])

        inp = []
        inp.append(a)
        inp.append(b)

        expected = []
        expected.extend(a)
        expected.extend(b)
        expected[0] = ("class:unsafe", "_ls")

        res = self.tran.call(inp)

        self.assertEqual(res, expected)

    def test_redirection(self):
        inp = [self.form_text()]
        res = self.tran.redirection(inp)
        expected = inp[0]
        self.assertEqual(res, expected)

    def test_l_redirection(self):
        inp = [[("a", "b")], [("a", "b")]]

        res = self.tran.l_redirection(inp)

        expected = [
            ("class:redir", "<"),
            ("a", "b"),
            ("a", "b"),
        ]
        self.assertEqual(res, expected)

    def test_r_redirection(self):
        inp = [[("a", "b")], [("a", "b")]]

        res = self.tran.r_redirection(inp)

        expected = [
            ("class:redir", ">"),
            ("a", "b"),
            ("a", "b"),
        ]

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
        inp = ["hello", "`world`"]
        res = self.tran.double_quoted(inp)
        expected = '"hello`world`"'
        self.assertEqual(res, expected)

    def test_single_quoted(self):
        inp = ["HELLO"]
        res = self.tran.single_quoted(inp)
        expected = "'HELLO'"
        self.assertEqual(res, expected)

    def test_back_quoted(self):
        inp = ["HELLO"]
        res = self.tran.back_quoted(inp)
        expected = "`HELLO`"
        self.assertEqual(res, expected)

    @settings(deadline=400)
    @given(from_lark(PARSER))
    def test_random_invariant(self, s):
        """Testing invariant with random testing

        One assumption here that must hold true for
        everything to work is:

        Output of the transformer MUST be a list
        of tuples of 2 strings.

        if that's not the case, prompt_toolkit
        will get VERY angry so we want to avoid it at all costs.
        """
        tree = PARSER.parse(s)

        out = self.tran.transform(tree)
        for each in out:
            self.assertIsInstance(each, tuple)
            self.assertIsInstance(each[0], str)
            self.assertIsInstance(each[1], str)
