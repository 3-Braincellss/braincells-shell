"""
Configuration
=============

Our default style for prompt.

"""

__all__ = [
    "STYLE_DICT",
]

STYLE_DICT = {
    "user_host": "#A78BFA",  # [user@hostname]
    "start_path": "#4ADE80",
    "path": "#38BDF8 underline",  # "h/m/D/c/src"
    "arrow": "#60A5FA",  # ~~>
    "oper": "#A3E635",  # |, ;
    "quotes": "#FDE047",  # "", ``, ''
    "app": "#22D3EE",  # apps that are supported
    "err": "#DC2626",  # apps that aren't supported
    "space": "",
    "redir": "",
    "arg": "#38BDF8",
    "unsafe": "#F472B6",
}
