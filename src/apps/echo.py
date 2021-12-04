"""
echo
====
This module represents the echo bash command.
Usage in shell: echo [ARGS]...

Example:
    `echo hello world`
"""
from apps.app import App


class EchoApp(App):
    """A class representing the echo shell command

    Args:
        args (:obj:`list`): Contains all the arguments and options of
            the instruction.

    """
    def __init__(self, args):
        super().__init__(args)
        self.args = args

    def run(self, inp, out):
        """Executes the echo command on the given arguments.

        Simply appends the space seperated arguments supplied.

        Args:
            inp (:obj:`deque`, *optional*): The input args of the command,
                only used for piping and redirects.
            out (:obj:`deque`): The output deque, used to store the
                result of execution.

        Returns:
            ``deque``: The deque will contain the input arguments,
            each seperated by whitespace.
        """

        out.append(" ".join(self.args))
        return out

    def validate_args(self):
        """
        Checks whether the given arguments are valid.
        """
