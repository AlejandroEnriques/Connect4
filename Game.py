import importlib

import Player
import Logic
import os

def clear_terminal():
    os.system('cls')



importlib.reload(Player)
class Board():
    def __init__(self):
        self.turn = ''
        self.is_game_finshed = ''
        self.victory = False
        self.new_start = False
        self.player_1 = ''
        self.player_2 = ''
        self.row_count = 6
        self.column_count = 7
        
           
    def new_game(self):

        game_finish = False
        self.player_1 = Player.Player('Player 1', '|O|', False)
        self.player_2 = Player.Player('Player 2', '|X|', False)
        turns = 2
        while game_finish == False:
            
            self._table = [['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |'],
                       ['| |', '| |', '| |', '| |','| |','| |','| |']] 
            self.victory = False
            roundturn = 0
            #While victory is False the game will continue
            while self.victory == False:
                
                #For to make a turn system
                for roundturn in range(turns):
        
                    if roundturn % 2 == 1:
                        self.turn = self.player_1
                    else:
                        self.turn = self.player_2
                turns += 1    

                clear_terminal()
                
                self.print_table()    
                print(f'{self.turn.name} Turn')
                            
                while True:
                    try:
                        selected_column = int(input('Column:'))
                        
                        if 1 <= selected_column <= 7:
                            break
                        else:
                            print('Please Enter a Number Between 1 to 8')
                                                        
                    except IndexError:
                        print('Sorry, should be a number')
                    
                    
                token_position = Logic.Rules(self.turn.token, self._table, selected_column, self.row_count, self.column_count)     
                token_position.place_token()   
                
                self.victory = token_position.check_winner()
                print(self.victory)
                if self.victory:
                    self.print_table()
                    print(f"THE WINNER IS {self.turn.name}\n!!!")
                    
                    again = input("Do you want to play again? (Y/N):")
                    
                    if again.upper() != 'Y':
                        print("Thank you for playing!")
                        return game_finish == True

    def print_table(self):
        for row in range(len(self._table)):
            row_text="" 
            for item in self._table[row]:
                row_text += f" {item}"
            print(row_text)
        print("  1   2   3   4   5   6   7 ")
         