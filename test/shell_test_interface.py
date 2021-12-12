import os
import shutil

import unittest


class ShellTestCase(unittest.TestCase):

    TOP_LEVEL = "_test"

    DIR_TREE = {
        "dir_empty": {},
        "dir_files": {
            "file-1": "AA\nBB",
            "file-2": "Lakad Matataaag",
            "file-3": "",
            "file-4": "depression",
            "file-5": "AAA\nBBB\nDDD\nI don't know any more letters",
        },
        "dir_nested": {
            "dir_nested.txt": "A file in the nested directory",
            "nest_1": {
                "dir_nested_1.txt": "A\nB\nC\nD\n",
            },
            "nest_2": {
                "dir_nested_2.txt": "What is this?",
            }
        },
        "dir_out": {},
        "no_extension": "A file without extension",
        "other_extension.py": "# a python file",
        "toplevel.txt": "A top level text file",
    }

    def setUp(self):
        """Prepares the working environment for a single test case.

        Initialises testing directory tree and sets it as the
        current directory
        """
        try:
            os.mkdir(self.TOP_LEVEL)
        except FileExistsError:
            shutil.rmtree("_test")
            os.mkdir(self.TOP_LEVEL)

        def recur_dir(dirs, current_path):

            for key in dirs:
                path = f"{current_path}/{key}"
                if isinstance(dirs[key], dict):
                    os.mkdir(path)
                    recur_dir(dirs[key], path)

                if isinstance(dirs[key], str):
                    with open(path, "w", encoding="utf-8") as outf:
                        outf.write(dirs[key])

        recur_dir(self.DIR_TREE, self.TOP_LEVEL)

        os.chdir(self.TOP_LEVEL)

    def tearDown(self):
        """ Deletes the test directory """
        os.chdir("..")
        shutil.rmtree("_test")
