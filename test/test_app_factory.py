from shell_test_interface import ShellTestCase

from apps import (
    AppFactory,
    CatApp,
    CdApp,
    CutApp,
    EchoApp,
    FindApp,
    GrepApp,
    HeadApp,
    LsApp,
    PwdApp,
    SortApp,
    TailApp,
    UniqApp,
    UnsafeApp,
)
from exceptions import AppNotFoundError


class TestAppFactory(ShellTestCase):

    apps = {
        "ls": [LsApp, []],
        "echo": [EchoApp, []],
        "pwd": [PwdApp, []],
        "cd": [CdApp, ["."]],
        "cat": [CatApp, ["nothing.txt"]],
        "head": [HeadApp, ["-n", "hi.txt"]],
        "tail": [TailApp, ["-n", "bye.txt"]],
        "grep": [GrepApp, ["some-pattern", "hi.txt"]],
        "cut": [CutApp, ["-b", "sup.txt"]],
        "find": [FindApp, ["-name", "*.py"]],
        "uniq": [UniqApp, ["wow.txt"]],
        "sort": [SortApp, ["biography.txt"]],
    }

    def test_get_regular_application(self):
        for app in self.apps:
            new_app = AppFactory().get_app(app, self.apps[app][1])
            self.assertTrue(isinstance(new_app, self.apps[app][0]))

    def test_get_unsafe_application(self):
        for app in self.apps:
            new_app = AppFactory().get_app("_" + app, self.apps[app][1])
            self.assertTrue(
                isinstance(new_app, UnsafeApp)
                and isinstance(new_app.app, self.apps[app][0]))

    def test_non_existent_app(self):
        with self.assertRaises(AppNotFoundError):
            AppFactory().get_app("bad_app", ["dummy", "args"])
