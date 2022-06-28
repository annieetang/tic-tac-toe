# Tic Tac Toe Game built with Python and Tkinter GUI
# Annie Tang, June 2022 
# to run: python3 tic-tac-toe.py

# import tkinter for GUI window
import tkinter as tk 
from tkinter import font
from typing import NamedTuple
from itertools import cycle 

class Player(NamedTuple):
    label: str
    color: str 

class Move(NamedTuple):
    row: int 
    col: int 
    label: str = ""

# defining constants for game
BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"), 
    Player(label="O", color="green")
)

class Game:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players) # cyclical iterator for players
        self.board_size = board_size 
        self.current_player = next(self.players)
        self.winner_combo = [] 
        self._current_moves = []
        self._has_winner = False 
        self._winnning_combos = []
        self._setup_board()
    
    def _setup_board(self):
        self._current_moves = [
            # try to rewrite: 
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]

        self._winning_combos = self._get_winning_combos()
    
    def _get_winning_combos(self):
        # try to rewrite:

        rows = [
            [(move.row, move.col) for move in row]
            for row in self._current_moves 
        ]

        columns = [list(col) for col in zip(*rows)]
        
        first_diagonal = [row[i] for i, row in enumerate(rows)]

        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]

        return rows + columns + [first_diagonal, second_diagonal]
    
    def is_valid_move(self, move):
        row, col = move.row, move.col 
        move_not_played = (self.current_moves[row][col].label == "")
        no_winner = not self._has_winner 
        return no_winner and move_not_played

class Board(tk.Tk):
    # initializing parent class Tk
    def __init__(self):
        super().__init__() 
        self.title("Tic-Tac-Toe Game")
        self._cells = {}
        self.display()
        self.grid()
    
    # create board display
    def display(self):
        # create Frame object from tk
        display_frame = tk.Frame(master=self)

        # ensuring resizes are proportional
        display_frame.pack(fill=tk.X)

        # creating Label object from tk
        self.display = tk.Label(
            master = display_frame, 
            text = "Ready?",
            font = font.Font(size=28, weight="bold")
        )
        self.display.pack()
    
    # creating board's grid using buttons
    def grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()

        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)

            for column in range(3):

                # create button for every cell 
                button = tk.Button(
                    master = grid_frame,
                    text = "", 
                    font = font.Font(size=36, weight="bold"), 
                    fg =  "black", 
                    width = 3, 
                    height = 2, 
                    highlightbackground = "#d2d7fa"
                )

                # add button to cells dictionary as button:coordinate key:value pair 
                self._cells[button] = (row, column)

                # add every button to main window
                button.grid(
                    row = row, 
                    column = column, 
                    padx = 2, 
                    pady = 2, 
                    sticky = "nsew"
                )
    


def main():
    # creating board and running its main loop
    board = Board()
    board.mainloop()

if __name__ == "__main__":
    main()