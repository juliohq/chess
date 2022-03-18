import logging

import chess


logger = logging.getLogger(__name__)
logger.debug("Creating chess game structure")


class ChessGame:
    def __init__(self):
        logger.debug("Creating chess game structure")
        self.board = chess.Board()
        logger.info("Chess board structure created")
