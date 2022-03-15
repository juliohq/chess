from PySide6.QtWidgets import QGroupBox, QVBoxLayout

from .move_table import MoveTable


class Moves(QGroupBox):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Moves", *args, **kwargs)
        self.layout = QVBoxLayout(self)
        self.table = MoveTable()
        
        self.layout.addWidget(self.table)
