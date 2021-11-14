class AppContextException(Exception):
    """
    This exception is raised during TREE TRANSFORMING STAGE
    When an app is created it's validate_args() method is called
    This method will call the context exception in case some arguments don't make sense
    """

    def __init__(self, app_str, message="GO AWAY >=["):
        self.message = f"Context error in '{app_str}': " + message + "\n"
        super().__init__(self.message)
