import sys
import chess
import chess.engine
import random

def uci_loop():
    while True:
        command = input()
        if command == "uci":
            print("uciok")
        if command == "quit":
            break
        elif command == "isready":
            print("readyok")
        elif command.startswith("position"):
            # Handle setting the board position
            handle_position(command)
        elif command.startswith("go"):
            # Handle starting the engine's search
            handle_go(command)
        '''
        else:
            print("Unknown command")
            '''

def handle_position(command):
    parts = command.split()
    if "startpos" in parts:
        board = chess.Board()
    else:
        # Handle setting a custom position (e.g., "position fen <FEN>")
        fen_index = parts.index("fen") + 1
        fen = " ".join(parts[fen_index:])
        board = chess.Board(fen)

    moves_index = parts.index("moves") if "moves" in parts else -1
    if moves_index != -1:
        # Handle applying a list of moves to the current position
        moves = parts[moves_index + 1:]
        for move in moves:
            board.push_uci(move)

def handle_go(command):
    # Basic implementation, just return a random move
    board = chess.Board()
    if "ponder" in command:
        print("bestmove {} ponder {}".format(get_random_move(board), get_random_move(board)))
    else:
        print("bestmove {}".format(get_random_move(board)))

def get_random_move(board):
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves).uci()

if __name__ == "__main__":
    #print("id name Chatgpt_Engine_1")
    #print("id author Chatgpt")
    uci_loop()