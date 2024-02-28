class Rules():
    def __init__(self, token, table, selected_column, row_count, column_count):
        self.token = token
        self.table = table
        self.selected_column = selected_column - 1
        self.row_count = row_count
        self.column_count = column_count
    
    def place_token(self):
            
        for row in reversed(range(6)):
            if  self.table[row][self.selected_column] == '| |':
                self.table[row][self.selected_column] = self.token 
                break
        
    def check_winner(self):   
        return self.check_rows() or self.check_columns() or self.check_diagonales()

    def check_rows(self):
        token_row = 0
        for row in range(self.row_count):
            for item in self.table[row]:
                if item == self.token:
                    token_row += 1
                    if token_row == 4:
                        return True
                else:
                    token_row = 0
        return False
    
    def check_columns(self):
        token_column = 0
        for column in range(self.column_count):
            for row in range(self.row_count):
                if self.table[row][column] == self.token:
                    
                    token_column += 1
                    if token_column == 4:
                        return True
                else:
                    token_column = 0
        return False
    
    def check_diagonales(self):

        
        for row in range(len(self.table)-3):
            for column in range(len(self.table[0])-3):
                
                
                if (self.table[row][column] == self.token and
                        self.table[row][column] == self.table[row+1][column+1] and
                        self.table[row][column] == self.table[row+2][column+2] and
                        self.table[row][column] == self.table[row+3][column+3]):
                        return True
                    # Check diagonal (up-right)
                if (self.table[row][column+3] == self.token and
                    self.table[row][column+3] == self.table[row+1][column+2] and
                    self.table[row][column+3] == self.table[row+2][column+1] and
                    self.table[row][column+3] == self.table[row+3][column]):
                    return True
        # for column in range(self.column_count):
        #     for row in range(self.row_count):

        #         # print(f"Checking item {row}, {column}")

        #         #Check upper left
        #         # print(f"Checking upper left diagonal {row + 1}, {column - 1}")
                
        #         if row + 1 < self.row_count and column - 1 >= 0:
        #             # print("Exist!")
        #             if self.table[row + 1][column - 1] == self.token:
        #                 token_diagonal += 1
        #                 if token_diagonal == 4:
        #                     return True
        #             else:
        #                 token_diagonal = 0


        #         #Check upper right
        #         # print(f"Checking upper right diagonal {row + 1}, {column + 1}")
        #         if row + 1 < self.row_count and column + 1 < self.column_count:
        #             # print("Exist!")
        #             if self.table[row + 1][column + 1] == self.token:
        #                 token_diagonal += 1
        #                 print(f"token_diagonal upper right: {token_diagonal}")
        #                 if token_diagonal == 4:
        #                     return True
        #             else:
        #                 token_diagonal = 0
        
        return False
        