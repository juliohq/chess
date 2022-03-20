import logging
import random
from functools import singledispatch

import chess

from .ai_player import AIPlayer

logger = logging.getLogger(__name__)


class Clownfish(AIPlayer):
    def __init__(self, name="Clownfish"):
        super().__init__(name)

    @singledispatch
    def ask_to_move(self, board: chess.Board) -> chess.Move:
        moves = [move for move in board.legal_moves]
        return random.choice(moves)
