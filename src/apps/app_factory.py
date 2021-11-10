from ls import LsApp
from echo import EchoApp
from pwd import PwdApp
from cd import CdApp
from cat import CatApp
from head import HeadApp
from tail import TailApp
from grep import GrepApp
from cut import CutApp
from find import FindApp
from uniq import UniqApp
from sort import SortApp


class AppFactory:
    """
    Creates an app object given the app_str
    """

    def __init__(self):
        self.apps = {
            "ls": self._ls,
            "echo": self._echo,
            "pwd": self._pwd,
            "cd": self._cd,
            "cat": self._cat,
            "head": self._head,
            "tail": self._tail,
            "grep": self._grep,
            "cut": self._cut,
            "find": self._find,
            "uniq": self._uniq,
            "sort": self._sort,
        }

    @staticmethod
    def get_app(self, app_str, args):
        app = self.apps[app_str](args)
        return app

    def _ls(self, args):
        return LsApp(args)

    def _echo(self, args):
        return EchoApp(args)

    def _pwd(self, args):
        return PwdApp(args)

    def _cd(self, args):
        return CdApp(args)

    def _cat(self, args):
        return catApp(args)

    def _head(self, args):
        return headApp(args)

    def _tail(self, args):
        return TailApp(args)

    def _grep(self, args):
        return grepApp(args)

    def _cut(self, args):
        return CutApps(args)

    def _find(self, args):
        return FindApp(args)

    def _uniq(self, args):
        return UniqApp(args)

    def _sort(self, args):
        return SortApp(args)
