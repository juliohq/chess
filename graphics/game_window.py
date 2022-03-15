import logging

import pygame
from pygame import *
from PySide6.QtCore import QObject, Signal


class GameWindow(QObject):
    destroyed = Signal()
    
    def __init__(self, width=600, height=600, fill=(0, 0, 0)):
        super().__init__()
        self.width = width
        self.height = height
        self.fill = fill
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Chess")
        self.running = True
    
    def stop(self):
        logging.debug("Game window was requested to quit")
        self.running = False
    
    def run(self):
        while self.running:
            self.screen.fill(self.fill)
            pygame.display.flip()
        logging.debug("Game window quitted successfully")
        pygame.quit()
        self.destroyed.emit()
