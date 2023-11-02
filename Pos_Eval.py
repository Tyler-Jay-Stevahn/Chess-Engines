import chess
import chess.engine

def engine_evaluation(board, time_limit=0.1):
    engine = chess.engine.SimpleEngine.popen_uci("C:/Users/tstevahn/To_Laptop/Chess UCI/berserk_12_x64/berserk-12-x64-avx2.exe")
    result = engine.analyse(board, chess.engine.Limit(time=time_limit))
    engine.close()
    score = result ['score']
    score = str(score)
    print(score)
    score = score[12:15]
    return score

'''
board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
result = engine_evaluation(board)
print(result)
'''
