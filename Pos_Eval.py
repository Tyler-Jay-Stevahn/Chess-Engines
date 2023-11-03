import chess
import chess.engine
import time
import re
import csv

def engine_evaluation(board, depth=1):
    # engine = chess.engine.SimpleEngine.popen_uci("C:/Users/Snick/Documents/To_Laptop/Chess UCI/berserk_12_x64/berserk-12-x64-avx2.exe")
    engine = chess.engine.SimpleEngine.popen_uci("C:/Users/tstevahn/To_Laptop/Chess UCI/berserk_12_x64/berserk-12-x64-avx2.exe")
    result = engine.analyse(board, chess.engine.Limit(depth))
    engine.close()
    score = result ['score']
    score = str(score)
    match = re.search(r'\(([-+]?\d+)\)', score)
    if match:
        value = match.group(1)
        score = value
    # print(score)
    return score

'''
board = chess.Board("1r5b/p1pqp1r1/3pbk2/8/4B3/1PP1P1P1/n1QP2KP/RNB1R3 w - - 0 37")
result = engine_evaluation(board)
print(result)
'''

'''
# Create or open a CSV file to store the results
# file_path = "C:/Users/Snick/Documents/To_Laptop/Chess-Engines/fen_scores.csv"  # Change this to your desired file path
file_path = "C:/Users/tstevahn/To_Laptop/Chess-Engines/fen_scores.csv"  # Change this to your desired file path
i = 0
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write a header row
    writer.writerow(['FEN', 'Score'])

    # Iterate over FEN positions and evaluate
    # with open("C:/Users/Snick/Documents/To_Laptop/Chess-Engines/fen_clean.txt", 'r') as fen_file:
    with open("C:/Users/tstevahn/To_Laptop/Chess-Engines/fen_clean.txt", 'r') as fen_file:
        for line in fen_file:
            fen = line.strip()
            i = i + 1
            if ((i/46194) % 1) == 0:
                print("Finished percentage", i/46194)
            if fen:
                try:
                    board = chess.Board(fen)
                    result = engine_evaluation(board)
                    writer.writerow([fen, result])  # Write FEN and its score to the CSV file
                    # print(fen, result)
                except ValueError as e:
                    print(f"Error parsing FEN: {fen} - {e}")
            else:
                pass  # Skip empty FEN strings

print(f"Data written to {file_path}.")
'''