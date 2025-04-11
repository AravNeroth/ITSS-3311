# Arav Neroth
# ITSS 3311 

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x300")

current_player = "X" 
board = [["" for _ in range(3)] for _ in range(3)]


# Function to check for a winner
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    for col in range(3):
        if board[0] [col] == board[1] [col] == board[2] [col] != "":
            return board[0] [col]
    if board[0][0] == board[1] [1] == board[2] [2] != "":
        return board[0][0]
    if board[0] [2] == board[1] [1] == board[2][0] != "":
        return board[0] [ 2]
    return None

# Function to handle button clicks
def on_button_click(row, col):
    global current_player
    if board[row] [col] == "":
        board[row] [col] = current_player
        buttons[row] [col].config(text=current_player)
        winner = check_winner()
        if winner:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_game()
        elif all(board[row] [col] != "" for row in range(3) for col in range(3)):
            messagebox. showinfo("Tic Tac Toe", "It's a tie!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Create the game board
"""buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=("Arial", 24), width=5, height=2, 
                                       command=lambda r=row, c=col: on_button_click(r, c))
    buttons[row][col].grid(row=row, column=col)"""

    # Create the game board
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(
            root, text="", font=("Arial", 24), width=5, height=2,
            command=lambda r=row, c=col: on_button_click(r, c)
        )
        buttons[row][col].grid(row=row, column=col)

# Function to reset the game
def reset_game():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row] [col]. config(text="")

root.mainloop()