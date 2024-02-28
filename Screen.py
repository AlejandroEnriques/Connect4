import importlib
import Game
importlib.reload(Game)

# Main Menu

print('''Lets play Connect 4!
You need 2 players to play!
Player 1 = X
Player 2 = O''')
input('Press Enter to start')


board = Game.Board()    
board.new_game()
