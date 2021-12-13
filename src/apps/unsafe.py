"""
unsafe
======
Module representing the unsafe application decorator.
Usage in shell: _application [OPTIONS] [ARGS]

Example:
    `_head file-that-does-not-exist.txt`
"""
from apps import App
from exceptions import ShellError


class UnsafeApp(App):
    """A class representing the unsafe shell application decorator

    Args:
        app (:obj:`App`): The application be decorated.
    """

    def __init__(self, app):
        super().__init__(app)
        self.app = app

    def run(self, inp, out):
        """Executes the application supplied.

        If the application causes some error, instead of raising said error,
        the error message is added to the output deque, otherwise the output
        is added to the deque like normal.

        """
        try:
            out = self.app.run(inp, out)
        except ShellError as error:
            out.append(str(error))
        return out

    def validate_args(self):
        """No validation needed for an unsafe application"""
