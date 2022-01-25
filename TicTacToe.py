#: A classic TicTacToe game
# ------Global Variables------

board = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]
game_status = True
winner = None
current_player = "X"

def board_display():
   print(board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ')
   print('------------')
   print(board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ')
   print('-------------')
   print(board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ')
    
def start_game():
    board_display()
    # while the game is still running
    while game_status:
        
        player_input(current_player)
        check_if_game_over()
        switch_player()
        
        if winner == "X" or winner == "0":
            print(winner + " won.")
        elif winner == None:
            print("Tie.")

def player_input(player):
    print(player + "'s turn.")
    position = input("Choose a number from (1-9): ")
     
    # double loop to avoid over-riding positions and out of range nums.
    valid = False
    while not valid:
        
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input.Choose a number from (1-9): ")
        
        position = int(position) - 1
        
        if board[position] != ("X" or "0"):
            valid = True
        else:
            print("That spot is already taken. Try another")
    board[position] = player
    board_display()
    
def check_if_game_over():
    check_win()
    check_tie()

def check_win():
    global winner
    # Check rows, columns, and diagonal
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    
    if column_winner:
        winner = column_winner
    elif row_winner:
        winner = row_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global game_status
    # Check if the rows are same
    row_1 = board[0] == board[1] == board[2]
    row_2 = board[3] == board[4] == board[5]
    row_3 = board[6] == board[7] == board[8]

    if row_1 or row_2 or row_3:
      game_status = False

    if row_1:
      return board[0]
    elif row_2:
      return board[3]
    elif row_3:
      return board[6]
    return


def check_columns():
    global game_status
    # Check if the rows are same
    column_1 = board[0] == board[3] == board[6]
    column_2 = board[1] == board[4] == board[7]
    column_3 = board[2] == board[5] == board[8]

    if column_1 or column_2 or column_3:
      game_status = False

    if column_1:
      return board[0]
    elif column_2:
      return board[1]
    elif column_3:
      return board[2]
    return

def check_diagonals():
    global game_status
    # Check if the rows are same
    diagonal_1 = board[0] == board[4] == board[8]
    diagonal_2 = board[3] == board[4] == board[6]

    if diagonal_1 or diagonal_2:
      game_status = False

    if diagonal_1:
      return board[0]
    elif diagonal_2:
      return board[3]
    return

def check_tie():
    global game_status
    for i in board:
        if i.isnumeric():
            game_status = True
    return

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return
         
start_game()
