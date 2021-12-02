"""
Here you can find all of our exception types and the definition of our
commmon exception interface.
"""

from abc import abstractmethod, ABCMeta


class ShellError(Exception, metaclass=ABCMeta):
    """Exception interface for our errors

    Some exceptions that are raised within our shell are expected behaviour.
    App exceptions will only stop or prevent apps from running.
    They will not cause the whole shell process to stop.
    All app exceptions are aware of the app that caused an exception
    and aware of an appropriate message to show.
    These exceptions are handled on the highest level of command execution.

    Attributes:
        app_str (:obj:`str`): Name of the app.
        message (:obj:`str`): Part of the message that will occur once an exception is raised.
    """

    @abstractmethod
    def __init__(self, app_str, message="Err"):
        super().__init__(app_str, message)
        self.message = message
        self.app_str = app_str


class ContextError(ShellError):
    """Context errors that prevent apps from being run

    Each app has a ``validate_args()`` method that is run right before the app is run.
    This method will check options that are passed to the app
    and raise ``ContextError`` if they don't make sense.
    ``ContextError`` exists to prevent apps from running
    when they are doomed to fail based on options alone,
    which should hopefully prevent wasting some CPU power when it's unnecessary.

    These errors **WILL** be ignored with **unsafe** apps.
    """

    def __init__(self, app_str, message="GO AWAY >=["):
        super().__init__(app_str, message)
        self.message = f"Context error in {app_str}: " + message


class AppNotFoundError(ShellError):
    """Errors that occur when shell doesn't know the app you are trying to run

    These errors are called by the `AppFactory`, in case it is not aware of
    the app you are trying to run. Using an unsafe signature will not
    prevent this error from appearing.

    """

    def __init__(self, app_str, message=""):
        super().__init__(app_str, message)
        self.message = f"I don't know about '{self.app_str}' command. Sorry :("


class RunError(ShellError):
    """Errors that occur during app's runtime

    Even if an app passes context checking phase, it can still cause some errors.
    Whenever this happens an `AppRunException` is raised.

    These errors **WILL** be ignored with *unsafe* apps.


    """

    def __init__(self, app_str, message="Oops, something went wrong"):
        super().__init__(app_str, message)
        self.message = f"Runtime error in '{app_str}': " + message
