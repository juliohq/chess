from PySide6.QtWidgets import QTableWidgetItem


class Move(QTableWidgetItem):
    def __init__(self, move="", *args, **kwargs):
        super().__init__(text=move, *args, **kwargs)
