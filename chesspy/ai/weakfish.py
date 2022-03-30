import logging
from functools import singledispatch

import chess

from .ai_player import AIPlayer
from .rules import *

logger = logging.getLogger(__name__)


class Weakfish(AIPlayer):
    def __init__(self, name="Weakfish", level=1, depth=3):
        super().__init__(name)
        self.depth = depth

    @singledispatch
    def ask_to_move(self, board: chess.Board) -> chess.Move:
        last_move = None
        try:
            last_move = board.peek()
        except:
            pass

        rates = []

        for move in board.legal_moves:
            board.push(move)
            rates.append((move, self.minimax(board, move, 1, -999, 999, False)))
            board.pop()

        best = min(rates, key=lambda rate: rate[1])

        return best[0]

    def evaluate(self, move: chess.Move, board: chess.Board) -> int:
        rate = 0

        # Check conditionals
        if board.is_checkmate():
            rate -= 999
        elif board.is_check():
            rate -= 400
        # Stalemate conditionals
        elif board.is_stalemate():
            rate -= 200

        # Move possibilities
        rate += board.legal_moves.count()

        # Capture conditionals
        if board.is_capture(move):
            rate += 1

        # Attacked
        if board.is_attacked_by(not board.turn, move.to_square):
            rate -= 1

        # Board control
        if move.to_square in [
            chess.D4,
            chess.E4,
            chess.D5,
            chess.F5,
        ]:
            rate += 1

        return rate

    def minimax(
        self,
        board: chess.Board,
        node: chess.Move,
        depth: int,
        alpha: int,
        beta: int,
        maximizing: bool,
    ) -> int:
        if depth == self.depth:
            return self.best(board, node)
        # breakpoint()
        if maximizing:
            max_eval = -999
            for move in board.legal_moves:
                value = self.minimax(board, move, depth + 1, alpha, beta, False)
                max_eval = max([max_eval, value])
                alpha = max([alpha, value])
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = 999
            for move in board.legal_moves:
                value = self.minimax(board, move, depth + 1, alpha, beta, True)
                min_eval = min([min_eval, value])
                beta = min([beta, value])
                if beta <= alpha:
                    break
            return min_eval

    def best(self, board: chess.Board, node: chess.Move, maximizing=True) -> int:
        rates = [self.evaluate(move, board) for move in board.legal_moves]

        if maximizing:
            return max(rates)
        else:
            return min(rates)
