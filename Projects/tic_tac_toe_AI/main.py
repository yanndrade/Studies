from game import *
from ai_player import *
import json


board = create_game_board()
q_table = defaultdict(lambda: np.zeros(9))




reward = None

result = {
    'X': 0,
    'O': 0,
    'Draw': 0
}

print("Qtable antes")
print(q_table)

winner = None

q_table = defaultdict(lambda: np.zeros(9))
result = {
    'X': 0,
    'O': 0,
    'Draw': 0
}


for n in range(100):
    board = create_game_board()
    reward = None
    winner = None

    HISTORY_STATES_ACTION=[]
    HISTORY_ACTION=[]
    HISTORY_AFTER_MOVE_STATES = []

    while True:
        X_player_possible_moves = get_possible_moves(board)
        X_move = random_move(X_player_possible_moves)
        board, _ = move('X',X_move,board)

        print("X Played")
        print_game_board(board)
        if check_win(board) or check_tie(board):
            if check_tie(board):
                reward = DRAW
                winner = 'Draw'
            else:
                reward = LOST
                winner = 'X'
            break
        

        O_move,act_state = ai_play(board,q_table)
        HISTORY_STATES_ACTION.append(act_state)
        HISTORY_ACTION.append(O_move) 
        board, _ = move('O',O_move,board)
        state_after_move = get_board_state(board)
        HISTORY_AFTER_MOVE_STATES.append(state_after_move)

        print("O Played")
        print_game_board(board)

        if check_win(board) or check_tie(board):
            if check_tie(board):
                reward = DRAW
                winner = 'Draw'
            else:
                reward = WIN
                winner = 'O'
            break
        
    history = {
    "states_action": HISTORY_STATES_ACTION,
    "actions": HISTORY_ACTION,
    "state_after_movie": HISTORY_AFTER_MOVE_STATES}

    print(history['actions'])
    print(history['states_action'])

    result[winner] += 1
    print(f"Reward AI: {reward}")
    q_table = update_q_table(history, reward,q_table)
     

print(q_table)



print(result)

for k,v in q_table.items():
    v = list(v)
with open('result.json', 'w') as fp:
    json.dump(result, fp)
    print("DEU CERTO SALVAR RESULTADOS")
    print(q_table)

with open('qtable.json', 'w') as fp:
    json.dump(q_table, fp)
    print("DEU CERTO SALVAR")
    





