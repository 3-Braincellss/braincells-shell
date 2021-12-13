from collections import deque

from shell_test_interface import ShellTestCase

from apps import ClearApp
from exceptions import ContextError


class TestClear(ShellTestCase):
    """ In order to properly test shell we have to
    access previous terminal command history, which
    is a big pain and something that can't be done
    consistently across different terminal emulators.
    
    So we just check that argument validation works as intended
    and that clear doesn't raise any errors.
    """
    def test_clear_run(self):
        args = []
        app = ClearApp(args)
        out = app.run(None, deque())
        # check that nothing is output
        self.assertFalse(out)

    def test_arg_validation(self):
        args = ['a', 'b', 'hello']
        app = ClearApp(args)

        with self.assertRaises(ContextError):
            app.validate_args()

    def test_arg_validation_no_args(self):
        # we just check that it run smoothly
        # without raising any errors
        args = []
        app = ClearApp(args)
        app.validate_args()
