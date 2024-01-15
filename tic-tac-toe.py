import random

# Variables
game_running = True
winner = None
current_player = "X"

# Creating the game board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# Displaying the game board
def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Getting player input
def get_player_input(board):
    usr_inp = int(input("Choose a board space 1-9: "))
    if usr_inp >= 1 and usr_inp <= 9 and board[usr_inp-1] == "-":
        board[usr_inp-1] = current_player
        switch_player()
    else:
        print("Oh noo, that spot is already taken (*_*)")

# Check for win or tie
# Checking rows, columns, and diagonals in a single function
def check_win(board):
    global game_running, winner

    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != "-":
            winner = board[i]
            game_running = False
            display_board(board)
            print(f"The winner is {winner}")
            return True  # Game won

        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] and board[i * 3] != "-":
            winner = board[i * 3]
            game_running = False
            display_board(board)
            print(f"The winner is {winner}")
            return True  # Game won

    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        game_running = False
        display_board(board)
        print(f"The winner is {winner}")
        return True  # Game won

    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        game_running = False
        display_board(board)
        print(f"The winner is {winner}")
        return True  # Game won

    if "-" not in board:
        display_board(board)
        print("It's a tie")
        game_running = False
        return True  # Tie

    return False  # Game still running

# Switch player
def switch_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# Random computer
def random_computer(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()

# A loop to make the game run continuously
while game_running:
    display_board(board)
    get_player_input(board)
    if not game_running:
        break
    random_computer(board)
    if not game_running:
        break
    game_running = not check_win(board)
