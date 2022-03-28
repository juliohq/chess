import sys

import chess
import cli
from chesspy import *
from graphics import *


class Game:
    def __init__(self):
        if len(sys.argv) > 1:
            result = cli.main()

            play_as = result.play_as.lower()
            ai = result.ai.lower()
            if "fen" in result:
                fen = result.fen

            if play_as in ["w", "white"]:
                game = CLIGame(chess.WHITE, result.chess960, ai, fen if fen else chess.STARTING_FEN)
            elif play_as in ["b", "black"]:
                game = CLIGame(chess.BLACK, result.chess960, ai, fen if fen else chess.STARTING_FEN)
        else:
            self.chess_game = ChessGame()

            self.game_window = GameWindow()
            self.game_window.run()

        game.start()
