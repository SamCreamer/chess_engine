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
    # chess.KING: [
    #     -30,-40,-40,-50,-50,-40,-40,-30,
    #     -30,-40,-40,-50,-50,-40,-40,-30,
    #     -30,-40,-40,-50,-50,-40,-40,-30,
    #     -30,-40,-40,-50,-50,-40,-40,-30,
    #     -20,-30,-30,-40,-40,-30,-30,-20,
    #     -10,-20,-20,-20,-20,-20,-20,-10,
    #      20, 20,  0,  0,  0,  0, 20, 20,
    #      20, 30, 10,  0,  0, 10, 30, 20
    # ]
    chess.KING: [
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -20,-30,-30,-40,-40,-30,-30,-20,
        -10,-20,-20,-20,-20,-20,-20,-10,
         0,   0,  0,  0,  0,  0,  0,  0,
         0,   0,  0,  0,  0,  0,  0,  0
    ]
}


class Hopkins:
    @staticmethod
    def whites_turn(board):
        return board.turn

    @staticmethod
    def position_piece_type_material_eval(board: chess.Board, piece: int) -> float:
        """
        Get's the material count eval for a specific piece type
        Keyword arguments:
            board -- A chess.Board object representing the state of a chess game
            piece -- An integer representing a type of piece
        """
        return PIECE_VALUES[piece] * (len(board.pieces(piece, chess.WHITE)) - len(board.pieces(piece, chess.BLACK)))

    def material_eval(self, board: chess.Board) -> float:
        """
        A part of evaluating the position, this calculates the material evaluation of the position
        Keyword arguments:
            board -- A chess.Board object representing the state of a chess game
        """
        # We don't care about kings for this eval
        relevant_piece_types = [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN]

        # Count material
        material_eval_val = 0.0
        for piece_type in relevant_piece_types:
            material_eval_val += self.position_piece_type_eval(board, piece_type)

        return material_eval_val

    @staticmethod
    def position_piece_type_square_eval(board: chess.Board, piece: int) -> float:
        """
        Get's the position eval from the squares of a piece type. Refers to the piece square tables.
        Keyword arguments:
            board -- A chess.Board object representing the state of a chess game
            piece -- An integer representing a type of piece
        """
        pass

    def piece_square_eval(self, board: chess.Board) -> float:
        """
        Get's the portion of the eval that takes into account the position of the pieces
        Keyword arguments:
            board -- A chess.Board object representing the state of a chess game
        """
        relevant_piece_types = [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN, chess.KING]

        piece_square_eval_val = 0.0

        for piece_type in relevant_piece_types:
            piece_square_eval_val += self.position_piece_type_square_eval(board, piece_type)

        return piece_square_eval_val


    def evaluate(self, board: chess.Board) -> float:
        """
        This method evaluates a chess position given a chess.Board object
        Keyword arguments:
            board -- A chess.Board object representing the state of a chess game
        """
        if board.is_checkmate():
            if self.whites_turn(board):  # black is checkmated
                return -1000000
            else:
                return 1000000
        if board.is_stalemate() or board.is_insufficient_material():
            return 0

        material_eval = self.material_eval(board)
        piece_square_eval = self.piece_square_eval(board)

        return (material_eval + piece_square_eval) / 10.0

    def get_move(self, pos: str, depth: int):
        """
        This method takes in a chess position in FEN format and return a move
        Keyword arguments:
            pos -- An FEN string that represents the current position
            depth -- The depth of calculation for this move
        """
        board = chess.Board(pos)

        legal_moves = list(board.legal_moves)

        best = None
        best_eval = 0.0
        for i in legal_moves:
            pass

        return best
