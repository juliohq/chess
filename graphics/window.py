import pygame
from pygame import *


class Window:
    def __init__(self, width=800, height=400, fill=(0, 0, 0)):
        self.width = width
        self.height = height
        self.fill = fill
        self.screen = pygame.display.set_mode((width, height))
    
    def main(self):
        while True:
            self.screen.fill(self.fill)
            pygame.display.flip()