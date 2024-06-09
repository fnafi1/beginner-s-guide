import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Крестики-нолики")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.root, text=" ", font=("Arial", 24), command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Победа!", f"Игрок {self.current_player} победил!")
                self.root.quit()
            elif " " not in self.board:
                messagebox.showinfo("Ничья", "Ничья! Игра окончена.")
                self.root.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
