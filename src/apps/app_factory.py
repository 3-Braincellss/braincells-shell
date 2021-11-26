from apps import (
    App,
    LsApp,
    EchoApp,
    CdApp,
    CatApp,
    CutApp,
    PwdApp,
    HeadApp,
    TailApp,
    SortApp,
    GrepApp,
    UniqApp,
    UnsafeApp,
)
from exceptions import AppNotFoundException, AppContextException
from common.tools import simple_globbing


class AppFactory:
    """
    Creates an app object given the app_str
    """

    def __init__(self):
        self.apps = {
            "ls": LsApp,
            "echo": EchoApp,
            "pwd": PwdApp,
            "cd": CdApp,
            "cat": CatApp,
            "head": HeadApp,
            "tail": TailApp,
            "grep": GrepApp,
            "cut": CutApp,
            # "find": self._find,
            "uniq": UniqApp,
            "sort": SortApp,
        }

        # Apps that don't require globbing
        self.no_glob = set(
            "find",
        )

    def get_app(self, app_str: str, args: list) -> App:
        """
        Returns an app object based on the app_str given.
        :param app_str: The string name of the app being requested.
        :param args: Array of all the options and arguments for the app.
        :return app:
        """
        unsafe = False
        if app_str[0] == "_":
            app_str = app_str[1:]
            unsafe = True
        if app_str in self.apps:
            # conditional globbing to take in account for functions like 'find'
            
            if not app_str in self.no_glob:
                args = simple_globbing(args)
                
            try:
                app = self.apps[app_str](args)
            except AppContextException as ace:
                raise ace

            if unsafe:
                app = UnsafeApp(app)
            else:
                app.validate_args()
            return app

            
        else:
            raise AppNotFoundException(app_str)

