import os

'''
with open("C:/Users/Snick/Documents/To_Laptop/Chess-Engines/fen_test.txt", 'a') as file: # Desktop 
# with open("C:/Users/Snick/Documents/To_Laptop/Chess-Engines/fen_test.txt", 'a') as file: # Laptop
            file.write(line)
'''
# Define the file path where FEN positions are saved
#file_path = "C:/Users/Snick/Documents/To_Laptop/Chess-Engines/fen_test.txt"  # Change this to the actual file path
file_path = "C:/Users/tstevahn/To_Laptop/Chess-Engines/fen_test.txt"  # Change this to the actual file path

# Create a set to store unique FEN positions
unique_fen_positions = set()

# Open the file and read FEN positions
with open(file_path, 'r') as file:
    for line in file:
        # Strip any leading/trailing whitespace and add to the set
        fen = line.strip()
        if len(fen) > 1:  # Check if the line is not empty
            unique_fen_positions.add(fen)

# Convert the set of unique FEN positions back to a list
unique_fen_positions_list = list(unique_fen_positions)

# Now, unique_fen_positions_list contains a list of unique FEN positions from the file

print(len(unique_fen_positions_list))

#with open("C:/Users/Snick/Documents/To_Laptop/Chess-Engines/fen_clean.txt", 'w') as file:
with open("C:/Users/tstevahn/To_Laptop/Chess-Engines/fen_clean.txt", 'w') as file:
    for line in unique_fen_positions_list:
        file.writelines(line)
        file.writelines(os.linesep)
