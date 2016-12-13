

import tkinter
import math
import gamelogic
import beggameboard

class OthelloGui:

    def __init__(self, row_num, col_num, first_player, top_left, way_to_win ):
        self._window = tkinter.Tk()
        
        self._row_num = row_num
        self._col_num = col_num
        self._first_player = first_player
        self._top_left = top_left
        self._way_to_win = way_to_win


        
        self._canvas = tkinter.Canvas(
            master = self._window,
            height = 640,
            width = 640,
           background = 'blue')
        
        self._canvas.grid(
            row = 1, column =0, 
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)



        if self._first_player == 'B':
            self._first_player = 1
        if self._first_player == 'W':
            self._first_player = 2

        if self._top_left == 'B':
            self._top_left = 1
        if self._top_left == 'W':
            self._top_left = 2

        self._canvas.bind('<Configure>', self.canvas_resize)
        self._window.rowconfigure(0, weight = 1)
        self._window.columnconfigure(0, weight = 1)

        self._canvas.bind('<Button-1>', self.on_click)
        
       
    
    def start(self): 
        self._window.mainloop()


    def canvas_resize(self, event: tkinter.Event):
        self.once_resized()
        

    def once_resized(self):
        self._canvas.delete(tkinter.ALL)
        self._draw_grid()
        self._draw_circles()
        self.game_style()
      

    def _draw_grid(self):
        
        length_row = self._canvas.winfo_height()/self._row_num
        width_col = self._canvas.winfo_width()/self._col_num


        for x in range(self._col_num):
            for y in range(self._row_num):
                x_one = x * width_col
                x_two = x * width_col + width_col
                y_one = y * length_row
                y_two = y * length_row + length_row


                
                self._canvas.create_rectangle(x_one, y_one, x_two, y_two)
        
        
        self._window.update()
        self._canvas.grid(
            row = 1, column = 0, padx = 3, pady = 3,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

    def _draw_circles(self):
        length_row = self._canvas.winfo_height()/self._row_num
        width_col = self._canvas.winfo_width()/self._col_num

        if self._top_left == 'B':
            self._top_left = 1
        elif self._top_left == 'W':
            self._top_left = 2

        board = beggameboard.GameBoard(self._row_num, self._col_num, self._top_left)
        board.create_board()
        self._board_list = board.beg_pieces()

        
        if self._top_left == 1:
            color = 'black'
            other_color = 'white'
        elif self._top_left == 2:
            color = 'white'
            other_color = 'black'

        col1 = (self._col_num/2) -1
        x1 = col1 * width_col
        row1 = (self._row_num/2) -1
        y1 = row1 * length_row

        col2 = (self._col_num/2)
        x2 = col2 * width_col
        row2 = (self._row_num/2) 
        y2 = row2 * length_row

        self._canvas.create_oval(x1, y1, x2, y2, outline = 'black' , fill = color)

        col3 = (self._col_num/2) + 1
        x3 = col3 * width_col
        row3 = (self._row_num/2) + 1
        y3 = row3 * length_row

        self._canvas.create_oval(x2, y2, x3, y3, outline = 'black', fill = color)

        col4 = (self._col_num/2) - 1
        x4 = col4 * width_col
        row4 = (self._row_num/2) 
        y4 = row4* length_row

        col5 = (self._col_num/2) 
        x5 = col5 * width_col
        row5 = (self._row_num/2) + 1 
        y5 = row5 * length_row
        self._canvas.create_oval(x4, y4, x5, y5, outline = 'black', fill = other_color)

        col6 = (self._col_num/2) 
        x6 = col6 * width_col
        row6 = (self._row_num/2) - 1
        y6 = row6 * length_row

        col7 = (self._col_num/2) + 1
        x7 = col7 * width_col
        row7 = (self._row_num/2) 
        y7 = row7 * length_row
        self._canvas.create_oval(x6, y6, x7, y7, outline = 'black', fill = other_color)

    def on_click(self, event: tkinter.Event):
        length_row = self._canvas.winfo_height()/self._row_num
        width_col = self._canvas.winfo_width()/self._col_num

        

        
        self._rowforlogic = math.floor(event.y/length_row)
        self._colforlogic = math.floor(event.x/width_col)

        self.make_move()

        moves = gamelogic.MakeMove(self._board_list, self._row_num, self._col_num, self._colforlogic, self._rowforlogic, self._first_player)
        if moves.game_over(self._first_player) == True:
                    try:
                    
                        
                        moves.make_move(self._first_player)
                        self._board_list = moves.flip_pieces(self._first_player)
                        self._first_player = moves._change_turn(self._first_player)
                        self.board_list_drawn()
                        self.get_score() 
                    except:
                        print('INVALID')
    
        self._button2 = tkinter.Button(master = self._window,
                                       text = self.get_score(),
                                       font = ('Helvetica', 15))
        self._button2.grid(
            row = 2, column = 0, padx = 0, pady = 0,
            sticky = tkinter.W + tkinter.S)


    def game_style(self):
        
        self._button1 = tkinter.Button(master = self._window,
                                      text = "FULL",
                                      font = ('Helvetica', 15))
        
        self._button1.grid(
            row = 0, column = 0, padx = 0, pady = 0,
           sticky = tkinter.W + tkinter.N)

        #self.get_score()




    def get_score(self):
        board_list = self._board_list
        white_pieces = 0
        black_pieces = 0

        for col in range(self._col_num):
            for row in range(self._row_num):
                if board_list[col][row] == 1:
                    black_pieces += 1
                    
        for col in range(self._col_num):
            for row in range(self._row_num):
                if board_list[col][row] == 2:
                    white_pieces += 1
                    
        return('W: {}, B: {}'.format(white_pieces, black_pieces))


    def make_move(self):
        self._col = self._colforlogic
        self._row = self._rowforlogic

        print(self._col, self._row)

    def board_list_drawn(self):
        
        board_list = self._board_list
        length_row = self._canvas.winfo_height()/self._row_num
        width_col = self._canvas.winfo_width()/self._col_num
        
        for x in range(self._col_num):
            for y in range(self._row_num):
                if board_list[x][y] == 0:
                    continue
                elif board_list[x][y] == 1:
                
                    x1 = x * width_col
                    y1 = y * length_row
                    x2 = (x + 1) * width_col
                    y2 = (y + 1) * length_row
                    self._canvas.create_oval(x1, y1, x2, y2, outline = 'black', fill = 'black')
                    

                    
                elif board_list[x][y] == 2:
                    x1 = x * width_col
                    y1 = y * length_row
                    x2 = (x + 1) * width_col
                    y2 = (y + 1) * length_row
                    self._canvas.create_oval(x1, y1, x2, y2, outline = 'black', fill = 'white')
        
