"""
Context Error
=============

They prevent apps from being run.
"""


from exceptions import ShellError


class ContextError(ShellError):
    """Context errors that prevent apps from being run

    Each app has a ``validate_args()`` method that is run right before the
    app is run. This method will check options that are passed to the app
    and raise ``ContextError`` if they don't make sense.
    ``ContextError`` exists to prevent apps from running
    when they are doomed to fail based on options alone,
    which should hopefully prevent wasting some CPU power when it's unnecessary.

    These errors **WILL** be ignored with **unsafe** apps.
    """
    def __init__(self, app_str, message="GO AWAY >=["):
        super().__init__(app_str, message)
        self.message = f"Context error in {app_str}: " + message
