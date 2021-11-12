class AppRunException(Exception):
    """All runtime errors happen here. They appear when the App.run() method is run"""

    def __init__(self, app_str, message="Oops, something went wrong"):
        self.message = f"Runtime error in '{app_str}': " + self.message
        super().__init__(self.message)
