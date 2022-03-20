import logging
import random
from functools import singledispatch
from typing import List, Optional

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
        fake_board.turn = board.turn
        logger.debug("Fake board FEN: %s", board.fen())

        tree = Tree()

        last_move = None
        try:
            last_move = board.peek()
        except:
            pass
        root = tree.create_node(
            last_move.uci() if last_move else "root",
            last_move.uci() if last_move else "root",
            data=last_move,
        )

        result = None
        depth_achieved = False
        # fake_root = root
        # current_depth_moves: List[chess.Move] = []

        while not depth_achieved:
            last_node: Node = None
            
            breakpoint()
            tree.show()
            # Navigate though the current tree from the root
            logger.debug("Navigating though the tree")
            for node in tree.expand_tree(last_node):
                # Set last node
                last_node = n.predecessor(tree) if last_node else root
                logger.debug("Set last_node to %s", last_node)
                
                # Check the tree depth
                if tree.depth() >= self.depth:
                    logger.debug("Tree achieved the target depth")
                    depth_achieved = True
                    break
                
                logger.debug("Current node %s", node)
                
                # Get possible moves
                moves = [move for move in fake_board.legal_moves]
                logger.debug("Get possible moves")
                
                # Add possible moves
                for move in moves:
                    uci = move.uci()
                    n = tree.create_node(uci, parent=last_node if last_node else root)
                    logger.debug(uci)
                logger.debug("Possible moves added")
            breakpoint()

        # for depth in range(self.depth):
        #     # Find moves for current state (White or Black)
        #     moves = [move for move in fake_board.legal_moves]

        #     # Populate current depth
        #     logger.debug("Populating depth #%s", depth)
        #     for move in moves:
        #         pdb.set_trace()
        #         tree.create_node(move.uci(), parent=fake_root, data=move)
        #     logger.debug("Move count: %s", len(moves))

        #     breakpoint()
        #     # Go deeper in the tree
        #     if len(tree.children(fake_root.identifier)) == len(current_depth_moves):
        #         current_depth_moves.clear()
        #         fake_board.pop()
        #         fake_root = fake_root.predecessor(tree.identifier)

        #     fake_root = random.choice(tree.children(fake_root))
        #     fake_board.push(fake_root.data)
        #     current_depth_moves.append(fake_root)

        # Rate

        # Pruning
        tree.rsearch()

        # Find best move by its rating
        # tree.children()

        return result if isinstance(result, chess.Move) else random.choice(moves)

    def rate(
        self, board: chess.Board, move: chess.Move, tree: Optional[Tree] = None
    ) -> int:
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
