from chesspy import *
from graphics import *


class Game:
    def __init__(self):
        self.chess_game = ChessGame()
        
        self.game_window = GameWindow()
        self.game_window.run()
