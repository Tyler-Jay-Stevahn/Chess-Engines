
import chess
import chess.engine
import time
from minmax_NSBM import minmax
import os


# print("starting")

board = chess.Board()
# print(board)
run = True

def select_best_move(board, depth, maximizing_player):
    legal_moves = list(board.legal_moves)
    best_move = None
    if maximizing_player:
        best_score = -float(10000) 
    else:
        best_score = float(10000)

    for move in legal_moves:
        board_copy = board.copy()
        board_copy.push(move)
        move_score = minmax(board_copy, depth - 1, not maximizing_player)
        print("testing", move, move_score, best_score)  
        # White is maximizing_player
        if maximizing_player:
            if move_score > best_score:
                best_score = move_score
                best_move = move
                print("best move found for max", best_move, best_score)  
        # Black is mininimizing_player
        if not maximizing_player:
            if move_score < best_score:
                best_score = move_score
                best_move = move
                print("best move found for not max", best_move, best_score)

    return best_move

while not board.is_game_over():
    message = input()
    #with open('C:/Users/tstevahn/To_Laptop/Chess-Engines/log.txt', 'a') as file:
    with open('C:/Users/Snick/Documents/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        file.write(message + os.linesep)
        file.close()
    if message == "quit":
        break
    # this is for the uciok message
    if message == "uci":
        print("id Random_moves")
        #with open('C:/Users/tstevahn/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        with open('C:/Users/Snick/Documents/To_Laptop/Chess-Engines/log.txt', 'a') as file:
            file.write("id Random_moves" + os.linesep)
            file.close()    
        print("uciok")
        #with open('C:/Users/tstevahn/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        with open('C:/Users/Snick/Documents/To_Laptop/Chess-Engines/log.txt', 'a') as file:
            file.write("uciok" + os.linesep)
            file.close()    
    # this is for the isready message
    if message == "isready":
        print("readyok")
        #with open('C:/Users/tstevahn/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        with open('C:/Users/Snick/Documents/To_Laptop/Chess-Engines/log.txt', 'a') as file:
            file.write("readyok" + os.linesep)
            file.close()    

    # this is for the ucinewgame message
    if message == "ucinewgame":
        #board = chess.Board()
        moves = [] 
        print("readyok")
        # with open('C:/Users/tstevahn/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        with open('C:/Users/Snick/Documents/To_Laptop/Chess-Engines/log.txt', 'a') as file:
            file.write("readyok" + os.linesep)
            file.close()    
    
     # this is for the position message
    if message.startswith("position startpos"):
        parts = message.split()
        i = 2
        turn = "white"
        if "moves" in parts:
            moves = parts[parts.index("moves") + 1:]
            board = chess.Board() 
            for move in moves:
                i = i + 1
                # print(move)
                board.push_uci(move)
            if (i % 2) == 1:
                turn = "black"
            else:
                turn = "white"
        
    # this is for the go message
    if message.startswith("go"):
        legal_moves = list(board.legal_moves)
        # print(legal_moves)
        high_score = -1000000
        move_score = -2000
        # with open("C:/Users/tstevahn/To_Laptop/Chess-Engines/fen_test.txt", 'a') as file: # Desktop 
        with open("C:/Users/Snick/Documents/To_Laptop/Chess-Engines/fen_test.txt", 'a') as file: # Laptop
            file.write(board.fen() + os.linesep)
        if legal_moves:
            if turn == "white":
                best_move = select_best_move(board, 2, True)
            else:
                best_move = select_best_move(board, 2, False)

            print("bestmove", best_move)
            time.sleep(0.05)
        else:
            print("bestmove (none)")  # No legal moves left