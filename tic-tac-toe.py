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

# Checking columns
def columns(baord):
    global winner

    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True

    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
# Checking diagonals:
    def diagonal(board):
        global winner

        if board[0] == board[5] == board[8] and board[0] != "-":
            winner = board[0]
            return True
        
        elif board[2] == board[5] == board[6] and board[2] != "-":
            winner = board[2]
            return True
        
# Checking tie
def tie(board):
    global winner

    if "-" not in board:
        display_board(board)
        print("it's a tie")
        game_running = False


while game_running:
    display_board(board)
    get_player_input(board)