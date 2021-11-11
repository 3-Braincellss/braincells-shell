import unittest
from apps.echo import EchoApp


class TestEchoApp(unittest.TestCase):
    def test_echo_on_single_word(self):
        args = {values: ["hello"]}
        echo = EchoApp(args)
        out = echo.run()
        assertEqual(out, "hello")

    def test_echo_on_multiple_words(self):
        args = {values: ["hello", "world"]}
        echo = EchoApp(args)
        out = echo.run()
        assertEqual(out, "hello world")

    def test_echo_on_nothing(self):
        args = {values: [""]}
        echo = EchoApp(args)
        out = echo.run()
        assertEqual(out, "")



if __name__ == "__main__":
    unittest.main()
