"""
App Not Found Error
===================

An error that is raised whenever an app is not found.
"""

from exceptions import ShellError


class AppNotFoundError(ShellError):
    """Errors that occur when shell doesn't know the app you are trying to run

    These errors are called by the `AppFactory`, in case it is not aware of
    the app you are trying to run. Using an unsafe signature will not
    prevent this error from appearing.

    """
    def __init__(self, app_str, message=""):
        super().__init__(app_str, message)
        self.message = f"I don't know about '{self.app_str}' command. Sorry :("
