"""
Call
====
An operation primitive that contains an app that it runs.
"""
from collections import deque

from apps import AppFactory
from common.tools import read_lines_from_file
from commands import Command


class Call(Command):
    """Call operation that executes some app.

    Attributes:
        app(App): The app to be run.
        left_red(:obj:`str`): File name from the left redirection.
            ``None`` if no left redirection was done.
        right_red(:obj:`str`): File name from the right redirection.
            ``None`` if no right redirection was done.
    """
    def __init__(self, ctx):
        super().__init__(ctx)
        self.app = AppFactory.get_app(
            ctx["app"],
            ctx["args"],
        )
        self.left_red = ctx["left_red"]
        self.right_red = ctx["right_red"]

    def run(self, inp, out):
        """Handles possible redirections and runs the app.

        Can handle both input and output redirections.

        In case there is an input redirection and some piped input
        it will prioritise redirected input.

        In case there is an output redirection will create an empty
        ``deque`` for the output and store results in the output file.
        Will return any output that was passed as the argument.
        """

        new_inp = inp
        if self.left_red is not None:
            lines = deque(read_lines_from_file(self.left_red, "redirect"))
            new_inp = deque(map(str.rstrip, lines))

        if self.right_red is not None:
            new_out = deque()
            with open(self.right_red, "w", encoding="utf-8") as f:
                self.app.validate_args()
                new_out = self.app.run(new_inp, new_out)
                for line in new_out:
                    f.write(line)
                    f.write("\n")
        else:
            self.app.validate_args()
            out = self.app.run(new_inp, out)
        return out
