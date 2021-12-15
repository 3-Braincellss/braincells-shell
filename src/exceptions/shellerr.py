"""
Shell Error
===========

General error interface
"""

from abc import ABCMeta, abstractmethod


class ShellError(Exception, metaclass=ABCMeta):
    """
    Exception interface for our errors

    Some exceptions that are raised within our shell are expected behaviour.
    App exceptions will only stop or prevent apps from running.
    They will not cause the whole shell process to stop.
    All app exceptions are aware of the app that caused an exception
    and aware of an appropriate message to show.
    These exceptions are handled on the highest level of command execution.

    Attributes:
        app_str (:obj:`str`): Name of the app.
        message (:obj:`str`): Part of the message that will occur once
            an exception is raised.
    """
    @abstractmethod
    def __init__(self, app_str, message="Err"):
        super().__init__(app_str, message)
        self.message = message
        self.app_str = app_str
