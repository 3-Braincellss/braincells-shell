import unittest
from apps.cut import CutApp


class TestCutApp(unittest.TestCase):

    def setUp(self):
        with open("some_text.txt", "w") as f:
            f.write("Lorem ipsum dolor sit amet \n consectetur adipiscing elit. ")

    def test_singleton_range(self):
        args = ["-b", "2", "some_text.txt"]
        cut = CutApp(args)
        stdout = cut.run(None)
        assertEqual(stdout,"Lrem ipsum dolor sit amet \n consectetur adipiscing elit. " )

    def test_range(self):
        args = ["-b", "2-5", "some_text.txt"]
        cut = CutApp(args)
        stdout = cut.run(None)
        assertEqual(stdout,"L ipsum dolor sit amet \n consectetur adipiscing elit. " )


    def test_multiple_singletons(self):
        args = ["-b", "2,9", "some_text.txt"]
        cut = CutApp(args)
        stdout = cut.run(None)
        assertEqual(stdout,"L ipum dolor sit amet \n consectetur adipiscing elit. " )
        pass

    def test_multiple_ranges(self):
        args = ["-b", "2-5,68-74", "some_text.txt"]
        cut = CutApp(args)
        stdout = cut.run(None)
        assertEqual(stdout,"L im dolor sit amet \n consectetur adipiscing elit. " )
        pass

    def test_mixed_ranges(self):
        args = ["-b", "2,8-10", "some_text.txt"]
        cut = CutApp(args)
        stdout = cut.run(None)
        assertEqual(stdout,"Lrem im dolor sit amet \n consectetur adipiscing elit. " )
        pass

if __name__ == "__main__":
    unittest.main()
