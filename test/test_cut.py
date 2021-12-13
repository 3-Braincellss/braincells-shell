from shell_test_interface import ShellTestCase

from apps import CutApp
from exceptions import ContextError, RunError

IPSUM_MAX = 592
TEST_TEXT_PATH = "./dir_files/file-5"


class TestCut(ShellTestCase):
    def test_cut(self):
        expected = ["AAA", "BBB", "DDD", "I d"]
        app = CutApp(["-b", "1-3", TEST_TEXT_PATH])
        app.validate_args()
        out = []
        app.run(None, out)
        self.assertEqual(out, expected)

    def test_cut_open_start_interval(self):
        expected = ["AAA", "BBB", "DDD", "I d"]
        app = CutApp(["-b", "-3", TEST_TEXT_PATH])
        out = []
        app.run(None, out)
        self.assertEqual(out, expected)

    def test_cut_open_end_interval(self):
        expected = ["AA", "BB", "DD", " don't know any more letters"]
        app = CutApp(["-b", "2-", TEST_TEXT_PATH])
        out = []
        app.run(None, out)
        self.assertEqual(out, expected)

    def test_cut_individual_interval(self):
        expected = ["AA", "BB", "DD", "Idn"]
        out = []
        CutApp(["-b", "1,3,5", TEST_TEXT_PATH]).run(None, out)
        self.assertEqual(out, expected)

    def test_cut_open_interval(self):
        expected = ["AAA", "BBB", "DDD", "I don't know any more letters"]
        out = []
        CutApp(["-b", "-", TEST_TEXT_PATH]).run(None, out)
        self.assertEqual(out, expected)

    def test_cut_input_redirection(self):
        expected = ["AA", "BB", "DD", "Idn"]
        out = []
        CutApp(["-b", "1,3,5"]).run(["AAA", "BBB", "DDD",
                                     "I don't know any more letters"], out)
        self.assertEqual(out, expected)

    def test_decreasing_interval_raises_exception(self):
        with self.assertRaises(RunError):
            CutApp(["-b", "12-9", TEST_TEXT_PATH]).run(None, [])

    def test_invalid_interval_raises_exception(self):
        with self.assertRaises(RunError):
            CutApp(["-b", "1-2-3", TEST_TEXT_PATH]).run(None, [])

    def test_non_int_interval_raises_exception(self):
        with self.assertRaises(RunError):
            CutApp(["-b", f"2.0-4", TEST_TEXT_PATH]).run(None, [])

    def test_interval_starting_with_zero_raises_exception(self):
        with self.assertRaises(RunError):
            CutApp(["-b", "0-3", TEST_TEXT_PATH]).run(None, [])

    def test_invalid_option_raises_exception(self):
        with self.assertRaises(ContextError):
            CutApp(["-s", "2-4", TEST_TEXT_PATH]).validate_args()
