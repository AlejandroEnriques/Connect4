

class Screen():

    ROWS = 6
    COLUMN = 7

    def __init__(self):

        self.plays = []
    
    def add_play(self, play):
        self.plays.append(play)

    def generate_table(self):
        for row in range(self.ROWS):
            row_text = ""
            for column in range(self.COLUMN):
                symbol_added = False
                for play in self.plays:
                    if play.row == row and play.column == column:
                        row_text += f"|{play.symbol}|"
                        symbol_added = True
                        break
                    
                if not symbol_added:
                    row_text += f"| |"

            print(row_text)

if __name__ == "__main__":
    screen = Screen()
    screen.generate_table()
