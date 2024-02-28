
class PlayIntention():
    def __init__(self, symbol, column):
        self.symbol = symbol
        self.column = column
    
    def get_final_result(self):
        row = 2
        return Play(self.symbol, self.column, row)