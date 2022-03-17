import logging

import pygame
from pygame import *
from PySide6.QtCore import QObject, Signal

from .board import *
from .pieces import *


class GameWindow(QObject):
    destroyed = Signal()
    
    def __init__(self, width=600, height=600, fill=(0, 0, 0)):
        super().__init__()
        self.width = width
        self.height = height
        self.fill = fill
        self.screen = pygame.display.set_mode((128, 131), SCALED)
        pygame.display.set_caption("Chess")
        self.running = True
        
        self.clock = pygame.time.Clock()
        
        self.pieces = pygame.sprite.Group()
        self.board = Board2D()
        self.visible_sprites = [
            # self.pieces,
            self.board,
        ]
        
        logging.info("Game window initialized")
    
    def stop(self):
        logging.debug("Game window was requested to close")
        self.running = False
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    logging.debug("Game window closed by pygame event")
            
            self.screen.fill(self.fill)
            
            for sprite in self.visible_sprites:
                sprite.run()
            
            pygame.display.flip()
            self.clock.tick(60)
        logging.debug("Game window closed successfully")
        self.destroyed.emit()
        return
