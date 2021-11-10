from apps.app import App


class EchoApp(App):
    """
    """

    def __init__(self, args):
        self.args = args

    def run(self, text=None):
        """
        """
        out = self.args["value"]
        return out

    def validate_args(self):
        pass
