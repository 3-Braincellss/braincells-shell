"""
This module contains operations that can execute apps and combine
their behaviours. All operations are created with Operation Factory.
"""
from .operation import Operation
from .call import Call
from .pipe import Pipe
from .sequence import Sequence
from .operation_factory import OperationFactory

__all__ = [
    "Operation",
    "Call",
    "Pipe",
    "Sequence",
    "OperationFactory",
]
