from apps.app import App


class EchoApp(App):
    """
    """

    def __init__(self, args):
        self.args = args

    def run(self, inp) -> str:
        """
        """
        return " ".join(self.args)

    def validate_args(self):
        pass
