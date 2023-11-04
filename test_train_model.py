import csv
import chess
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Conv2D, Flatten, Dense, Dropout

# Initialize empty lists to store FEN positions and scores
fen_positions = []
scores = []

# Set your desired learning rate here
learning_rate = 0.00001

# Set the Dropout rate here 
drop_rate = 0.2

# Load FEN positions and scores from a CSV file
csv_file = "C:/Users/Snick/Documents/To_Laptop/Chess-Engines/fen_scores.csv"  # Update with the path to your CSV file
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if present
    for row in reader:
        fen_positions.append(row[0])
        scores.append(float(row[1]))  # Assuming scores are stored as floats in the CSV

# Split the dataset into training and validation sets
split_ratio = 0.8  # 80% of the data for training, 20% for validation
split_index = int(len(fen_positions) * split_ratio)

train_fen_positions = fen_positions[:split_index]
train_scores = scores[:split_index]
val_fen_positions = fen_positions[split_index:]
val_scores = scores[split_index:]

# Function to evaluate king safety based on pawn shelter
def evaluate_king_safety(board):
    king_safety_score = 0
    current_color = board.turn
    king_square = board.king(current_color)
    rank, file = chess.square_rank(king_square), chess.square_file(king_square)
    squares_in_front = [chess.square(file, rank - 1), chess.square(file - 1, rank - 1), chess.square(file + 1, rank - 1)]

    for square in squares_in_front:
        if board.piece_at(square) == chess.Piece(current_color, chess.PAWN):
            king_safety_score += 1

    return king_safety_score

# Function to evaluate opponent's piece proximity to the king
def evaluate_opponent_proximity(board):
    opponent_proximity_score = 0
    current_color = board.turn
    king_square = board.king(current_color)

    # Determine the squares attacked by the opponent's queen and rooks
    opponent_attacks = board.attacks(king_square)

    # Check if the opponent's pieces are attacking the king
    for square in board.pieces(chess.QUEEN, not current_color):
        if king_square in board.attacks(square):
            opponent_proximity_score += 1

    for square in board.pieces(chess.ROOK, not current_color):
        if king_square in board.attacks(square):
            opponent_proximity_score += 1

    return opponent_proximity_score
i = 0

# Define a function to convert FEN positions to numerical features
def convert_fen_to_features(fen_positions):
    features = []
    for fen in fen_positions:
        board = chess.Board(fen)

        # Initialize an empty 8x8x12 array to represent the chessboard
        board_features = np.zeros((8, 8, 12), dtype=np.float32)

        # One-hot encode the piece positions with piece type and color information
        for rank in range(8):
            for file in range(8):
                piece = board.piece_at(chess.square(file, rank))
                if piece is not None:
                    piece_index = piece.piece_type - 1  # Piece type index (0 for pawn, 1 for knight, etc.)
                    color_index = int(piece.color)  # 0 for white, 1 for black
                    board_features[rank, file, color_index * 6 + piece_index] = 1.0

        features.append(board_features)

    return np.array(features)

# Convert scores to a format suitable for training
train_target_scores = np.array(train_scores)
val_target_scores = np.array(val_scores)

# Define a more complex CNN model
def create_complex_cnn_model(input_shape, learning_rate=learning_rate, dropout_rate=drop_rate):
    model = keras.Sequential([
        Conv2D(64, (3, 3), activation='relu', input_shape=input_shape),
        Conv2D(128, (3, 3), activation='relu'),
        Conv2D(256, (3, 3), activation='relu'),
        Conv2D(256, (3, 3), activation='relu', padding='same'),
        Conv2D(256, (3, 3), activation='relu', padding='same'),
        Conv2D(256, (3, 3), activation='relu', padding='same'),
        Flatten(),
        Dense(256, activation='relu'),
        Dropout(dropout_rate),
        Dense(64, activation='relu'),
        Dense(1)  # Output layer for the predicted score
    ])
    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['mae'])

    return model

# Convert FEN positions to numerical features
train_features = convert_fen_to_features(train_fen_positions)
val_features = convert_fen_to_features(val_fen_positions)

# Create the dropout CNN model
input_shape = train_features[0].shape
model = create_complex_cnn_model(input_shape, learning_rate=0.001, dropout_rate=0.2)

# Train the model
epochs = 10
batch_size = 64

history = model.fit(
    train_features,
    train_target_scores,
    epochs=epochs,
    batch_size=batch_size,
    validation_data=(val_features, val_target_scores)
)

# Save the trained model
model.save("chess_score_prediction_cnn_model_with_dropout")

print("Training completed.")