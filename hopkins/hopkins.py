import chess


PIECE_VALUES = {chess.PAWN: 10, chess.KNIGHT: 28, chess.BISHOP: 30, chess.ROOK: 50, chess.QUEEN: 90, chess.KING: 900}
PIECE_SQUARE_TABLES = {
    chess.PAWN: [
         0,  0,  0,  0,  0,  0,  0,  0,
        50, 50, 50, 50, 50, 50, 50, 50,
        10, 10, 20, 30, 30, 20, 10, 10,
         5,  5, 10, 25, 25, 10,  5,  5,
         0,  0,  0, 20, 20,  0,  0,  0,
         5, -5,-10,  0,  0,-10, -5,  5,
         5, 10, 10,-20,-20, 10, 10,  5,
         0,  0,  0,  0,  0,  0,  0,  0
    ],
    chess.KNIGHT : [
        -50,-40,-30,-30,-30,-30,-40,-50,
        -40,-20,  0,  0,  0,  0,-20,-40,
        -30,  0, 10, 15, 15, 10,  0,-30,
        -30,  5, 15, 20, 20, 15,  5,-30,
        -30,  0, 15, 20, 20, 15,  0,-30,
        -30,  5, 10, 15, 15, 10,  5,-30,
        -40,-20,  0,  5,  5,  0,-20,-40,
        -50,-40,-30,-30,-30,-30,-40,-50,
    ],
    chess.BISHOP: [
        -20,-10,-10,-10,-10,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5, 10, 10,  5,  0,-10,
        -10,  5,  5, 10, 10,  5,  5,-10,
        -10,  0, 10, 10, 10, 10,  0,-10,
        -10, 10, 10, 10, 10, 10, 10,-10,
        -10,  5,  0,  0,  0,  0,  5,-10,
        -20,-10,-10,-10,-10,-10,-10,-20,
    ],
    chess.ROOK: [
          0,  0,  0,  0,  0,  0,  0,  0,
          5, 10, 10, 10, 10, 10, 10,  5,
         -5,  0,  0,  0,  0,  0,  0, -5,
         -5,  0,  0,  0,  0,  0,  0, -5,
         -5,  0,  0,  0,  0,  0,  0, -5,
         -5,  0,  0,  0,  0,  0,  0, -5,
         -5,  0,  0,  0,  0,  0,  0, -5,
          0,  0,  0,  5,  5,  0,  0,  0
    ],
    chess.QUEEN: [
        -20,-10,-10, -5, -5,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5,  5,  5,  5,  0,-10,
         -5,  0,  5,  5,  5,  5,  0, -5,
          0,  0,  5,  5,  5,  5,  0, -5,
        -10,  5,  5,  5,  5,  5,  0,-10,
        -10,  0,  5,  0,  0,  0,  0,-10,
        -20,-10,-10, -5, -5,-10,-10,-20
    ],
    chess.KING: [
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -20,-30,-30,-40,-40,-30,-30,-20,
        -10,-20,-20,-20,-20,-20,-20,-10,
         20, 20,  0,  0,  0,  0, 20, 20,
         20, 30, 10,  0,  0, 10, 30, 20
    ]
}


class Hopkins:
    def material_eval(self, board: chess.Board) -> float:
        """
        A part of evaluating the position, this calculates the material evaluation of the position
        Keyword arguments:
            board -- A chess.Board object representing the state of a chess game
        """
        # Count material
        white_pawns = len(board.pieces(chess.PAWN, chess.WHITE))
        white_knights = len(board.pieces(chess.KNIGHT, chess.WHITE))
        white_bishops = len(board.pieces(chess.BISHOP, chess.WHITE))
        white_rooks = len(board.pieces(chess.ROOK, chess.WHITE))
        white_queens = len(board.pieces(chess.QUEEN, chess.WHITE))

        black_pawns = len(board.pieces(chess.PAWN, chess.WHITE))
        black_knights = len(board.pieces(chess.KNIGHT, chess.WHITE))
        black_bishops = len(board.pieces(chess.BISHOP, chess.WHITE))
        black_rooks = len(board.pieces(chess.ROOK, chess.WHITE))
        black_queens = len(board.pieces(chess.QUEEN, chess.WHITE))

        material_eval = PIECE_VALUES[chess.PAWN] * (white_pawns - black_pawns) + PIECE_VALUES[chess.KNIGHT] * (white_knights - black_knights) + PIECE_VALUES[chess.BISHOP] * (white_bishops - black_bishops) + PIECE_VALUES[chess.ROOK] * (white_rooks - black_rooks) + PIECE_VALUES[chess.QUEEN] * (white_queens - black_queens)
        return material_eval

    def evaluate(self, board: chess.Board) -> float:
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
        if board.is_stalemate() or board.is_insufficient_material():
            return 0

        material_eval = self.material_eval(board)

        return material_eval

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
            return

        legal_moves = list(board.legal_moves)

        best = None
        best_eval = 0.0
        for i in legal_moves:
            pass

        return best
