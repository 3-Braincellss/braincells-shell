"""
Run
===

This module runs the application.

1) If ``-c`` flag was provided it will execute the shell
   directly and print out the output.

2) If run normally it will start an interactive shell prompt session.

"""

import sys

from prompt import ShellSession
from shell import Shell

if __name__ == "__main__":
    ARGS_NUM = len(sys.argv) - 1

    if ARGS_NUM > 0:
        if ARGS_NUM != 2:
            raise ValueError("wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {sys.argv[1]}")
        sh = Shell()
        out = sh.execute(sys.argv[2])
        print(out)
    else:
        # just some coding here
        # this screen capture is so cool
        session = ShellSession()
        session.run()
