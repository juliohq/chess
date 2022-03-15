from PySide6.QtWidgets import *

from .game import Moves


class Window(QMainWindow):
    def __init__(self):
        super().__init__(windowTitle="Chess")
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.setCentralWidget(self.widget)
        self.setup_ui()
        self.show()

    def setup_ui(self):
        self.moves = Moves()
        
        self.layout.addWidget(self.moves)
