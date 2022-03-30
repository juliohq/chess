from functools import singledispatch

import chess

from ..player.player import Player


class AIPlayer(Player):
    def __init__(self, name="AIPlayer"):
        super().__init__(name)

    @singledispatch
    def ask_to_move(self, board: chess.Board) -> chess.Move:
        pass
