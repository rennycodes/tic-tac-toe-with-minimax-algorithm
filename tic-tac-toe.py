player = 'O'
computer = 'X'

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
                exit()
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
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True

    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True

    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True

    elif (board[3] == board[5] and board[3] == board[7] and board[3] != ' '):
        return True

    else:
        return False

def check_which_spot_wins(spot):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == spot):
        return True
    
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == spot):
        return True
    
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == spot):
        return True
    
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == spot):
        return True
    
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == spot):
        return True

    elif (board[3] == board[6] and board[3] == board[9] and board[3] == spot):
        return True

    elif (board[1] == board[5] and board[1] == board[9] and board[1] == spot):
        return True

    elif (board[3] == board[5] and board[3] == board[7] and board[3] == spot):
        return True

    else:
        return False

def check_draw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def player_move():
    position = int(input("Enter a position for 'O': "))
    insert_letter(player, position)
    return

def computer_move():
    best_score = -800
    best_move = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, False)
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key
    
    insert_letter(computer, best_move)
    return

def minimax(board, maximizing):
    if check_which_spot_wins(computer):
        return 1
    
    elif check_which_spot_wins(player):
        return -1
    
    elif check_draw():
        return 0
    
    if maximizing:
        best_score = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, False)
                board[key] = ' '
                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '
                if score < best_score:
                    best_score = score
            return best_score

while not check_win():
    computer_move()
    player_move()

