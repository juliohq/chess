import logging

import chess
import pygame
from pygame.locals import *

logger = logging.getLogger(__name__)


class Piece2D(pygame.sprite.Sprite):
    def __init__(self, sprite=None, offset=(0, 0), type=chess.PAWN):
        super().__init__()
        self.image = sprite
        self.type = type
        self.rect = self.image.get_rect().move(*offset)

        logger.debug("Creating Piece2D with type: %s", self.piece_type)

        self.screen = pygame.display.get_surface()

    def run(self):
        pass
