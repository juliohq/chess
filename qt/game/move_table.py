from PySide6.QtWidgets import QTableWidget


class MoveTable(QTableWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Player #1", "Player #2"])
