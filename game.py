import logging
import sys

from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QApplication

from chess import *
from graphics import *
from qt import *


class Game(QObject):
    quit = Signal()
    
    def __init__(self):
        super().__init__()
        self.game_window = GameWindow()
        self.game_window.destroyed.connect(self.exit)
        self.quit.connect(lambda: self.game_window.stop())
        
        thread = QThread()
        thread.started.connect(self.game_window.run)
        self.game_window.moveToThread(thread)
        thread.start()
        logging.debug("Game initialized")
        
        self.app = QApplication(sys.argv)
        self.window = Window()
        logging.debug("Window initialized")
        
        self.app.exec()
        self.quit.emit()
    
    def exit(self):
        sys.exit()
