"""
Shell Session
=============

This module contains the shell prompt session.
"""

import getpass
import os
import socket
import traceback

from prompt_toolkit import PromptSession
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit.styles import Style

from common.tools import prettify_path
from exceptions import ShellError
from session import ShellPathCompleter
from shell import execute
from shellparser import ShellHighlighter

from .conf import STYLE_DICT

__all__ = [
    'ShellSession',
]


class ShellSession(PromptSession):
    """This class is responsible for managing the prompt session."""

    def __init__(self):
        self.style = Style.from_dict(STYLE_DICT)
        self.lexer = ShellHighlighter()

        super().__init__(
            style=self.style,
            completer=ShellPathCompleter(),
            lexer=self.lexer,
            complete_style=CompleteStyle.READLINE_LIKE,
        )

    def run(self):
        """Runs the prompt session."""

        while True:
            try:

                text = self.prompt(self._prompt_message())
            except KeyboardInterrupt:
                exit()

            try:
                out = execute(text)
            except ShellError as err:
                out = err.message

            except KeyboardInterrupt as err:
                print(f"Keyboard interrupt")
                traceback.print_tb(err.__traceback__)
                

            if len(out) > 0:
                print(out)

    def _prompt_message(self):
        """ Creates a string that will be printed with
        every prompt.

        Returns:
            FormattedText: prompt text
        """
        username = getpass.getuser()
        hostname = socket.gethostname()
        user_host = f"[{username}@{hostname}]"
        cur_dir = prettify_path(os.getcwd())

        msg = FormattedText([
            ("class:user_host", f"{user_host} "),
            ("class:start_path", f"{cur_dir}"),
            ("class:arrow", " ~~> "),
        ])

        return msg


if __name__ == "__main__":
    sh = ShellSession()
    sh.run()
