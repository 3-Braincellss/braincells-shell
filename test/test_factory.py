import unittest

from operations.operation_factory import OperationFactory
from operations.call import Call


class TestFactory(unittest.TestCase):
    def test_call(self):
        o = OperationFactory()
        a = o.get_operation("call", "ls")
        self.assertIsInstance(a, Call)
