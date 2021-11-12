from apps.app import App

from apps.ls import LsApp
from apps.echo import EchoApp
from apps.pwd import PwdApp
from apps.cd import CdApp
from apps.cat import CatApp
from apps.head import HeadApp
from apps.tail import TailApp
from apps.grep import GrepApp
from apps.cut import CutApp
from apps.find import FindApp
from apps.uniq import UniqApp
from apps.sort import SortApp

from exceptions.app_not_found import AppNotFoundException
from exceptions.app_context import AppContextException


class AppFactory:
    """
    Creates an app object given the app_str
    """

    def __init__(self):
        self.apps = {
            "ls": self._ls,
            "echo": self._echo,
            # "pwd": self._pwd,
            "cd": self._cd,
            # "cat": self._cat,
            # "head": self._head,
            # "tail": self._tail,
            # "grep": self._grep,
            # "cut": self._cut,
            # "find": self._find,
            # "uniq": self._uniq,
            # "sort": self._sort,
        }

    def get_app(self, app_str: str, args: list) -> App:
        """
        app_str - app name
        args = [array, of, strings, which, are, all, options]
        """
        if app_str in self.apps:
            try:
                app = self.apps[app_str](args)
                app.validate_args()
                return app
            except AppContextException as ace:
                raise ace
        else:
            raise AppNotFoundException(app_str)

    def _ls(self, args):
        return LsApp(args)

    def _echo(self, args):
        return EchoApp(args)

    def _pwd(self, args):
        return PwdApp(args)

    def _cd(self, args):
        return CdApp(args)

    def _cat(self, args):
        return CatApp(args)

    def _head(self, args):
        return HeadApp(args)

    def _tail(self, args):
        return TailApp(args)

    def _grep(self, args):
        return GrepApp(args)

    def _cut(self, args):
        return CutApps(args)

    def _find(self, args):
        return FindApp(args)

    def _uniq(self, args):
        return UniqApp(args)

    def _sort(self, args):
        return SortApp(args)
