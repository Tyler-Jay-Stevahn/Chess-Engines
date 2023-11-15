
import chess

# Material = Done
# King Safety
# Activity of Pieces
# Pawn Structure
# Space Advantage

PV = {
    'pawn': 100,
    'knight': 320,
    'bishop': 330,
    'rook': 500,
    'queen': 950,
    'king': 99999
}

DRAW_VALUE = 0

# Piece Square Tables
pawn_table = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0
]

knight_table = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
]

bishop_table = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
]

rook_table = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, 10, 10, 10, 10, 5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, 5, 5, 0, 0, 0
]

queen_table = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
]

king_table = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
]

CENTER_SQUARES = {chess.E4, chess.D4, chess.E5, chess.D5}


def evaluation(board, turn):
    # if board.is_insufficient_material():
    #     return DRAW_VALUE

    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))

    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))

    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))

    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))

    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))

    wk = len(board.pieces(chess.KING, chess.WHITE))
    bk = len(board.pieces(chess.KING, chess.BLACK))

    value = (
        PV['pawn'] * (wp - bp) + PV['knight'] * (wn - bn) + PV['bishop'] * (wb - bb) + PV['rook'] * (wr - br) + PV['queen'] * (wq - bq)  + PV['king'] * (wk - bk)
    )
    #print("value", value)
    #print(board.piece_map())
    # Add Piece Square Tables
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            #print("square", square)
            #print("Piece", piece)
            if piece.color == chess.WHITE:
                value += get_pst_value(piece, square)
            else:
                value -= get_pst_value(piece, square)
            #print(value)
    # Add term for center control
    center_control = sum(1 for square, piece in enumerate(board.piece_map()) if piece is not None and square in CENTER_SQUARES)
    
    # You can adjust the weight according to the importance you want to give to center control
    center_control_score = 10 * center_control
    value += center_control_score

    # Encourage castling
    castling_bonus = 50  # Adjust the bonus according to your preference

    # Award points for maintaining castling rights
    castling_rights_bonus = 10  # Adjust the bonus according to your preference

    #if board.has_kingside_castling_rights(chess.WHITE):
    #    value += castling_rights_bonus

    #if board.has_queenside_castling_rights(chess.WHITE):
    #    value += castling_rights_bonus

    #if board.has_kingside_castling_rights(chess.BLACK):
    #    value -= castling_rights_bonus

    #if board.has_queenside_castling_rights(chess.BLACK):
    #    value -= castling_rights_bonus

    # Check if kings are castled
    
    #if board.has_kingside_castling_rights(chess.WHITE) and board.has_kingside_castling_rights(chess.BLACK):
    #    value += castling_bonus

    #if board.has_queenside_castling_rights(chess.WHITE) and board.has_queenside_castling_rights(chess.BLACK):
    #    value += castling_bonus

    return value

def minmax(board, depth, alpha, beta, maximizing_player):
    # print("Starting Minmax")
    if depth == 0 or board.is_game_over():
        return evaluation(board, maximizing_player)

    if maximizing_player:
        best = -10000

        for move in list(board.legal_moves):
            board_copy = board.copy()
            board_copy.push(move)
            val = minmax(board_copy, depth - 1, alpha, beta, False)  # Switch to minimizing player
            alpha = max(alpha, best)
            alphacurr = alpha
            if alphacurr < alpha:
                print("alpha", alphacurr, "for move ", move)
            if beta <= alpha:
                break
            best = max(best, val)

    else:  # Minimizing player
        best = 10000

        for move in list(board.legal_moves):
            board_copy = board.copy()
            board_copy.push(move)
            val = minmax(board_copy, depth - 1, alpha, beta, True)  # Switch to maximizing player
            beta = min(beta, best)
            betacurr = beta
            if betacurr > beta:
                print("beta", betacurr, "for move ", move)
            if beta <= alpha:
                break
            best = min(best, val)

    return best

def get_pst_value(piece, square):
    if piece.piece_type == chess.PAWN:
        return pawn_table[square]
    elif piece.piece_type == chess.KNIGHT:
        return knight_table[square]
    elif piece.piece_type == chess.BISHOP:
        return bishop_table[square]
    elif piece.piece_type == chess.ROOK:
        return rook_table[square]
    elif piece.piece_type == chess.QUEEN:
        return queen_table[square]
    elif piece.piece_type == chess.KING:
        return king_table[square]

    return 0