"""
This module contains operations that can execute apps and combine
their behaviours. All operations are created with Operation Factory.
"""
from .command import Command
from .call import Call
from .pipe import Pipe
from .sequence import Sequence
from .command_factory import CommandFactory

__all__ = [
    "Command",
    "Call",
    "Pipe",
    "Sequence",
    "CommandFactory",
]
