

PV = {
    'pawn': 100,
    'knight': 320,
    'bishop': 330,
    'rook': 500,
    'queen': 950
}

DRAW_VALUE = 0


def evaluation(fen):
    fen



def minmax(board, turn, depth):
    list_of_moves = list(board.legal_moves)
    # print(list_of_moves)
    if board.game_over() or depth==0:
        return evaluation(board, turn)
    
    if turn == "white":
        best = -100000

        for move in list_of_moves:
            board = board.push_uci(move)
            val = minmax(board,depth-1)
            print("white", val)

            turn = "black"

            if val > best:
                best = val
    
    print(board)
    print(turn)
    print(depth)

    if turn == "black":
        best = 10000
        print("turn")

        print(list_of_moves)

        for move in list_of_moves:
            print(move)
            board = board.push_uci(move)
            val = minmax(board,depth-1)
            print("Black", val)

            turn = "white"

            if val < best:
                best = val
    print(best)
    return best 
