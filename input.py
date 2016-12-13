

import tkinter
import GUI



DEFAULT_FONT = ('Helvetica', 14)





class InputDialog:
    def __init__(self):

        root = tkinter.Tk()
        root.withdraw()
        self._dialog_window = tkinter.Toplevel()

        play_rule_label = tkinter.Label(
            master = self._dialog_window, text = 'How would you like to play?',
            font = DEFAULT_FONT)

        play_rule_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        row_label = tkinter.Label(
            master = self._dialog_window, text = 'Row:',
            font = DEFAULT_FONT)

        row_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._row_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._row_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        col_label = tkinter.Label(
            master = self._dialog_window, text = 'Col:',
            font = DEFAULT_FONT)

        col_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._col_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._col_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)
        
        first_player_label = tkinter.Label(
            master = self._dialog_window, text = 'First Player:',
            font = DEFAULT_FONT)

        first_player_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._first_player_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._first_player_entry.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        top_left_label = tkinter.Label(
            master = self._dialog_window, text = 'Player To Occupy Top Left Position:',
            font = DEFAULT_FONT)

        top_left_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._top_left_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._top_left_entry.grid(
            row = 4, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)
        
        way_to_win_label = tkinter.Label(
            master = self._dialog_window, text = 'Player w/ Most(>) or Least(<) Discs Wins:',
            font = DEFAULT_FONT)

        way_to_win_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._way_to_win_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._way_to_win_entry.grid(
            row = 5, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)
        

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)



        self._ok_clicked = False
        self._row = ''
        self._col = ''
        self._first_player = ''
        self._top_left = ''
        self._way_to_win = ''


    def show(self) -> None:
        
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()



    def was_ok_clicked(self) -> bool:
        return self._ok_clicked


    def get_row(self) -> str:
        return self._row


    def get_col(self) -> str:
        return self._col

    def get_first_player(self) -> str:
        return self._first_player

    def get_top_left(self) -> str:
        return self._top_left

    def get_way_to_win(self) -> str:
        return self._way_to_win

    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self._row = self._row_entry.get()
        self._col = self._col_entry.get()
        self._first_player = self._first_player_entry.get()
        self._top_left = self._top_left_entry.get()
        self._way_to_win = self._way_to_win_entry.get()

        self._dialog_window.destroy()


    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()

#################
#################
################



if __name__ == '__main__':
    x = InputDialog()
    #x.start()
    x.show()
    newgame = GUI.OthelloGui(int(x._row),int(x._col), x._first_player, x._top_left, x._way_to_win)

