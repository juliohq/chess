import logging
import random

import chess

from .ai import *
from .player import *

logger = logging.getLogger(__name__)


class ChessGame:
    def __init__(self, human=chess.WHITE, chess960=False):
        logger.debug("Creating chess game structure")

        logger.debug(
            "White player (%s) x Black player (%s)",
            self.white_player,
            self.black_player,
        )

        self.players = [self.black_player, self.white_player]

        self.board = chess.Board()
        logger.info("Chess board structure created")

        if chess960:
            self.board = self.board.from_chess960_pos(random.randint(0, 959))
            logger.info("Creating Chess960 positions")

        if human == chess.BLACK:
            self.board = self.board.mirror()
            logger.debug("Get board mirror")

        self.print_board()

    def start(self):
        logger.info("Chess game started")

    def print_board(self):
        print("\n")
        b = str(self.board)
        for k, v in chess.UNICODE_PIECE_SYMBOLS.items():
            b = b.replace(k, v)
        print(b)

    def on_player_moved(self, player: Player, move: chess.Move):
        logger.info("Player %s moved %s", player, move)
        self.board.push(move)

        logger.info("%s turn", "White" if self.board.turn == chess.WHITE else "Black")
