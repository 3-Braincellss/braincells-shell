"""
Shell
=====

Shell module where the code execution starts.
All major "Shell" logic happens here.
"""

import sys
import os
import getpass
import socket

from collections import deque
from lark.exceptions import VisitError

from shellparser import run_parser
from exceptions import ShellError
from common.tools import prettify_path


class Shell:
    """Main shell class which can start the execution."""

    PREFIX = "~~> "
    """ String that separates current directory section from user input."""
    def run(self, command=None):
        """Runs the shell.

        This method can be run in 2 ways.

        1) In case no arguments are passed, shell will run in an
        **interactive mode**. In other words, run an infinite loop
        prompting user to input a command. If a command is valid and
        can be executed, shell will print the output of the command
        to stdout. In case an error occurs at any point, shell will
        discard any accumulated output, and print out the error message.


        2) If a string is passed, then shell will interpret the string
        as a command, execute this command and print output to **stdout**.

        Parameters:
            command (:obj:`str`): a string representation of a command
                to execute.
        """
        username = getpass.getuser()
        hostname = socket.gethostname()
        user_host = f"[{username}@{hostname}]"

        if command:
            out = self.execute(command)
            while len(out) > 0:
                print(out.popleft())
        else:
            while True:
                cur_dir = prettify_path(os.getcwd())
                print(f"{user_host} {cur_dir} {self.PREFIX}", end="")
                text = input()
                if text:
                    try:
                        out = self.execute(text)
                    except ShellError as err:
                        out = deque()
                        out.append(err.message)

                    while len(out) > 0:
                        print(out.popleft())

    @staticmethod
    def execute(input_str):
        """Parses and executes the input string

        Parameters:
            input_str (:obj:`str`): input string representing a command.

        Returns:
            ``deque``: a deque object each value of which is a single line
            of the output.

        Raises:
            ShellError: in case parsing fails, our a command cannot be run.
            VisitError: in case syntax checking fails.
        """

        out = deque()

        command = run_parser(input_str + " ")
        if command:
            out = command.run(None, out)

        return out


if __name__ == "__main__":
    ARGS_NUM = len(sys.argv) - 1
    sh = Shell()
    if ARGS_NUM > 0:
        if ARGS_NUM != 2:
            raise ValueError("wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {sys.argv[1]}")

        sh.run(sys.argv[2])
    else:
        sh.run()
