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
        
        player_input()
        check_if_game_over()
        switch_player()
        
        if winner == "X" or winner == "0":
            print(winner + "won.")
        elif winner == None:
            print("Tie.")

def check_if_game_over():
    check_win()
    check_tie()

def check_win():
    # Check rows, columns, and diagonal
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    return

def check_rows():
    return

def check_columns():
    return

def check_diagonals():
    return

def check_tie():
    return

def switch_player():
    return
         
