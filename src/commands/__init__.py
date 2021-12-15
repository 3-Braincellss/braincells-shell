"""
Module Contents
===============

This module contains definitions for different types
of commands that can be executed in our shell, as well
as the common command interface and a command factory
for easy object creation.

The list of supported commands:

- ``Call`` - Command primitive which runs a specific app.

- ``Pipe`` - Can redirect output of one command as the input of another

- ``Sequence`` - Runs 2 commands in a sequence
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
