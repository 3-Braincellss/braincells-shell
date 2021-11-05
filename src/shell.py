"""
Shell class where the code execution starts.
All major "Shell" logic happens here.
"""


class Shell:
    prefix = "~~> "

    def __init__(self):

        pass

    """ Starts up the shell """

    def run(self):

        while true:
            text = input(self.prefix)

            print(text)


if __name__ == "__main__":
    sh = Shell()
    sh.run()
