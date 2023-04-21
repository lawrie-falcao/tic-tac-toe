import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.master, text="", width=10, height=5,
                                   command=lambda row=row, col=col: self.handle_click(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=3, column=1)

    def handle_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win():
                messagebox.showinfo("Winner", f"{self.current_player} wins!")
                self.reset_game()
            elif self.check_tie():
                messagebox.showinfo("Tie", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True

        return False

    def check_tie(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
