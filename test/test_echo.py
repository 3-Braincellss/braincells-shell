from hypothesis import given
from hypothesis import strategies as st
from shell_test_interface import ShellTestCase

from apps import EchoApp


class TestEcho(ShellTestCase):
    @given(st.from_regex("[a-zA-Z0-9 ]*", fullmatch=True))
    def test_echo_never_fails(self, text):
        app = EchoApp(text.split(" "))
        out = []
        app.run(None, out)
        self.assertEqual(out[0], text)
