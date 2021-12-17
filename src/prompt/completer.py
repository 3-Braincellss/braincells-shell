"""
Shell Path Completer
====================

"""

from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.document import Document

__all__ = [
    "ShellPathCompleter",
]


class ShellPathCompleter(PathCompleter):
    """Path completer wrapper for our shell"""
    def get_completions(self, document, complete_event):
        """The original PathCompleter wasn't working quite as
        we needed it to work so we tweaked it a very tiny bit.

        It used to always take the whole input string with
        spaces as the input, and we made a wrapper to pass only
        the last word separated by space to consider for completion.
        """

        words = document.text.split(" ")
        if len(words) <= 1:
            return []

        new_text = words[-1]
        new_cursor = len(new_text)
        new_document = Document(new_text, new_cursor)

        return super().get_completions(new_document, complete_event)
