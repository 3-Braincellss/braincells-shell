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
    FindApp,
)
from exceptions import AppNotFoundException
from common.tools import simple_globbing


class AppFactory:
    """A class that is used to create app objects"""

    apps = {
        "ls": LsApp,
        "echo": EchoApp,
        "pwd": PwdApp,
        "cd": CdApp,
        "cat": CatApp,
        "head": HeadApp,
        "tail": TailApp,
        "grep": GrepApp,
        "cut": CutApp,
        "find": FindApp,
        "uniq": UniqApp,
        "sort": SortApp,
    }
    """dict: A dictionary that maps app names to their classes"""

    no_glob = set(["find"])
    """set: A set of apps that don't require globbing"""

    @staticmethod
    def get_app(app_str: str, opts: list) -> App:
        """Returns an app object based on the app_str given.

        Args:
            app_str (obj:`str`): A string that represents the command to be called.
                If app_str starts with '_' the app will be treated as unsafe
            opts (:obj:`list`): A List of arguments that should be passed to the app.

        Returns:
            app (:obj:`App`): An app object that is ready to be run
        """

        # check if an app is unsafe
        unsafe = app_str[0] == "_"
        _app_str = app_str[1:] if unsafe else app_str

        if _app_str in AppFactory.apps:

            # conditional globbing to take in account for functions like 'find'
            if _app_str not in AppFactory.no_glob:
                opts = simple_globbing(opts)

            # initialise app using the constructors dictionary
            _app = AppFactory.apps[_app_str](opts)

            # Apply the decorator if it's unsafe
            app = UnsafeApp(_app) if unsafe else _app
            return app

        else:
            raise AppNotFoundException(_app_str)
