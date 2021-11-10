import unittest

from operations.operation_factory import OperationFactory
from operations.call import Call


class TestFactory(unittest.TestCase):
    def test_call(self):
        o = OperationFactory()
        data = {
            "app": "echo",
            "args": {"value": "hello"},
        }

        a = o.get_operation("call", data)
        self.assertEqual(a.run(None), "hello")
