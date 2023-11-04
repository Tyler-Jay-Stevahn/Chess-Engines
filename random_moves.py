import random
import chess
import chess.engine
import time
import os

board = chess.Board()
# print(board)
run = True

while run:
    message = input()
    #with open('C:/Users/tstevahn/To_Laptop/Chess-Engines/log.txt', 'a') as file:
    with open('C:/Users/Snick/Documents/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        file.write(message + os.linesep)
        file.close()
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

    # this is for the isready message
    if message == "quit":
        break
    # this is for the ucinewgame message
    if message == "ucinewgame":
        #board = chess.Board()
        moves = [] 
        print("readyok")
        #with open('C:/Users/tstevahn/To_Laptop/Chess-Engines/log.txt', 'a') as file:
        with open('C:/Users/Snick/Documents/To_Laptop/Chess-Engines/log.txt', 'a') as file:
            file.write("readyok" + os.linesep)
            file.close()    
    
     # this is for the position message
    if message.startswith("position startpos"):
        parts = message.split()
        # with open("C:/Users/tstevahn/To_Laptop/Chess-Engines/fen_test.txt", 'a') as file: # Desktop 
        with open("C:/Users/Snick/Documents/To_Laptop/Chess-Engines/fen_test.txt", 'a') as file: # Laptop
            file.write(board.fen() + os.linesep)
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
            
            new_message = best_move
            new_message = str(new_message)
            time.sleep(0.25) # put this here to test GUI's to see if this was the issue. It was not the issue.
            #with open('C:/Users/tstevahn/To_Laptop/Chess-Engines/log.txt', 'a') as file:
            with open('C:/Users/Snick/Documents/To_Laptop/Chess-Engines/log.txt', 'a') as file:
                file.write("bestmove " + new_message + os.linesep)
                file.close()    
            print("bestmove", best_move)
        else:
            print("bestmove (none)")  # No legal moves left