class MakeMove:

    def __init__(self, board: [list], game_rows: int, game_cols: int, move_col: int, move_row: int, turn:int):
        self.board = board
        self.move_row = move_row
        self.move_col = move_col
        self.game_rows = game_rows
        self.game_cols = game_cols
        self.turn = turn

    def check_game_pieces(self, turn:int):
        board = self.board
        num_of_color = 0
        for col in range(self.game_cols):
            for row in range(self.game_rows):
                if board[col][row] == turn:
                    num_of_color += 1
        if num_of_color == 0:
            return False
        else:
            return True
                
                
    def check_game(self):
        ''' checks to see if there are any blanks spaces available to place a piece.
    If there aren't any, it return False'''
        board = self.board 
        num_of_blanks = 0
        
        for col in range(self.game_cols):
            for row in range(self.game_rows):
                if board[col][row] == 0:
                    num_of_blanks += 1
                    
        if num_of_blanks == 0:
            return False
        else:
            return True
                              
    def check_pieces_around(self, turn: int):
        ''' Checks to see if any of the pieces beginning at the specified cell and
    extending in any of the eight possible directions are of the opposite color'''
        
        board = self.board
        if turn == 1:
            opposite_player = 2
        if turn == 2:
            opposite_player = 1

        move_cell = board[self.move_col][self.move_row]

        x = self.move_col
        y = self.move_row

        if move_cell == 0:

            return board[x+0][y+1] == opposite_player \
            or board[x+1][y+1]== opposite_player \
            or board[x+1][y+0]== opposite_player \
            or board[x+1][y-1]== opposite_player \
            or board[x+0][y-1]== opposite_player \
            or board[x-1][y-1]== opposite_player \
            or board[x-1][y+0]== opposite_player \
            or board[x-1][y+1]== opposite_player 

    def make_move(self, turn: int):
        eight_dir = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        colx = self.move_col
        rowy = self.move_row
        game_rows = self.game_rows
        game_cols = self.game_cols
        board = self.board
   

        flip_pieces = []
        
        if turn == 1:
            other_color = 2
        elif turn == 2:
            other_color = 1
            
        for x_dir, y_dir in eight_dir:
            col = colx
            row = rowy
            col += x_dir
            row += y_dir
            if _check_on_board(game_rows, game_cols, col, row) and board[col][row] == other_color:
                col += x_dir
                row += y_dir
                if not _check_on_board(game_rows, game_cols, col, row):
                    continue 
                while board[col][row] == other_color:
                    col += x_dir
                    row += y_dir
                    if not _check_on_board(game_rows, game_cols, col, row):
                        break
                if not _check_on_board(game_rows, game_cols, col, row):
                    continue
                if board[col][row] == turn:
                    while True:
                        col -= x_dir
                        row -= y_dir
                        if col == colx and row == rowy:
                            break
                        flip_pieces.append((col, row))
                      
        return flip_pieces
    
    def valid_move(self, turn:int, list_of_flips: list):
        list_of_flips = self.make_move(turn)
        if len(list_of_flips) == 0:
            return False
        else:
            return True
        
    def flip_pieces(self, turn: int):
        col = self.move_col
        row = self.move_row
        board = self.board
        list_of_flips = self.make_move(turn)
        if self.valid_move(turn, list_of_flips) == True:
            print('VALID')
            board[col][row] = turn
            for col, row in list_of_flips:
                board[col][row] = turn
            return board
    
        elif self.valid_move(turn, list_of_flips) == False :
            print('INVALID')
            raise Exception

    

    def print_board(self, turn:int, board_list: [list]):
                
        for row in range(self.game_rows):
            for col in range(self.game_cols):
                if board_list[col][row] == 0:
                    print('.', end = ' ')
                elif board_list[col][row] == 1:
                    print('B', end = ' ')
                elif board_list[col][row] == 2:
                    print('W', end = ' ')
            print()

    def game_over(self, turn: int):
        return self.check_game() and  self.check_game_pieces(turn)   

    def _change_turn(self, turn: int):
        if turn == 1:
            return 2
        else:
            return 1
        
    def get_winner(self, way_to_win: str, turn:int):
        board = self.flip_pieces(turn)
        white_pieces = 0
        black_pieces = 0

        for col in range(self.game_cols):
            for row in range(self.game_rows):
                if board[col][row] == 1:
                    black_pieces += 1
                    
        for col in range(self.game_cols):
            for row in range(self.game_rows):
                if board[col][row] == 2:
                    white_pieces += 1

        if way_to_win == '>':
            if black_pieces > white_pieces:
                print ('WINNER: BLACK')
            elif white_pieces > black_pieces:
                print ('WINNER: WHITE')
            else:
                print('WINNER: NONE')
                
        if way_to_win == '<': 
            if black_pieces < white_pieces:
                print ('WINNER: BLACK')
            elif white_pieces < black_pieces:
                print ('WINNER: WHITE')
            else:
                print('WINNER: NONE') 
        
    def get_score(self, turn:int):
        board = self.flip_pieces(turn)
        white_pieces = 0
        black_pieces = 0

        for col in range(self.game_cols):
            for row in range(self.game_rows):
                if board[col][row] == 1:
                    black_pieces += 1
                    
        for col in range(self.game_cols):
            for row in range(self.game_rows):
                if board[col][row] == 2:
                    white_pieces += 1
        print ('B: {}'.format(black_pieces))
        print('W: {}'.format(white_pieces))
                
def _check_on_board(game_rows: int, game_cols: int, col: int, row: int):
    
    if 0 > col >= game_cols or 0 > row >= game_rows:
        return False
    else:
        return True



        
