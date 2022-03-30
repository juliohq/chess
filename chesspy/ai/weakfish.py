import logging
from functools import singledispatch

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
        tree = Tree()

        last_move = None
        try:
            last_move = board.peek()
        except:
            pass

        # Create root node
        tree.create_node(
            last_move.uci() if last_move else "root",
            data=(board.fen(), last_move.uci() if last_move else "none"),
        )

        self.populate(tree)

        rates = []
        children = tree.children(tree.root)

        for child in children:
            rates.append((child, self.minimax(tree, child, 1, -999, 999, False)))

        best = min(rates, key=lambda rate: rate[1])
        move = chess.Move.from_uci(best[0].data[1])

        return move

    def populate(self, tree: Tree):
        # nodes = len(tree)

        for i in range(self.depth):
            # Check the overall tree depth
            # if tree.depth() >= self.depth:
            #     break

            for leave in tree.leaves():
                # Check to see if the leave is behind (Alpha-Beta pruning)
                if tree.depth(leave) + 1 < tree.depth():
                    continue

                # Bring back board state
                b = chess.Board(leave.data[0])
                
                if b.legal_moves.count() == 0:
                    return

                # Append new moves
                for move in b.legal_moves:
                    b.push(move)
                    tree.create_node(
                        move.uci(),
                        data=(b.fen(), move.uci()),
                        parent=leave,
                    )
                    b.pop()

                    print(len(tree))

            # Check if all nodes were found
            # if len(tree) == nodes:
            #     break

    def evaluate(self, move: chess.Move, fen: str) -> int:
        rate = 0
        b = chess.Board(fen)

        next_moves = [m for m in b.legal_moves]

        # for next in next_moves:
        #     b.push(next)
        #     if b.is_checkmate():
        #         rate += 999
        #     elif b.gives_check(next):
        #         rate -= 400
        #     b.pop()

        # Check conditionals
        if b.is_checkmate():
            rate -= 999
        elif b.is_check():
            rate -= 400
        # Stalemate conditionals
        elif b.is_stalemate():
            rate -= 200

        # Move possibilities
        rate += len(next_moves)

        # Capture conditionals
        if b.is_capture(move):
            rate += 1

        # Attacked
        if b.is_attacked_by(not b.turn, move.to_square):
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

    def minimax(self, tree: Tree, node: Node, depth: int, alpha: int, beta: int, maximizing: bool) -> int:
        if depth + 1 == tree.depth():
            return self.best(tree, node)
        # breakpoint()
        if maximizing:
            max_eval = -999
            for n in tree.children(node.identifier):
                value = self.minimax(tree, n, depth + 1, alpha, beta, False)
                max_eval = max([max_eval, value])
                alpha = max([alpha, value])
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = 999
            for n in tree.children(node.identifier):
                value = self.minimax(tree, n, depth + 1, alpha, beta, True)
                min_eval = min([min_eval, value])
                beta = min([beta, value])
                if beta <= alpha:
                    break
            return min_eval

    def best(self, tree: Tree, node: Node, maximizing=True) -> int:
        children = [n for n in tree.children(node.identifier)]
        rates = [
            self.evaluate(chess.Move.from_uci(child.data[1]), child.data[0])
            for child in children
        ]

        if maximizing:
            return max(rates)
        else:
            return min(rates)
