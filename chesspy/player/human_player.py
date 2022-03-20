from .player import Player


class HumanPlayer(Player):
    def __init__(self, name="Human Player"):
        super().__init__(name)
