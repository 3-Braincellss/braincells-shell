from shell_test_interface import ShellTestCase

from apps import SortApp
from exceptions import ContextError


class TestSort(ShellTestCase):
    def test_sort(self):
        expected = ["AAA", "BBB", "DDD", "I don't know any more letters"]
        out = []
        SortApp(["dir_files/file-5"]).run(None, out)
        self.assertEqual(expected, out)

    def test_sort_redirection(self):
        expected = [
            "Have you watched peaky blinders?", "It's pretty good!",
            "Sup Surgey!"
        ]
        inp = [
            "It's pretty good!", "Sup Surgey!",
            "Have you watched peaky blinders?"
        ]
        out = []
        app = SortApp([])
        app.validate_args()
        app.run(inp, out)
        self.assertEqual(expected, out)
        pass

    def test_invalid_args_raises_exception(self):
        with self.assertRaises(ContextError):
            SortApp(["-w", "im-scared.txt"])
        pass

    def test_too_many_args_raises_an_exception(self):
        with self.assertRaises(ContextError):
            SortApp(["-r", "im-scared.txt",
                     "like_really_scared!"]).validate_args()

    def test_no_args_raises_an_exception(self):
        with self.assertRaises(ContextError):
            SortApp([]).run(None, [])

    def test_sort_reversed(self):
        expected = ["I don't know any more letters", "DDD", "BBB", "AAA"]
        out = []
        SortApp(["-r", "dir_files/file-5"]).run(None, out)
        self.assertEqual(expected, out)
        pass
