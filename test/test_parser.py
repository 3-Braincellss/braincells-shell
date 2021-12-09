from hypothesis import given, strategies as st
import unittest
from shellparser import parser
from operations import Call, Sequence, Pipe
from exceptions import ShellSyntaxError
from shell_test_interface import ShellTestCase
import os


class TestParser(ShellTestCase):
    def test_command(self):
        out = parser.run_parser("echo ")
        self.assertIsInstance(out, Call)

    def test_seq(self):
        out = parser.run_parser("echo ; echo ")
        self.assertIsInstance(out, Sequence)

    def test_pipe(self):
        out = parser.run_parser("echo | echo ")
        self.assertIsInstance(out, Pipe)

    def test_redirects(self):
        out = parser.run_parser("echo < file1 > file2")
        self.assertIsInstance(out, Call)

    def test_singlequote(self):
        out = parser.run_parser("echo \' text \'")
        self.assertIsInstance(out, Call)

    def test_doublequote(self):
        out = parser.run_parser("echo \" text \"")
        self.assertIsInstance(out, Call)

    def test_backquote_call(self):
        out = parser.run_parser("echo \"`echo text`\"")
        self.assertIsInstance(out, Call)

    def test_raisesyntaxerror(self):
        with self.assertRaises(ShellSyntaxError):
            parser.run_parser(";")