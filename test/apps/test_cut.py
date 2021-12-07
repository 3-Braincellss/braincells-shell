from hypothesis import given, strategies as st
import unittest
import os
from apps import CutApp
from common.tools import read_lines_from_file
from exceptions import RunError, ContextError

IPSUM_MAX = 592
TEST_TEXT_PATH = "lorem_ipsum.txt"


class TestCut(unittest.TestCase):

    def setUp(self):
        with open(TEST_TEXT_PATH, "w") as file:
            file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce enim quam, imperdiet nec est nec, elementum placerat lorem. Suspendisse tempus pretium velit ac porttitor. Nullam suscipit, mi lobortis mattis pulvinar, sem ex euismod magna, vitae fringilla arcu turpis sit amet massa. Vivamus vel nisi sed augue malesuada consequat vel quis ex. Duis feugiat vestibulum mi posuere dictum. Nunc in interdum lacus, eu fermentum leo. Mauris eu purus quis urna pharetra elementum. Pellentesque nec nulla in magna blandit lobortis.\
            Phasellus ultrices imperdiet purus, vel volutpat risus vestibulum id. Praesent ut mauris feugiat, faucibus ligula at, suscipit odio. Nam eros urna, commodo vel vehicula id, accumsan a purus. Morbi enim tortor, faucibus quis dolor sit amet, iaculis congue felis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum interdum tristique convallis. Ut sodales magna maximus accumsan mattis. In facilisis tempor justo, non ullamcorper dui maximus non. Nam tincidunt suscipit arcu, a eleifend diam luctus quis.\
            Duis ex magna, sollicitudin non sodales in, elementum in odio. Nullam quis efficitur diam, quis convallis libero. Vestibulum auctor libero ac risus laoreet imperdiet. In aliquet mi sit amet ante porttitor, non ultrices tellus sagittis. Phasellus elementum arcu eu erat pharetra, eget lobortis augue vulputate. Fusce dapibus a sapien non accumsan. Suspendisse semper ultrices neque in tempus. Cras augue turpis, tempor sed quam vel, imperdiet lacinia justo. Praesent sed sollicitudin quam. Duis aliquet elit nulla, at auctor ex congue id. Vestibulum et diam a est imperdiet semper non id orci. Pellentesque fringilla elit vel tempus aliquet. Fusce in urna vel velit egestas finibus sit amet ac felis.\
            Etiam volutpat eu mauris in tincidunt. Nullam faucibus venenatis mauris. Nam at ligula sit amet nisi malesuada cursus. Nunc eu scelerisque libero. Sed blandit fringilla elit quis condimentum. Quisque eu magna eu justo ultricies ullamcorper. Cras vitae fermentum lectus, vel volutpat nibh. Sed congue turpis lacinia eros porta venenatis. Nunc vitae arcu mollis, ornare dui quis, tincidunt tortor. Morbi sollicitudin magna at finibus vehicula. Donec fermentum magna et odio congue, eu rutrum nisi imperdiet. Nulla porttitor pulvinar urna et volutpat. Ut dictum lacus et enim dignissim pulvinar.\
            Vivamus tellus dui, elementum eget quam nec, ultrices tempus enim. Phasellus blandit nibh vitae molestie fermentum. Morbi in leo sapien. Nullam tincidunt quis enim at bibendum. Maecenas est velit, suscipit et pellentesque a, lobortis id lectus. Etiam sed sem eget nisl feugiat tincidunt. Proin accumsan sit amet lectus sit amet convallis. In hac habitasse platea dictumst. Morbi et volutpat odio. Donec et eros ut lectus tempus fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam in pulvinar erat. Suspendisse efficitur eros ut risus mollis auctor. Pellentesque nec laoreet sapien."
                       )

    def tearDown(self):
        os.remove(TEST_TEXT_PATH)

    @given(st.integers(1, IPSUM_MAX), st.integers(1, IPSUM_MAX))
    def test_cut(self, x, y):
        interval = (min(x, y), max(x, y))
        lines = read_lines_from_file(TEST_TEXT_PATH, "cut_test")
        expected = [(lambda line: line[interval[0] - 1:interval[1]].rstrip())(line)
                    for line in lines]
        args = ["-b", f"{interval[0]}-{interval[1]}", TEST_TEXT_PATH]
        app = CutApp(args)
        out = []
        out = app.run(None, out)
        self.assertEqual(out, expected)

    @given(st.integers(1, IPSUM_MAX))
    def test_cut_open_start_interval(self, x):
        lines = read_lines_from_file(TEST_TEXT_PATH, "cut_test")
        expected = [(lambda line: line[:x].rstrip())(line)
                    for line in lines]
        args = ["-b", f"-{x}", TEST_TEXT_PATH]
        app = CutApp(args)
        out = []
        out = app.run(None, out)
        self.assertEqual(out, expected)

    @given(st.integers(1, IPSUM_MAX))
    def test_cut_open_end_interval(self, x):
        lines = read_lines_from_file(TEST_TEXT_PATH, "cut_test")
        expected = [(lambda line: line[x - 1:].rstrip())(line)
                    for line in lines]
        args = ["-b", f"{x}-", TEST_TEXT_PATH]
        app = CutApp(args)
        out = []
        out = app.run(None, out)
        self.assertEqual(out, expected)

    def test_cut_open_interval(self):
        lines = read_lines_from_file(TEST_TEXT_PATH, "cut_test")
        expected = [(lambda line: line.rstrip())(line)
                    for line in lines]
        args = ["-b", "-", TEST_TEXT_PATH]
        app = CutApp(args)
        out = []
        out = app.run(None, out)
        self.assertEqual(out, expected)

    @given(st.integers(1, IPSUM_MAX), st.integers(1, IPSUM_MAX))
    def test_cut_input_redirection(self, x, y):
        interval = (min(x, y), max(x, y))
        lines = read_lines_from_file(TEST_TEXT_PATH, "cut_test")
        expected = [(lambda line: line[interval[0] - 1:interval[1]].rstrip())(line)
                    for line in lines]
        args = ["-b", f"{interval[0]}-{interval[1]}"]
        app = CutApp(args)
        out = []
        out = app.run(lines, out)
        self.assertEqual(out, expected)

    @given(st.integers(1, IPSUM_MAX), st.integers(1, IPSUM_MAX))
    def test_decreasing_interval_raises_exception(self, x, y):
        if x == y:
            return
        interval = (max(x, y), min(x, y))
        args = ["-b", f"{interval[0]}-{interval[1]}", TEST_TEXT_PATH]
        app = CutApp(args)
        with self.assertRaises(RunError):
            app.run(None, [])

    @given(st.integers(0, 0), st.integers(1, IPSUM_MAX))
    def test_interval_starting_with_zero_raises_exception(self, x, y):
        if x == y:
            return
        interval = (x, y)
        args = ["-b", f"{interval[0]}-{interval[1]}", TEST_TEXT_PATH]
        app = CutApp(args)
        with self.assertRaises(RunError):
            app.run(None, [])

    @given(st.from_regex("(A|a|[c-z]|[C-Z])", fullmatch=True))
    def test_invalid_option_raises_exception(self, char):
        args = ["-{char}", f"{0}-{10}", TEST_TEXT_PATH]
        with self.assertRaises(ContextError):
            CutApp(args)
