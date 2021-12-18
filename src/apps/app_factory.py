"""
App Factory
===========
Module for creating applications.
"""
from apps import (App, CatApp, CdApp, ClearApp, CutApp, EchoApp, FindApp,
                  GrepApp, HeadApp, LsApp, MkdirApp, PwdApp, RmApp, SortApp,
                  TailApp, UniqApp, UnsafeApp)
from common.tools import simple_globbing
from exceptions import AppNotFoundError


class AppFactory:
    """A class used to create app objects"""

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
        "clear": ClearApp,
        "mkdir": MkdirApp,
        "rm": RmApp,
    }
    """(:obj:`dict`): A dictionary that maps app names to their classes"""

    no_glob = set(["find"])
    """set: A set of apps that don't require globbing"""
    @staticmethod
    def get_app(app_str: str, opts: list) -> App:
        """Returns an app object based on the app_str given.

        Args:
            app_str (:obj:`str`): A string that represents the command
                to be called. If app_str starts with '_' the app will
                be treated as unsafe
            opts (:obj:`list`): A List of arguments that should be
                passed to the app.

        Returns:
            App: An app object that is ready to be run

        Raises:
            AppNotFoundError: If an app that doesn't exist is requested for.
        """
        # check if an app is unsafe
        unsafe = app_str[0] == "_"
        temp_app = app_str[1:] if unsafe else app_str

        if temp_app in AppFactory.apps:
            # conditional globbing to take in account for functions like 'find'
            if temp_app not in AppFactory.no_glob:
                opts = simple_globbing(opts)

            # initialise app using the constructors dictionary
            raw_app = AppFactory.apps[temp_app](opts)

            # Apply the decorator if it's unsafe
            app = UnsafeApp(raw_app) if unsafe else raw_app
            return app

        else:
            raise AppNotFoundError(temp_app)
