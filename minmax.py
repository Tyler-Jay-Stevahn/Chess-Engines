
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
pawn_table_white = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0
]


knight_table_white = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
]

bishop_table_white = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
]

rook_table_white = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, 10, 10, 10, 10, 5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, 5, 5, 0, 0, 0
]

queen_table_white = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
]

king_table_white = [
    20, 30, -10, 0, 0, -10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
]

# Piece Square Tables for Black (Reverse for Black)
pawn_table_black = pawn_table_white[::-1]
knight_table_black = knight_table_white[::-1]
bishop_table_black = bishop_table_white[::-1]
rook_table_black = rook_table_white[::-1]
queen_table_black = queen_table_white[::-1]
king_table_black = king_table_white[::-1]

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
            if piece.color == chess.WHITE:
                value += get_pst_value(piece, square, True)
            else:
                value -= get_pst_value(piece, square, False)
            #print(value)
    
    # Add term for center control
    center_control = sum(1 for square, piece in enumerate(board.piece_map()) if piece is not None and square in CENTER_SQUARES)
    center_control_score = 100 * center_control
    value += center_control_score
    #print("Center Control Score:", center_control_score, "Total Value:", value)

    
    # Encourage castling
    castling_bonus = 1000  # Adjust the bonus according to your preference

    # Award points for maintaining castling rights
    castling_rights_bonus = 1000  # Adjust the bonus according to your preference

    if board.has_kingside_castling_rights(chess.WHITE):
        value += castling_rights_bonus
        # print("White Kingside Castling Rights Bonus Added. Total Value:", value)

    if board.has_queenside_castling_rights(chess.WHITE):
        value += castling_rights_bonus
        # print("White Queenside Castling Rights Bonus Added. Total Value:", value)

    if board.has_kingside_castling_rights(chess.BLACK):
        value -= castling_rights_bonus
        # print("Black Kingside Castling Rights Bonus Deducted. Total Value:", value)

    if board.has_queenside_castling_rights(chess.BLACK):
        value -= castling_rights_bonus
        # print("Black Queenside Castling Rights Bonus Deducted. Total Value:", value)

    # Check if kings are castled
    if board.has_kingside_castling_rights(chess.WHITE) and board.has_kingside_castling_rights(chess.BLACK):
        value += castling_bonus
        # print("Both Kings Castled Bonus Added. Total Value:", value)

    if board.has_queenside_castling_rights(chess.WHITE) and board.has_queenside_castling_rights(chess.BLACK):
        value += castling_bonus
        # print("Both Queens Castled Bonus Added. Total Value:", value)

    # Penalize king moves
    # if board.kings[chess.WHITE] != 4 or board.kings[chess.BLACK] != 60:
    #     value -= castling_bonus
    if board.is_stalemate():
        if chess.WHITE:
            value -= 100000
        elif chess.BLACK:
            value += 100000
    
    value = value/1000

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

def get_pst_value(piece, square, is_white):
    # Use the appropriate PST based on the color of the piece
    if piece.piece_type == chess.PAWN:
        return pawn_table_white[square] if is_white else pawn_table_black[square]
    elif piece.piece_type == chess.KNIGHT:
        return knight_table_white[square] if is_white else knight_table_black[square]
    elif piece.piece_type == chess.BISHOP:
        return bishop_table_white[square] if is_white else bishop_table_black[square]
    elif piece.piece_type == chess.ROOK:
        return rook_table_white[square] if is_white else rook_table_black[square]
    elif piece.piece_type == chess.QUEEN:
        return queen_table_white[square] if is_white else queen_table_black[square]
    elif piece.piece_type == chess.KING:
        return king_table_white[square] if is_white else king_table_black[square]

    return 0