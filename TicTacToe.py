#: A TicTacToe game

board = {'top-L': 'x', 'top-M': 'o', 'top-R': 'x',
         'mid-L': 'x', 'mid-M': 'x', 'mid-R': 'o',
         'low-L': 'o', 'low-M': 'o', 'low-R': 'x'}

def board_display(board):
   print(board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'] + ' | ')
   print('------------')
   print(board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'] + ' | ')
   print('-------------')
   print(board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'] + ' | ')
    
board_display(board)

# next turn player 1 vs player 2
# check win - coulumn, row, diagonal
# play again, result, exit
