import importlib
import Game
import os


importlib.reload(Game)

# Main Menu
def clear_terminal():
    os.system('cls')

clear_terminal()
print('''Lets play Connect 4!
You need 2 players to play!
Player 1 = X
Player 2 = O''')
input('Press Enter to start')


board = Game.Board()    
board.new_game()
