


'''NONE = 0
BLACK = 1
WHITE = 2'''

class GameBoard:

    ''' Game board will be a two dimesional list of strings describing the
    game board. Each string is either None = '.', BLACK = 'B', or WHITE = 'W' '''

    def __init__(self, rows:int, cols:int, beg_piece: int): #OK
        self.rows = rows
        self.cols = cols
        self.beg_piece = beg_piece
        self.game_board = []

    
    def create_board(self): #OK
        for column in range(self.cols):
            self.game_board.append([])
            for row in range(self.rows):
                self.game_board[-1].append(0)
        return self.game_board
    
    def beg_pieces(self): #OK
        
        for column in range(self.cols):
            for row in range(self.rows):
                
                column = int(self.cols/2)-1
                row = int(self.rows/2)-1
                self.game_board[column][row] = self.beg_piece
                
                column2 = int(self.cols/2) 
                row2 = int(self.rows/2)
                self.game_board[column2][row2] = self.beg_piece

                if self.beg_piece == 1:
                    
                    
                    column3 = int(self.cols/2) 
                    row3 = int(self.rows/2)-1
                    self.game_board[column3][row3] = 2
                    
                    column4 = int(self.cols/2)-1
                    row4 = int(self.rows/2)
                    self.game_board[column4][row4] = 2
                    
                elif self.beg_piece == 2:

                                        
                    column3 = int(self.cols/2) 
                    row3 = int(self.rows/2)-1
                    self.game_board[column3][row3] = 1
                    
                    column4 = int(self.cols/2)-1
                    row4 = int(self.rows/2)
                    self.game_board[column4][row4] = 1
                
        return self.game_board
    

    def print_board(self): #OK
        
        board = self.game_board 
        
        for row in range(self.rows):
            for col in range(self.cols):
                if board[col][row] == 0:
                    print('.', end = ' ')
                elif board[col][row] == 1:
                    print('B', end = ' ')
                elif board[col][row] == 2:
                    print('W', end = ' ')
            print()
                
    





                   
