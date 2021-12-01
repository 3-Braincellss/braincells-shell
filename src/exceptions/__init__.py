"""
This module contains exceptions that shell will be raising and handling.
There is one common interface ``AppExcpetion`` and 3 concrete implementations
of that interface.

"""

from .exceptions import (
    AppException,
    AppContextException,
    AppRunException,
    AppNotFoundException,
)
