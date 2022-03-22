import logging
import random
from functools import singledispatch
from typing import Dict

import chess

from .ai_player import AIPlayer
from .rules import VALUES

logger = logging.getLogger(__name__)


class Kingfish(AIPlayer):
    def __init__(self, name="Kingfish", level=1, depth=2):
        super().__init__(name)
        self.depth = depth

    @singledispatch
    def ask_to_move(self, board: chess.Board) -> chess.Move:
        moves = [move for move in board.legal_moves]
        random.shuffle(moves)

        def best_move(move: chess.Move) -> float:
            piece_type = board.piece_type_at(move.from_square)
            ret: float = 0
            if piece_type in VALUES:
                ret = VALUES[piece_type]
            return ret

        result = max(moves, key=best_move)

        return result
