from chess import *
from qt import *
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QThread
import sys


class Game:
    def __init__(self):
        self.game_window = None
        
        thread = QThread()
        
        self.app = QApplication(sys.argv)
        self.window = Window()
        self.app.exec()