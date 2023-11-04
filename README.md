# Chess-Engines
Just a list of chess engines I have made and the python behind them

Random_moves.py Literally just makes random moves.
- Note: only works with computer vs computer matches in some GUI's.
    - it has issues with player versus computer matches after moves because it just stops playing and you have to stop/start it to get it to play each move.
        - This is because Banksiagui will occasionally not send a message to the program. Not sure what it is doing.
    - has good stability with CuteChess GUI
    - has bad stability with Banksiagui with Player versus Computer matches.
    - does not have any scoring method for moves
Test.py currently is messing around with a scoring method.
- Note: this is still in the testing phase and it is using the Randm_moves.py as a baseline. 
    - found scoring method from https://chess.stackexchange.com/questions/39004/python-efficient-board-scoring-function-to-use-as-placeholder
    - implemented to show that it can have more choice in the moves it makes as a rough start to an evaluation method.
Not_So_Bright_Marauder.py is a bot that values the pieces only and makes the move with the highest score.
- Note: Tends to play the same pieces and not develop other pieces. 
