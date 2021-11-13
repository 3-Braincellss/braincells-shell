from apps.app import App


class EchoApp(App):
    """ """

    def __init__(self, args):
        self.args = args

    def run(self, inp, out):
        """ """
        out.append(" ".join(self.args) + "\n")
        return out

    def validate_args(self):
        pass
