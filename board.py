Pieces = (["None", 0],
          ["WhitePawn", 1],
          ["WhiteKnight", 2],
          ["WhiteBishop", 3],
          ["WhiteRook", 4],
          ["WhiteQueen", 5],
          ["WhiteKing", 6],
          ["BlackPawn", 7],
          ["BlackKnight", 8],
          ["BlackBishop", 9],
          ["BlackRook", 10],
          ["BlackQueen", 11],
          ["BlackKing", 12]
          )

class Move:
    def __init__(self, from_index, to_index, promotion):
        # Constructor for the Move class
        # Initializes the fields FromIndex, ToIndex, and Promotion.
        self.FromIndex = from_index  # The index of the starting position of the move
        self.ToIndex = to_index  # The index of the target position of the move
        self.Promotion = promotion  # The piece type for promotion, or None if no promotion

# Board
    #    A  B  C  D  E  F  G  H        BLACK
    # 8  56 57 58 59 60 61 62 63  8
    # 7  48 49 50 51 52 53 54 55  7
    # 6  40 41 42 43 44 45 46 47  6
    # 5  32 33 34 35 36 37 38 39  5
    # 4  24 25 26 27 28 29 30 31  4
    # 3  16 17 18 19 20 21 22 23  3
    # 2  08 09 10 11 12 13 14 15  2
    # 1  00 01 02 03 04 05 06 07  1
    #    A  B  C  D  E  F  G  H        WHITE


class Board:
    def __init__(self):
        # Initialize the state as a list of Piece objects for the 64 squares on the chessboard.
        self.state = [Piece() for _ in range(64)]

    def __getitem__(self, position):
        # The __getitem__ method allows you to access elements of the board using square brackets.
        rank, file = position  # Extract the rank and file indices from the given position.
        return self.state[rank * 8 + file]  # Retrieve the piece at the specified rank and file.

    def __setitem__(self, position, value):
        # The __setitem__ method allows you to set elements of the board using square brackets.
        rank, file = position  # Extract the rank and file indices from the given position.
        self.state[rank * 8 + file] = value  # Set the value (piece) at the specified rank and file.

    def play(self, move):
        moving_piece = self.state[move.FromIndex]  # Get the piece to be moved.
        if move.Promotion is not None:
            moving_piece = move.Promotion  # If there is a promotion, set the moving piece to the promoted piece.

        # Move the correct piece to the target square.
        self.state[move.ToIndex] = moving_piece

        # Clear the square it was previously located on by setting it to None.
        self.state[move.FromIndex] = None

class Piece:
    def __init__(self):
        pass