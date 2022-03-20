import logging
from typing import Dict

import chess

logger = logging.getLogger(__name__)


class Player:
    def __init__(self, name="", rating=None):
        self.name = name
        self.rating = rating

    def __repr__(self):
        return self.name

    def ask_to_move(self):
        logger.info("Player %s was asked to move", self)

    def give_up(self):
        pass
