from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.document import Document


class ShellPathCompleter(PathCompleter):
    def get_completions(self, document, complete_event):
        words = document.text.split(" ")
        if len(words) <= 1:
            return []
            
        new_text = words[-1]
        new_cursor = len(new_text)
        new_document = Document(new_text, new_cursor)

        return super().get_completions(new_document, complete_event)
