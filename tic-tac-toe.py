import random

# Variables
game_running = True
winner = None
current_player = "X"

# Creating the game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Displaying the game board
def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("----------")