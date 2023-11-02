import random
import chess
import chess.engine
import time
from minmax import minmax, evaluation
from Pos_Eval import engine_evaluation
import os

board = chess.Board()
# print(board)
run = True

while not board.is_game_over():
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
        i = 2
        turn = "white"
        if "moves" in parts:
            moves = parts[parts.index("moves") + 1:]
            board = chess.Board() 
            for move in moves:
                i = i + 1
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
        with open("C:/Users/tstevahn/Phone/Documents/Chess-Engines/fen_test.txt", 'a') as file:
            file.write(board.fen() + os.linesep)
        if legal_moves:
            # best_move = random.choice(legal_moves)
            curr_board = board


            # this is iterating through the list of moves and scoring them. 
            for move in legal_moves:
                # print(move)
                # print(board)
                print(board.fen())
                # print(board)
                move_score = random.randrange(1,10, 1)
                # move_score = engine_evaluation(board.fen(), 0.01)
                # move_score = minmax(board,turn, 2)
                # move_score = evaluation(fen) # this evaluates boards by pieces in play.
                # print(move, move_score)
                if move_score > high_score:
                    high_score = move_score
                    best_move = move
            
            # print("The Best move is",best_move,"with a score of" , move_score)
            

            # print(board)
            # print(i-2, best_move, turn)
            # print(turn)
            # best_move = minmax(board,turn, 2)
            # time.sleep(0.25)
            print("bestmove", best_move)
        else:
            print("bestmove (none)")  # No legal moves left