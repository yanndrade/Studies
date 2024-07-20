import numpy as np
from random import randint

def create_game_board():
    board = np.array([[' ']*3 for _ in range(3)])
    return board

def print_game_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def get_possible_moves(board):
    possible = []
    for i in range(len(board[0])):  #row
        for j in range(len(board)): #element of the row
            if board[i][j] == ' ':
                possible.append((i,j))
    return possible

def random_move(possible):
    rng = np.random.default_rng()
    choice = rng.choice(possible,1)
    return tuple(choice[0])


def move(player, coords, board):
    row = coords[0]
    col = coords[1]
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
                print(f"Winner: {val}, completed the row: {i}")
                return (True,val,i)
        
    return False

def check_columns(board):
    board = board.T
    for i,row in enumerate(board):
        valcount = np.unique(row, return_counts=True)
        for val, count in zip(valcount[0],valcount[1]):
            if count == 3 and val != ' ':
                print(f"Winner: {val}, completed the column: {i}")
                return (True,val,i)
        
    return False

def check_diagonal(board):
    diag1 = [board[0][0],board[1][1],board[2][2]]
    valcount = np.unique(diag1, return_counts=True)
    for val, count in zip(valcount[0],valcount[1]):
        if count == 3 and val != ' ':
            print(f"Winner: {val}, completed the diagonal: {1}")
            return (True,val,1)
        
    diag2 = [board[0][2],board[1][1],board[2][0]]
    valcount = np.unique(diag2, return_counts=True)
    for val, count in zip(valcount[0],valcount[1]):
        if count == 3 and val != ' ':
            print(f"Winner: {val}, completed the diagonal: {2}")
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

    temp = [diag,col,row]

    if diag == col == row == False:
        return False
    else:
        return True



