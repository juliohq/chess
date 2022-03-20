from functools import singledispatch
import logging
import os
from typing import Tuple

import chess
import pygame

from ..pieces import *

logger = logging.getLogger(__name__)


class Board2D(pygame.sprite.Sprite):
    def __init__(self):
        logger.debug("Creating Board2D")

        self.screen = pygame.display.get_surface()
        self.image = pygame.image.load(
            os.path.join("assets", "sprites", "extras", "board1.png")
        )
        self.rect = (0, 0)
        self.pieces = pygame.sprite.Group(
            Pawn(),
            Pawn(),
            Pawn(),
            Pawn(),
            Pawn(),
            Pawn(),
            Pawn(),
            Pawn(),
        )

        for piece in self.pieces:
            if piece.type == chess.PAWN:
                pass

        logger.info("Board2D created")

    def run(self):
        self.screen.blit(self.image, self.rect)
        self.pieces.draw(self.screen)

    @singledispatch
    def piece_at(self, pos: Tuple[int, int]) -> Piece2D:
        pass

    @piece_at.register
    def _(self, square: int) -> Piece2D:
        pass

    @piece_at.register
    def _(self, square: str) -> Piece2D:
        pass

    @singledispatch
    def move(self, from_square: int, to_square: int):
        pass

    @move.register
    def _(self, piece: Piece2D, to: Tuple[int, int]):
        pass
