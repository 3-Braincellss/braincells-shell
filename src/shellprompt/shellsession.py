import os
import getpass
import socket

from collections import deque

from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.lexers import PygmentsLexer

from common.tools import prettify_path
from pretty_colours import KeyWordLexer
from exceptions import ShellError
from shell import Shell
from shellprompt.shellcompleter import ShellPathCompleter


class ShellSession(PromptSession):
    def __init__(self):
        self.shell = Shell()
        self.style = Style.from_dict({
            "user_host": "#ff006e",
            "path": "#06d6a0",
            "arrow": "#118ab2",
            "pygments.keyword": "#118ab2",
        })
        self.lexer = PygmentsLexer(KeyWordLexer)
        super().__init__(style=self.style, completer=ShellPathCompleter(), lexer=self.lexer)

    def run(self):

        while True:

            try:

                text = self.prompt(self._prompt_message())
            except KeyboardInterrupt:
                exit()

            if text:
                try:
                    out = self.shell.execute(text)
                except ShellError as err:
                    out = deque()
                    out.append(err.message)

                while len(out) > 0:
                    print(out.popleft())

    def _prompt_message(self):
        username = getpass.getuser()
        hostname = socket.gethostname()
        user_host = f"[{username}@{hostname}]"
        cur_dir = prettify_path(os.getcwd())

        msg = FormattedText([
            ("class:user_host", f"{user_host} "),
            ("class:path", f"{cur_dir}"),
            ("class:arrow", " ~~> "),
        ])

        return msg


if __name__ == "__main__":
    sh = ShellSession()
    sh.run()
