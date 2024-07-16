import numpy as np

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
        return board
    board[row][col] = player
    return board

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




def check_win(board): ...



board = create_game_board()

print_game_board(board)

board = move('X',0,2,board)
check_rows(board)
board = move('X',1,1,board)
check_rows(board)
board = move('X',2,0,board)
print_game_board(board)
check_rows(board)
check_columns(board)
check_diagonal(board)