
from screen_V2 import Screen
from play import Play

class Game():

    def __init__(self):
        pass

    def start():
        print('''Lets play Connect 4!
        You need 2 players, the first one that connect 4 will win
        Player 1 = X
        Player 2 = O''')
        print('enemy\n please')
        input('Press Enter to play')
    
if __name__ == "__main__":
    screen = Screen()

    play_intention = PlayIntention("x", 2)
    play = play_intention.get_final_result()

    screen.add_play(play)
    # screen.add_play(Play("x", 2, 3))
    # screen.add_play(Play("0", 1, 3))
    # screen.add_play(Play("x", 4, 0))
    # screen.add_play(Play("0", 4, 4))

    screen.generate_table()