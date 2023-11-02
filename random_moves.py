import random
import chess
import chess.engine
import time

board = chess.Board()
# print(board)
run = True

while run:
    message = input()
    # this is for the uciok message
    if message == "uci":
        print("id Random_moves")
        print("uciok")

    # this is for the isready message
    if message == "isready":
        print("readyok")

    # this is for the ucinewgame message
    if message == "ucinewgame":
        #board = chess.Board()
        moves = [] 
        print("readyok")
    
     # this is for the position message
    if message.startswith("position startpos"):
        parts = message.split()
        if "moves" in parts:
            moves = parts[parts.index("moves") + 1:]
            board = chess.Board() 
            for move in moves:
                board.push_uci(move)
        
    # this is for the go message
    if message.startswith("go"):
        legal_moves = list(board.legal_moves)
        # print(legal_moves)
        if legal_moves:
            best_move = random.choice(legal_moves)
            time.sleep(0.25) # put this here to test GUI's to see if this was the issue. It was not the issue.
            print("bestmove", best_move)
        else:
            print("bestmove (none)")  # No legal moves left