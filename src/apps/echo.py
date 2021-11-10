from apps.app import App


class EchoApp(App):
    """
    """

    def __init__(self, args):
        self.args = args

    def run(self, text):
        """
        """
        text = self.args["value"]
        return text

    def validate_args(self):
        pass
