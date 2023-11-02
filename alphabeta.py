

def alphabeta(board, alpha, beta, depth):
    if board.game_over() or depth==0:
        return evaluate(board)
    
    if board.turn == "white":
        best = -100000

        for move in board.moves():
            board = board.make(move)
            val = alphabeta(board,depth-1)

            if val > best:
                best = val
    else:
        best = 10000

        for move in board.moves():
            board = board.make(move)
            val = alphabeta(board,depth-1)

            if val < best:
                best = val
    return best 