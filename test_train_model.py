import csv
import chess
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Initialize empty lists to store FEN positions and scores
fen_positions = []
scores = []

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

# Convert FEN positions to numerical features (simplified representation)
def convert_fen_to_features(fen_positions):
    # You should implement a proper conversion from FEN to features
    # For simplicity, we'll use a random feature vector of length 10 as a placeholder
    features = [np.random.rand(10) for _ in fen_positions]
    return np.array(features)

# Convert scores to a format suitable for training
train_target_scores = np.array(train_scores)
val_target_scores = np.array(val_scores)

# Create a neural network model
def create_model(input_shape):
    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=input_shape),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(1)  # Output layer for the predicted score
    ])
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])  # Include Mean Absolute Error (MAE) metric
    return model

# Convert FEN positions to numerical features
train_features = convert_fen_to_features(train_fen_positions)
val_features = convert_fen_to_features(val_fen_positions)

# Create a model and compile it
input_shape = train_features[0].shape
model = create_model(input_shape)

# Train the model on the training dataset and validate on the validation dataset
epochs = 10
batch_size = 32

history = model.fit(
    train_features,
    train_target_scores,
    epochs=epochs,
    batch_size=batch_size,
    validation_data=(val_features, val_target_scores)
)

# Save the trained model for later use
model.save("chess_score_prediction_model")


print("Training completed.")