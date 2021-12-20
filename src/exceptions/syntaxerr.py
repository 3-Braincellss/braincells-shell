"""
Shell Syntax Error
==================

Error wrapper for lark's VisitError.
It is raised whenever the parsing fails.
"""

from exceptions import ShellError

__all__ = [
    "ShellSyntaxError"
]


class ShellSyntaxError(ShellError):
    """Errors that appears on failed parsing of the input string."""
    def __init__(self, message="Wrong Syntax"):
        super().__init__("", message)
        self.message = f"Syntax Error:\n{message}"
