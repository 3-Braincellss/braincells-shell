import os
import getpass
import socket

from prompt_toolkit.formatted_text import FormattedText

from prompt import ShellSession
from common.tools import prettify_path

from shell_test_interface import ShellTestCase


class TestSession(ShellTestCase):
    def test_prompt_message(self):

        sesh = ShellSession()

        txt = ShellSession()._prompt_message()

        expected = FormattedText([
            ("class:user_host",
             f"[{getpass.getuser()}@{socket.gethostname()}] "),
            ("class:start_path", f"{prettify_path(os.getcwd())}"),
            ("class:arrow", " ~~> "),
        ])

        self.assertEqual(txt, expected)
