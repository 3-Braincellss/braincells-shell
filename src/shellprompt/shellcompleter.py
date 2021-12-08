from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.document import Document


class ShellPathCompleter(PathCompleter):
    def get_completions(self, document, complete_event):

        new_text = document.text.split(" ")[-1]
        new_cursor = len(new_text)
        new_document = Document(new_text, new_cursor)

        return super().get_completions(new_document, complete_event)
