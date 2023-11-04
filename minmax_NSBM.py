import chess

PV = {
    'pawn': 100,
    'knight': 320,
    'bishop': 330,
    'rook': 500,
    'queen': 950
}

DRAW_VALUE = 0

def evaluation(board, turn):
    if board.is_insufficient_material():
        return DRAW_VALUE

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

    value = (
        PV['pawn'] * (wp - bp) + PV['knight'] * (wn - bn) + PV['bishop'] * (wb - bb) + PV['rook'] * (wr - br) + PV['queen'] * (wq - bq) #-
        #PV['pawn'] * (bp - wp) + PV['knight'] * (bn - wn) + PV['bishop'] * (bb - wb) + PV['rook'] * (br - wr) + PV['queen'] * (bq - wq)
        )
    '''
    if value != 0:
        print(turn)
    '''
    return value

def minmax(board, depth, maximizing_player):
    # print("Starting Minmax")
    if depth == 0 or board.is_game_over():
        return evaluation(board, maximizing_player)

    if maximizing_player:
        best = -10000

        for move in list(board.legal_moves):
            board_copy = board.copy()
            board_copy.push(move)
            val = minmax(board_copy, depth - 1, False)  # Switch to minimizing player
            best = max(best, val)

    else:  # Minimizing player
        best = 10000

        for move in list(board.legal_moves):
            board_copy = board.copy()
            board_copy.push(move)
            val = minmax(board_copy, depth - 1, True)  # Switch to maximizing player
            best = min(best, val)

    return best
