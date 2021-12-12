from hypothesis import given, strategies as st
import unittest
from apps import EchoApp


class TestEcho(unittest.TestCase):
    @given(st.from_regex("[a-zA-Z0-9 ]*", fullmatch=True))
    def test_echo_alpha_num(self, text):
        app = EchoApp(text.split(" "))
        out = []
        app.run(None, out)
        self.assertEqual(out[0], text)
