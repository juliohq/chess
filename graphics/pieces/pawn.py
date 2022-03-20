import os

import pygame

from .piece_2d import Piece2D


class Pawn(Piece2D):
    def __init__(self):
        super().__init__(
            pygame.image.load(os.path.join("assets", "sprites", "16x32", "W_Pawn.png")),
            (0, -16),
        )
