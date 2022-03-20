import unittest

import cli


class CLITest(unittest.TestCase):
    def test_play_as(self):
        res = cli.main(["--play-as", "white"])
        self.assertEqual(res.play_as, "white")

        res = cli.main(["--play-as", "black"])
        self.assertEqual(res.play_as, "black")

        res = cli.main(["--play-as", "w"])
        self.assertEqual(res.play_as, "w")

        res = cli.main(["--play-as", "b"])
        self.assertEqual(res.play_as, "b")

        res = cli.main(["--play-as", "white", "black"])
        self.assertNotEqual(res.play_as, "white")
        self.assertNotEqual(res.play_as, "black")


if __name__ == "__main__":
    unittest.main()
