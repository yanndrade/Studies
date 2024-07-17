import numpy as np
from random import randint

def create_game_board():
    board = np.array([[' ']*3 for _ in range(3)])
    return board

def print_game_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def move(player, row, col, board):
    if board[row][col]!=' ':
        print("Invalid move! Please choose an empty space.")
        return (board,False)
    board[row][col] = player
    return (board,True)

def check_rows(board: np.array):
    for i,row in enumerate(board):
        valcount = np.unique(row, return_counts=True)
        for val, count in zip(valcount[0],valcount[1]):
            if count == 3 and val != ' ':
                print(f"Vencedor: {val}, completou a row: {i}")
                return (True,val,i)
        
    return False

        

def check_columns(board):
    board = board.T
    for i,row in enumerate(board):
        valcount = np.unique(row, return_counts=True)
        for val, count in zip(valcount[0],valcount[1]):
            if count == 3 and val != ' ':
                print(f"Vencedor: {val}, completou a column: {i}")
                return (True,val,i)
        
    return False

def check_diagonal(board):
    diag1 = [board[0][0],board[1][1],board[2][2]]
    valcount = np.unique(diag1, return_counts=True)
    for val, count in zip(valcount[0],valcount[1]):
        if count == 3 and val != ' ':
            print(f"Vencedor: {val}, completou a diagonal: {1}")
            return (True,val,1)
        
    diag2 = [board[0][2],board[1][1],board[2][0]]
    valcount = np.unique(diag2, return_counts=True)
    for val, count in zip(valcount[0],valcount[1]):
        if count == 3 and val != ' ':
            print(f"Vencedor: {val}, completou a diagonal: {2}")
            return (True,val,2)
        
    return False


def check_tie(board):
    board.flatten()
    if ' ' not in board:
        print("Its a tie game")
        return True
    else: return False

def check_win(board):
    diag = check_diagonal(board)
    col = check_columns(board)
    row = check_rows(board)
    if diag == col == row == False:
        return False
    else: return True



"""board = create_game_board()

print_game_board(board)

board = move('O',0,2,board)
check_rows(board)
board = move('O',1,1,board)
check_rows(board)
board = move('O',2,0,board)
print_game_board(board)
# check_rows(board)
# check_columns(board)
# check_diagonal(board)

check_win(board)

"""

board = create_game_board()
while True:
    check = False
    while not check:
        board,check = move('O',randint(0,2),randint(0,2),board)
    print("O JOGOU")
    print_game_board(board)
    if check_win(board) or check_tie(board):
        break
    check = False
    while not check:
        board,check = move('X',randint(0,2),randint(0,2),board)
    print("X JOGOU")
    print_game_board(board)
    if check_win(board) or check_tie(board):
        break

print_game_board(board)

