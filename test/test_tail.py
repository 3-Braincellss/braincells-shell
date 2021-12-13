from shell_test_interface import ShellTestCase

from apps import TailApp
from exceptions import ContextError


class TestTail(ShellTestCase):
    def test_head_singlefile(self):
        app = TailApp(["dir_files/file-5"])
        out = []
        app.run(None, out)
        self.assertEqual(
            out, ["AAA", "BBB", "DDD", "I don't know any more letters"])

    def test_head_multifile(self):
        app = TailApp(["dir_files/file-5", "dir_files/file-4"])
        out = []
        app.run(None, out)
        self.assertEqual(out, [
            "\n--> dir_files/file-5 <--\n", "AAA", "BBB", "DDD",
            "I don't know any more letters", "\n--> dir_files/file-4 <--\n",
            "depression"
        ])

    def test_head_argument(self):
        app = TailApp(["-n", "1", "dir_files/file-5"])
        out = []
        app.run(None, out)
        self.assertEqual(out, ["I don't know any more letters"])

    def test_head_input(self):
        app = TailApp([])
        out = []
        app.run(["AAA", "BBB"], out)
        self.assertEqual(out, ["AAA", "BBB"])

    def test_head_input_with_arguments(self):
        app = TailApp(["-n", "1"])
        out = []
        app.run(["AAA", "BBB"], out)
        self.assertEqual(out, ["BBB"])

    def test_head_get_opt_error(self):
        with self.assertRaises(ContextError):
            TailApp(["-f", "1"])

    def test_head_validate_args(self):
        app = TailApp(["-n", "d"])
        with self.assertRaises(ContextError):
            app.validate_args()
