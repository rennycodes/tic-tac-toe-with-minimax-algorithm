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
        # Rows
        if board[i] == board[i + 3] == board[i + 6] and board[i] != "-":
            winner = board[i]
            game_running = False
            display_board(board)
            print(f"The winner is {winner}")
            return True  # Game won
        
        # Columns
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] and board[i * 3] != "-":
            winner = board[i * 3]
            game_running = False
            display_board(board)
            print(f"The winner is {winner}")
            return True  # Game won

    # Diagonals
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

    # Tie
    if "-" not in board:
        display_board(board)
        print("It's a tie")
        game_running = False
        return True  # Tie

    return False  # Game still running

# Check if the game is over
def game_over(board):
    return check_win(board) or "-" not in board

# Getting a list of possible moves(empty spaces) on board
def possible_moves(board):
    return[i + 1 for i in range(9) if board[i] == "-"]

# Make move on board
def make_move(board, move, maximizing_player):
    player = "X" if maximizing_player else "O"
    board[move - 1] = player
    return board

# Switch player
def switch_player():
    global current_player

    current_player = "O" if current_player == "X" else "X"

# Implementing the minimax algorithm
def minimax(board, depth, maximizing_player):
    if game_over(board) or depth == 0:
        if check_win(board):
            return -1 if maximizing_player else 1
        else:
            return 0
    
    if maximizing_player:
        max_eval = float('-inf')
        for move in possible_moves(board):
            eval = minimax(make_move(board, move, maximizing_player), depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in possible_moves(board):
            eval = minimax(make_move(board, move, maximizing_player), depth -1, True)
            min_eval = min(min_eval, eval)
        return min_eval

# Making the best move
def make_best_move(board):
    best_move = None
    max_eval = float('-inf')

    for move in possible_moves(board):
        eval = minimax(make_move(board, move, True), depth = 2, maximizing_player = False)
        if eval > max_eval:
            max_eval = eval
            best_move = move
    
    return best_move

# Random computer
def random_computer(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()

# A loop to make the game run continuously
"""
while game_running:
    display_board(board)
    get_player_input(board)
    
    if not game_running:
        break
    
    # Check if the game is over after the players move
    if game_over(board):
        break
    

"""
game_over(board)