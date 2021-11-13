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
        Returns an app object based on the app_str given.
        :param app_str: The string name of the app being requested.
        :param args: Array of all the options and arguments for the app.
        :return app:
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

    @classmethod
    def _ls(cls, args):
        return LsApp(args)

    @classmethod
    def _echo(cls, args):
        return EchoApp(args)

    @classmethod
    def _pwd(cls, args):
        return PwdApp(args)

    @classmethod
    def _cd(cls, args):
        return CdApp(args)

    @classmethod
    def _cat(cls, args):
        return CatApp(args)

    @classmethod
    def _head(cls, args):
        return HeadApp(args)

    @classmethod
    def _tail(cls, args):
        return TailApp(args)

    @classmethod
    def _grep(cls, args):
        return GrepApp(args)

    @classmethod
    def _cut(cls, args):
        return CutApp(args)

    @classmethod
    def _find(cls, args):
        return FindApp(args)

    @classmethod
    def _uniq(cls, args):
        return UniqApp(args)

    @classmethod
    def _sort(cls, args):
        return SortApp(args)
