"""
Apps Module.

Contains all concrete apps, abstract
app interface, app factory and an unsafe
decorator
"""
from .app import App
from .cat import CatApp
from .cd import CdApp
from .clear import ClearApp
from .cut import CutApp
from .echo import EchoApp
from .find import FindApp
from .grep import GrepApp
from .head import HeadApp
from .ls import LsApp
from .mkdir import MkdirApp
from .pwd import PwdApp
from .sort import SortApp
from .tail import TailApp
from .uniq import UniqApp
from .unsafe import UnsafeApp
from .app_factory import AppFactory

__all__ = [
    "App",
    "AppFactory",
    "LsApp",
    "EchoApp",
    "PwdApp",
    "CdApp",
    "CatApp",
    "HeadApp",
    "TailApp",
    "GrepApp",
    "CutApp",
    "FindApp",
    "UniqApp",
    "SortApp",
    "ClearApp",
    "UnsafeApp",
]
