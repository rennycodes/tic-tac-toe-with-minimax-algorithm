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

# Getting player input
def get_player_input(board):
    usr_inp = int(input("choose a board space 1-9: "))
    if usr_inp >= 1 and usr_inp <= 9 and board[usr_inp-1] == "-":
        board[usr_inp-1] = current_player
    else:
        print("Oh noo, that spot is already taken(*_*)")

# Check for win or tie
# Checking rows
def row(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

while game_running:
    display_board(board)
    get_player_input(board)