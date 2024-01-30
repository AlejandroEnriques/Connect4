import Player
import random

class Board():
    def __init__(self, turn, is_game_finshed, isVictorious, new_start) -> None:
        self.turn = turn
        self.is_game_finshed = is_game_finshed
        self.isVictorious = isVictorious
        self.new_start = new_start
        self.player_1 = ''
        self.player_2 = ''
        
        
        self._table = [['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ]      
        
    def new_game(self):
        self._table = [['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ] 
        
        self.player_1 = Player.Player('|O|', False)
        self.player_2 = Player.Player('|X|', False)
        
        self.first_turn = random.randrange(1, 2) 
        
        if self.first_turn == 1:
            self.first_turn = 'Player 1'
        else:
            self.first_turn = 'Player 2'
    
            
            

        #Make the logic of the game run in this part... i think, the core game should be in game, the problem is i don't know here
        
        
        
        
    def print_table(self):
        for column in range(len(self._table)):
            
            for row in range(len(self._table[column])):
        
                print(self._table[column][row], end=" ")
            
        
        