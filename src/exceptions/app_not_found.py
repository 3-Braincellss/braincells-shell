

class AppNotFoundException(Exception):
    def __init__(self, app_str):
        self.app_str = app_str
        self.message = f"Command '{self.app_str}' doesn't exist. Sorry :( \n"
        super().__init__(self.message)
