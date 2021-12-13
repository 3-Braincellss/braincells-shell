import os

from hypothesis import given
from hypothesis import strategies as st
from shell_test_interface import ShellTestCase

from apps import CatApp
from common.tools import read_lines_from_file
from exceptions import ContextError


class TestCat(ShellTestCase):

    TEST_PATH = "./dir_files/file-3"

    @staticmethod
    def filter_ws(arr):
        return list(filter(lambda x: (x != ""), arr))

    @given(st.from_regex("([a-zA-Z0-9]+\n)+", fullmatch=True))
    def test_cat_read_contents_is_file_contents(self, text):
        expected = self.filter_ws(text.split("\n"))
        with open(self.TEST_PATH, "w") as file:
            file.write(text)
        out = []
        CatApp([self.TEST_PATH]).run(None, out)
        out = self.filter_ws(out)
        self.assertEqual(out, expected)

    @given(st.from_regex("([a-zA-Z0-9 ]+\n)+", fullmatch=True))
    def test_cat_input_redirection(self, text):
        inp = text.split("\n")
        out = []
        CatApp([]).run(inp, out)
        out = self.filter_ws(out)
        expected = self.filter_ws(text.split("\n"))
        self.assertEqual(out, expected)

    @given(st.from_regex("-[a-zA-z]", fullmatch=True))
    def test_cat_accepts_no_options(self, text):
        with self.assertRaises(ContextError):
            app = CatApp([text])

    @given(st.from_regex("([a-zA-Z0-9 ]+\n)+", fullmatch=True))
    def test_cat_validation_never_does_anything(self, text):
        app = CatApp([text])
        app.validate_args()
