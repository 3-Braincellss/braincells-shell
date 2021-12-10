import unittest
from hypothesis import given, strategies as st
from common.tools import read_lines_from_file
from apps import CatApp
from exceptions import ContextError
from unittest.mock import patch
import os


class TestCat(unittest.TestCase):

    @staticmethod
    def filter_ws(arr):
        return list(filter(lambda x: (x != ""), arr))

    @given(st.from_regex("([a-zA-Z0-9]+\n)+", fullmatch=True))
    def test_cat_read_contents_is_file_contents(self, text):
        expected = self.filter_ws(text.split("\n"))
        with open("test.txt", "w") as file:
            file.write(text)
        out = []
        CatApp(["test.txt"]).run(None, out)
        os.remove("test.txt")
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
