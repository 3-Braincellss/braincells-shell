"""
Apps Module.

Contains all concrete apps, abstract
app interface, app factory and an unsafe
decorator
"""
from .app import App
from .ls import LsApp
from .echo import EchoApp
from .pwd import PwdApp
from .cd import CdApp
from .cat import CatApp
from .head import HeadApp
from .tail import TailApp
from .grep import GrepApp
from .cut import CutApp
from .find import FindApp
from .uniq import UniqApp
from .sort import SortApp
from .clear import ClearApp
from .unsafe import UnsafeApp
from .app_factory import AppFactory

__all__ = [
    "App",
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
    "AppFactory",
]
