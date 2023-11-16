import random
import chess
import chess.engine
import time
from minmax import minmax, evaluation
from Pos_Eval import engine_evaluation
import os


depth = 3

# print("starting")

board = chess.Board()
# print(board)
run = True

def select_best_move(board, depth, alpha, beta, maximizing_player):
    # print("list moves")
    legal_moves = list(board.legal_moves)
    best_move = None
    if maximizing_player:
        best_score = -float(10000) 
    else:
        best_score = float(10000)
    # print("Set Score")

    for move in legal_moves:
        board_copy = board.copy()
        board_copy.push(move)
        # print(move)
        move_score = minmax(board_copy, depth - 1, alpha, beta, not maximizing_player)
        print("info score cp", move_score, "for move", move) #Stockfish prints  info depth 2 seldepth 2 multipv 1 score cp 910 nodes 116 nps 116000 hashfull 0 tbhits 0 time 1 pv d7c6
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

    if message.startswith("setoption"):
        # Set the options here.

        if message.startswith("setoption name depth"):
            print(message)
            depth = message[-2:]
    #with open('C:/Users/tstevahn/To_Laptop/Chess-Engines/log.txt', 'a') as file:
    # with open('C:/Users/Snick/Documents/To_Laptop/Chess-Engines/log.txt', 'a') as file:
    #     file.write(message + os.linesep)
    #     file.close()
    if message == "quit":
        break
    # this is for the uciok message
    if message == "uci":
        print("id Random_moves")
        #with open('C:/Users/tstevahn/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        #with open('C:/Users/Snick/Documents/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        #    file.write("id Random_moves" + os.linesep)
        #    file.close()
        # print("setoptions name depth 3")
        print("uciok")
        #with open('C:/Users/tstevahn/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        #with open('C:/Users/Snick/Documents/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        #    file.write("uciok" + os.linesep)
        #    file.close()    
    # this is for the isready message
    if message == "isready":
        print("readyok")
        #with open('C:/Users/tstevahn/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        #with open('C:/Users/Snick/Documents/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        #    file.write("readyok" + os.linesep)
        #    file.close()    

    # this is for the ucinewgame message
    if message == "ucinewgame":
        #board = chess.Board()
        moves = [] 
        print("readyok")
        # with open('C:/Users/tstevahn/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        #with open('C:/Users/Snick/Documents/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        #    file.write("readyok" + os.linesep)
        #    file.close()    
    
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
        # print(turn)
        
    # this is for the go message
    if message.startswith("go"):
        print("go")
        # with open("C:/Users/tstevahn/To_Laptop/Chess-Engines/fen_test.txt", 'a') as file: # Desktop 
        # with open("C:/Users/Snick/Documents/To_Laptop/Chess-Engines/fen_test.txt", 'a') as file: # Laptop
        #     file.write(board.fen() + os.linesep)
        #     file.close
        
        if turn == "white":
            best_move = select_best_move(board, depth, -10000, 10000, True)
        else:
            best_move = select_best_move(board, depth, -10000, 10000, False)

        print("bestmove", best_move)
        # time.sleep(0.05)
        legal_moves = list(board.legal_moves)
        if not board.legal_moves:
            print("bestmove (none)")  # No legal moves left