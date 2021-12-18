from prompt_toolkit.document import Document
from shell_test_interface import ShellTestCase

from prompt import ShellPathCompleter


class TestCompleter(ShellTestCase):
    def test_completions(self):
        completer = ShellPathCompleter()
        test_doc = Document("hello dir_", 4)

        completions = completer.get_completions(test_doc, None)
        out = []
        for each in completions:
            out.append(each.text)

        expected = set(["empty", "files", "nested", "out"])

        self.assertEqual(set(out), expected)

    def test_null_completions(self):
        completer = ShellPathCompleter()
        test_doc = Document("hello", 4)

        completions = completer.get_completions(test_doc, None)

        out = set(map(lambda x: x.text, completions))

        self.assertEqual(out, set([]))
