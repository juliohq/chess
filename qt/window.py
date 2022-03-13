from PySide6.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.setCentralWidget(self.widget)
        self.setup_ui()
        self.show()

    def setup_ui(self):
        pass
