import chess


class Hopkins:
    def __init__(self):
        self.board = chess.Board()

    def legal_moves(self):
        return self.board.legal_moves
