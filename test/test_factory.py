import unittest

from operations.operation_factory import OperationFactory
from operations.call import Call
from operations.pipe import Pipe


class TestFactory(unittest.TestCase):
    def test_call(self):
        o = OperationFactory()

        data = {
            "app": "echo",
            "args": {"value": "hello"},
        }

        a = o.get_operation("call", data)
        self.assertEqual(a.run(None), "hello")

    def test_pipe(self):
        o = OperationFactory()

        call_data = {"app": "echo", "args": {"value": "hello"}}

        data = {
            "op1": o.get_operation("call", call_data),
            "op2": o.get_operation("call", call_data),
        }

        op = o.get_operation("pipe", data)

        res = op.run(None)
        assertEquals(res, "hello")
