import chess
import random


PIECE_VALUES = {'P': 10, 'N': 25, 'B': 30, 'R': 50, 'Q': 90, 'K': 900}
PIECE_SQUARE_TABLES = {
    'P': {

    },
    'N' : {

    },
    'B': {

    },
    'R': {

    },
    'Q': {

    },
    'K': {

    }
}


class Hopkins:
    def evaluate(self, board):
        """
        This method evaluates a chess position given a chess.Board object
        Keyword arguments:
            board -- A chess.Board object representing the state of a chess game
        """
        if board.is_checkmate():
            if board.turn:
                return -9999
            else:
                return 9999
        if board.is_stalemate():
            return 0
        if board.is_insufficient_material():
            return 0

        return 0

    def get_move(self, pos: str):
        """
        This method takes in a chess position in FEN format and return a move
        Keyword arguments:
            pos -- An FEN string that represents the current position
        """
        try:
            board = chess.Board(pos)
        except ValueError:
            print('Invalid FEN!')

        legal_moves = list(board.legal_moves)

        # To start, just return a random move
        return random.choice(legal_moves)
