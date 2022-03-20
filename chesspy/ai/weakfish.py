import logging
from functools import singledispatch
from typing import Dict, List

import chess
from treelib import Node, Tree

from .ai_player import AIPlayer
from .rules import *

logger = logging.getLogger(__name__)


class Weakfish(AIPlayer):
    def __init__(self, name="Weakfish", level=1, depth=3):
        super().__init__(name)
        self.depth = depth

    @singledispatch
    def ask_to_move(self, board: chess.Board) -> chess.Move:
        fake_board = chess.Board(board.fen())
        logger.debug("Fake board FEN: %s", board.fen())

        tree = Tree()

        last_move = None
        try:
            last_move = board.peek()
        except:
            pass

        tree.create_node(
            last_move.uci() if last_move else "root",
            data=last_move,
        )

        result = None

        while True:
            leave_count = 0
            depth_leaves_count = 0

            for leave in tree.leaves():
                leave_count += 1

                if tree.level(leave.identifier) == self.depth - 1:
                    depth_leaves_count += 1

            if depth_leaves_count == leave_count:
                logger.debug("Tree depth achieved")
                break

            # Navigate though the current tree from the root
            logger.debug("Navigating though the tree")

            # breakpoint()

            for leave in tree.leaves():
                # Check the leave depth
                if tree.level(leave.identifier) >= self.depth - 1:
                    logger.debug("Leave %s is out of the target depth", leave)
                    continue

                logger.debug("Current node %s", leave)

                # breakpoint()

                # Push move
                if not leave.is_root():
                    try:
                        fake_board.pop()
                    except:
                        pass

                    fake_board.push(leave.data)
                    logger.debug("Pushed %s", leave.data)

                # breakpoint()

                # Get possible moves
                moves = [move for move in fake_board.legal_moves]
                logger.debug("Get possible moves")

                # Add possible moves
                for move in moves:
                    uci = move.uci()
                    tree.create_node(
                        uci,
                        parent=leave,
                        data=move,
                    )
                    logger.debug(uci)
                logger.debug("Possible moves added")

                # Check overall tree depth
                logger.debug("Check overall tree depth")

        # Rate
        ratings: Dict[str, int] = {}
        while tree.depth() > 1:
            leaves: List[Node] = tree.leaves()

            for leave in leaves:
                if tree.level(leave.identifier) == 1:
                    logger.debug("Rating finished")
                    breakpoint()
                    break
                else:
                    pid = leave.predecessor(tree.identifier)
                    # breakpoint() # pid, len(tree)
                    tree.remove_node(leave.identifier)
                    # breakpoint() # len(tree)

                    rate = self.rate(fake_board, leave.data)
                    # breakpoint() # rate

                    if not pid in ratings:
                        ratings[pid] = 0
                    ratings[pid] += rate
                    # breakpoint() # ratings

        # Find best move by its rating
        def get_rate(node: Node) -> int:
            return ratings[node.identifier]

        result = max(tree.leaves(), key=get_rate).data

        return result

    def rate(self, board: chess.Board, move: chess.Move) -> int:
        rate = 0

        board.push(move)

        # Check conditionals
        if board.is_checkmate():
            rate += 1
        else:
            rate -= 1
        if board.is_check():
            rate += 1
        else:
            rate -= 1

        # Stalemate conditionals
        if board.is_stalemate():
            rate -= 1
        else:
            rate += 1

        # Move possibilities
        rate -= len([move for move in board.legal_moves])

        board.pop()

        # Capture conditionals
        if board.is_capture(move):
            piece_type = board.piece_type_at(move.to_square)

            if piece_type in VALUES:
                rate += VALUES[piece_type]
        else:
            rate -= 1

        # Giving check conditionals
        if board.gives_check(move):
            rate += 1

        # Attacked
        if board.is_attacked_by(not board.turn, move.to_square):
            piece_type = board.piece_type_at(move.from_square)

            if piece_type in VALUES:
                rate -= VALUES[piece_type]
        else:
            rate += 1

        # Move possibilities
        rate += len([move for move in board.legal_moves])

        # Board control
        if move.to_square in [
            chess.D4,
            chess.E4,
            chess.D5,
            chess.F5,
        ]:
            rate += 1

        return rate
