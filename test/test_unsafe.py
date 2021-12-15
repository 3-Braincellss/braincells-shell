from shell_test_interface import ShellTestCase

from apps import LsApp, UnsafeApp


class TestUnsafe(ShellTestCase):
    def test_unsafe_no_error(self):
        expected = sorted([
            "dir_empty", "dir_files", "dir_nested", "dir_out", "no_extension",
            "other_extension.py", "toplevel.txt"
        ])
        out = []
        app = LsApp([])
        unsafe_app = UnsafeApp(app)
        unsafe_app.run(None, out)
        self.assertEqual(out, expected)

    def test_unsafe_error_message(self):
        expected = [
            "(\'ls\', \"[Errno 2] No such file or directory: \'where_am_i\'\")"
        ]
        out = []
        app = LsApp(["where_am_i"])
        unsafe_app = UnsafeApp(app)
        unsafe_app.run(None, out)
        self.assertEqual(out, expected)
