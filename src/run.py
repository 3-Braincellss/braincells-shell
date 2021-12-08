import sys

from shell import Shell
from shellprompt.shellsession import ShellSession

if __name__ == "__main__":
    ARGS_NUM = len(sys.argv) - 1

    if ARGS_NUM > 0:
        if ARGS_NUM != 2:
            raise ValueError("wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {sys.argv[1]}")

        sh = Shell()
        out = sh.execute(sys.argv[2])
        while len(out) > 0:
            print(out.popleft())
    else:
        session = ShellSession()
        session.run()
    
