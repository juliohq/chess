import unittest

import chess
from chesspy.ai.weakfish import Weakfish


class TestWeakfish(unittest.TestCase):
    def test_weakfish_rate_equal(self):
        weakfish = Weakfish()

        board = chess.Board()
        board.turn = chess.WHITE

        e2e4 = weakfish.rate(board, chess.Move.from_uci("e2e4"))
        board.push_uci("e2e4")
        board.pop()
        a2a3 = weakfish.rate(board, chess.Move.from_uci("a2a3"))

        self.assertEqual(e2e4, a2a3)

    def test_weakfish_rate_greater(self):
        weakfish = Weakfish()

        board = chess.Board()
        board.turn = chess.WHITE

        g1f3 = weakfish.rate(board, chess.Move.from_uci("g1f3"))
        board.push_uci("e2e4")
        board.pop()
        e2e4 = weakfish.rate(board, chess.Move.from_uci("e2e4"))

        self.assertGreater(g1f3, e2e4)


if __name__ == "__main__":
    unittest.main()
