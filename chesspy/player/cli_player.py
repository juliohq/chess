import logging

from .human_player import HumanPlayer

logger = logging.getLogger(__name__)


class CLIPlayer(HumanPlayer):
    def __init__(self, name="CLIPlayer"):
        super().__init__(name)

    def ask_to_move(self):
        move = input(": ")
        logger.debug("Move string: %s by %s", move, self)
        return move
