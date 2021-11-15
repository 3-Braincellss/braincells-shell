from apps.app import App


class CutApp(App):
    """
    """

    def __init__(self):
        pass

    def run(self):
        """
        """
        pass

    def validate_args(self):

        pass
    def validate_args(self):
        if not self.options:
            raise AppRunException(
                "cut", "Missing option: -b byte_cut_start-byte_cut_end,.. >=[")
        if len(self.options) != 1:
            raise AppRunException("cut", "Invalid number of options >=[")
        if self.options[0][0] != '-b':
            raise AppRunException(
                "cut", f"Invalid option: {self.options[0][0]}")
