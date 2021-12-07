from hypothesis import given, strategies as st
import unittest
from exceptions import AppNotFoundError
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
    AppFactory
)


class TestAppFactory(unittest.TestCase):

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
        factory = AppFactory()
        for app in self.apps:
            new_app = factory.get_app(app, self.apps[app][1])
            self.assertTrue(isinstance(new_app, self.apps[app][0]))

    def test_get_unsafe_application(self):
        factory = AppFactory()
        for app in self.apps:
            new_app = factory.get_app("_" + app, self.apps[app][1])
            self.assertTrue(isinstance(new_app, UnsafeApp)
                            and isinstance(new_app.app, self.apps[app][0]))

    def test_non_existent_app(self):
        factory = AppFactory()
        with self.assertRaises(AppNotFoundError):
            factory.get_app("bad_app", ["dummy", "args"])
