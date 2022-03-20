import logging
import random
from functools import singledispatch

import chess

from .ai_player import AIPlayer

logger = logging.getLogger(__name__)


class Plainfish(AIPlayer):
    def __init__(self, name="Plainfish"):
        super().__init__(name)

    @singledispatch
    def ask_to_move(self, board: chess.Board) -> chess.Move:
        moves = [move for move in board.legal_moves]
        return random.choice(moves)
