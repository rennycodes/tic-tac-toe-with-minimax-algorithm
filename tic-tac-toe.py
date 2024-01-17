# Creating the game board
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

# Displaying the game board
def display_board(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("--+---+--")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("--+---+--")
    print(board[7] + " | " + board[8] + " | " + board[9])

def  space_is_free(position):
    if board[position] == ' ':
        return True
    return False

def insert_letter(letter, position):
    if space_is_free(position):
        board[position] = letter
        display_board(board)

        if check_draw():
            print("Draw!")
            exit()
        
        if check_win():
            if letter == 'X':
                print("Bot wins!")
            else:
                print("Player wins!")
                exit()
        return
    
    else:
        print("Invalid position")
        position = int(input("Please enter a new position: "))
        insert_letter(letter, position)
        return

def check_win():
    pass















# # Getting a list of possible moves(empty spaces) on board
# def possible_moves(board):
#     return[i + 1 for i in range(9) if board[i] == "-"]

# # Make move on board
# def make_move(board, test, maximizing_player):
#     global move
#     move = test
#     move = possible_moves(board)
#     player = "X" if maximizing_player else "O"
#     for m in move:

#         board[m - 1] = player
#     return board

# # Switch player
# def switch_player():
#     global current_player

#     current_player = "O" if current_player == "X" else "X"

# # Implementing the minimax algorithm
# def minimax(board, depth, maximizing_player):
#     if game_over(board) or depth == 0:
#         if check_win(board):
#             return -1 if maximizing_player else 1
#         else:
#             return 0
    
#     if maximizing_player:
#         max_eval = float('-inf')
#         for move in possible_moves(board):
#             eval = minimax(make_move(board, move, maximizing_player), depth - 1, False)
#             max_eval = max(max_eval, eval)
#         return max_eval
#     else:
#         min_eval = float('inf')
#         for move in possible_moves(board):
#             eval = minimax(make_move(board, move, maximizing_player), depth -1, True)
#             min_eval = min(min_eval, eval)
#         return min_eval

# # Making the best move
# def make_best_move(board):
#     best_move = None
#     max_eval = float('-inf')

#     for move in possible_moves(board):
#         eval = minimax(make_move(board, move, True), depth = 2, maximizing_player = False)
#         if eval > max_eval:
#             max_eval = eval
#             best_move = move
    
#     return best_move

# # Random computer
# def random_computer(board):
#     global move
#     while current_player == "O":
#         position = make_move(board, move, True)
#         if board[position] == "-":
#             board[position] = "O"
#             switch_player()

# # A loop to make the game run continuously

# while game_running:
#     display_board(board)
#     get_player_input(board)
#     game_over(board)
#     random_computer(board)
# """
#     if not game_running:
#         break
    
#     # Check if the game is over after the players move
#     if game_over(board):
#         break
    

# """