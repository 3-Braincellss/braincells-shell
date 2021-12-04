"""
This module contains exceptions that shell will be raising and handling.
There is one common interface ``AppExcpetion`` and 3 concrete implementations
of that interface.

"""

from .shellerr import ShellError
from .contexterr import ContextError
from .appnotfounderr import AppNotFoundError
from .runerr import RunError

__all__ = [
    "ShellError",
    "ContextError",
    "AppNotFoundError",
    "RunError",
]
