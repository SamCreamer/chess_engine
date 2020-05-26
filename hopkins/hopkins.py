import chess
import random


PIECE_VALUES = {'P': 10, 'K': 25, 'B': 30, 'R': 50, 'Q': 90, 'K': 900}


class Hopkins:
    @staticmethod
    def get_move(pos: str):
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
