"""
This module contains exceptions that shell will be raising and handling.
There is one common interface ``AppExcpetion`` and 3 concrete implementations
of that interface.

"""
from .shellerr import ShellError
from .appnotfounderr import AppNotFoundError
from .contexterr import ContextError
from .runerr import RunError
from .syntaxerr import ShellSyntaxError

__all__ = [
    "ShellError",
    "ContextError",
    "AppNotFoundError",
    "RunError",
    "ShellSyntaxError",
]
