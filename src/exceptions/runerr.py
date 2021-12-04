"""
Run Error
=========

Errors that are raised during runtime.
"""


from exceptions import ShellError

class RunError(ShellError):
    """Errors that occur during app's runtime

    Even if an app passes context checking phase, it can still cause some
    errors. Whenever this happens an `AppRunException` is raised.

    These errors **WILL** be ignored with *unsafe* apps.


    """
    def __init__(self, app_str, message="Oops, something went wrong"):
        super().__init__(app_str, message)
        self.message = f"Runtime error in '{app_str}': " + message
