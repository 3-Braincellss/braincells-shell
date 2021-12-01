from apps.app import App
from exceptions import AppContextException
from exceptions import AppRunException


class UnsafeApp(App):
    def __init__(self, app):
        self.app = app

    def run(self, inp, out):
        try:
            out = self.app.run(inp, out)
            return out
        # except AppContextException as e:
        #     out.append(e.message)
        #     return out
        # except AppRunException as e:
        #     out.append(e.message)
        #     return out
        except Exception as e:
            out.append(str(e))
            return out

    def validate_args(self):
        pass
