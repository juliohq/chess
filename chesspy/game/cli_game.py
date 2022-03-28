import logging

import chess
from chesspy import ChessGame
from chesspy.ai.ai_player import AIPlayer
from chesspy.ai.kingfish import Kingfish
from chesspy.ai.plainfish import Plainfish
from chesspy.ai.weakfish import Weakfish
from chesspy.player.cli_player import CLIPlayer

logger = logging.getLogger(__name__)

OPONENTS = {
    "plainfish": Plainfish,
    "weakfish": Weakfish,
    "kingfish": Kingfish,
}


class CLIGame(ChessGame):
    def __init__(
        self, human=chess.WHITE, chess960=False, ai="plainfish", fen=chess.STARTING_FEN
    ):
        oponent = OPONENTS.get(ai, Plainfish)
        if human == chess.WHITE:
            self.white_player = CLIPlayer()
            self.black_player = oponent()
        else:
            self.white_player = oponent()
            self.black_player = CLIPlayer()
        super().__init__(human, chess960, fen)

    def start(self):
        super().start()

        while True:
            player = None
            move = None
            exit = False
            while True:
                try:
                    player = self.players[int(self.board.turn)]
                    logger.debug("Get player %s", player)
                    if isinstance(player, CLIPlayer):
                        uci = player.ask_to_move()
                        if uci in ["q", "quit", "exit"]:
                            exit = True
                            break
                        move = chess.Move.from_uci(uci)
                    elif isinstance(player, AIPlayer):
                        move = player.ask_to_move(self.board)
                    if self.board.is_legal(move):
                        break
                    else:
                        self.print_board()
                except Exception as e:
                    logger.exception(e)
                    continue
            if exit or not self.board.is_legal(move):
                break
            self.on_player_moved(player, move)
            self.print_board()
