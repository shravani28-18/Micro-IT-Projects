import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.buttons = []
        self.is_x = True  # True for X, False for O

        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=('Arial', 40), width=5, height=2,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def on_click(self, index):
        button = self.buttons[index]
        if button["text"] == "":
            button["text"] = "X" if self.is_x else "O"
            button.config(state="disabled")
            self.is_x = not self.is_x
            self.check_win()

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in win_combinations:
            a, b, c = combo
            if (self.buttons[a]["text"] == self.buttons[b]["text"] ==
                self.buttons[c]["text"] != ""):
                messagebox.showinfo("Game Over", f"{self.buttons[a]['text']} wins!")
                self.reset_game()
                return

        if all(button["text"] != "" for button in self.buttons):
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()

    def reset_game(self):
        for button in self.buttons:
            button["text"] = ""
            button.config(state="normal")
        self.is_x = True


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    game = TicTacToeGame(root)
    root.mainloop()
