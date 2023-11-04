import chess

PV = {
    'pawn': 100,
    'knight': 320,
    'bishop': 330,
    'rook': 500,
    'queen': 950
}

DRAW_VALUE = 0

def evaluation(board):
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
        PV['pawn'] * (wp - bp) +
        PV['knight'] * (wn - bn) +
        PV['bishop'] * (wb - bb) +
        PV['rook'] * (wr - br) +
        PV['queen'] * (wq - bq) -
        PV['pawn'] * (bp - wp) +
        PV['knight'] * (bn - wn) +
        PV['bishop'] * (bb - wb) +
        PV['rook'] * (br - wr) +
        PV['queen'] * (bq - wq) )
    print(value)
    if board.turn == chess.WHITE:
        return value
    return -value

def minmax(board, depth, turn):
    #print("Started Minmax")
    # print(turn)
    if depth == 0:
        return evaluation(board)

    if turn == "white":
        # print("white's turn")
        best = -100000

        for move in list(board.legal_moves):
            # print("works")
            board_copy = board.copy()
            # print("copy board")
            board_copy.push(move)
            # print("pushed move")
            val = minmax(board_copy, depth - 1, "black")
            # print("got value")
            if val > best:
                # best_move = move
                best = val
            # print("White got best value")

    if turn =="black":  # turn == "black"
        # print("Black's turn")
        best = 10000

        for move in list(board.legal_moves):
            # print("works")
            board_copy = board.copy()
            # print("copy board")
            board_copy.push(move)
            # print("pushed move")
            val = minmax(board_copy, depth - 1, "white")
            # print("got value")
            if val < best:
                # best_move = move
                best = val
            # print("Black got best value")

    return best

'''
fen = 'rnbqkbnr/ppp1pppp/8/3P4/8/8/PPPP1PPP/RNBQKBNR b KQkq - 0 2'
board = chess.Board(fen)

value = minmax(board, 3, "white")
print(f'board evaluation: {value}')
'''