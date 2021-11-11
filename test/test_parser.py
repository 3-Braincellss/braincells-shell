import unittest
from parser import parser


class TestShell(unittest.TestCase):
    def test_parser(self):
        tree = parser.run_parser("echo -f stuff --flag stuff2")
        print(tree.pretty())
        tree = parser.run_parser("echo /path/")
        print(tree.pretty())
        tree = parser.run_parser("echo /sdf/ > 'text.txt'")
        print(tree.pretty())
        tree = parser.run_parser("echo \"\'double quoted quote\'\"")
        print(tree.pretty())
        tree = parser.run_parser("echo \"this is space: `echo \"quotedthing\"`\"")
        print(tree.pretty())
        tree = parser.run_parser("gcc -Wall robot.c -o a.out")
        print(tree.pretty())


if __name__ == "__main__":
    unittest.main()
