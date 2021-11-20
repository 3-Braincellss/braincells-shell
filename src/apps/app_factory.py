from apps import App, LsApp, EchoApp, CdApp, CatApp, CutApp, PwdApp, HeadApp, TailApp, SortApp
from exceptions import AppNotFoundException, AppContextException


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
            # "grep": self._grep,
            "cut": self._cut,
            # "find": self._find,
            # "uniq": self._uniq,
            "sort": self._sort,
        }

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
            try:
                app = self.apps[app_str](args, unsafe)
                app.validate_args()
                return app
            except AppContextException as ace:
                raise ace
        else:
            raise AppNotFoundException(app_str)

    def _ls(self, args, unsafe):
        app = LsApp(args)
        if unsafe:
            app = UnsafeApp(app)
        return app

    def _echo(self, args, unsafe):
        app = EchoApp(args)
        if unsafe:
            app = UnsafeApp(app)
        return app

    def _pwd(self, args, unsafe):
        app = PwdApp(args)
        if unsafe:
            app = UnsafeApp(app)
        return app

    def _cd(self, args, unsafe):
        app = CdApp(args)
        if unsafe:
            app = UnsafeApp(app)
        return app

    def _cat(self, args, unsafe):
        app = CatApp(args)
        if unsafe:
            app = UnsafeApp(app)
        return app

    def _head(self, args, unsafe):
        app = HeadApp(args)
        if unsafe:
            app = UnsafeApp(app)
        return app

    def _tail(self, args, unsafe):
        app = TailApp(args)
        if unsafe:
            app = UnsafeApp(app)
        return app

    def _grep(self, args, unsafe):
        app = GrepApp(args)
        if unsafe:
            app = UnsafeApp(app)
        return app

    def _cut(self, args, unsafe):
        app = CutApp(args)
        if unsafe:
            app = UnsafeApp(app)
        return app

    def _find(self, args, unsafe):
        app = FindApp(args)
        if unsafe:
            app = UnsafeApp(app)
        return app

    def _uniq(self, args, unsafe):
        app = UniqApp(args)
        if unsafe:
            app = UnsafeApp(app)
        return app

    def _sort(self, args, unsafe):
        app = SortApp(args)
        if unsafe:
            app = UnsafeApp(app)
        return app
