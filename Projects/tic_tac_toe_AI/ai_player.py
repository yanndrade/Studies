from collections import defaultdict
import numpy as np
from game import *
import sys


INF = sys.maxsize

WIN =  1
DRAW = 0
LOST = -1
EXPLORATION = 0.01 
LR = 0.5
GAMMA = 0.8 


MAPP ={
        0: (0,0),
        1: (0,1),
        2: (0,2),

        3: (1,0),
        4: (1,1),
        5: (1,2),

        6: (2,0),
        7: (2,1),
        8: (2,2),
    }



HISTORY_STATES_ACTION=[]
HISTORY_ACTION=[]
HISTORY_AFTER_MOVE_STATES = []

"""
Qtable
                              Actions
                              A(0,0) A(0,1) A(0,2) A(1,0) A(1,1) A(1,2) A(2,0) A(2,1) A(2,2)
                    State
"""


""" 
Rascunho

q_table = defaultdict(lambda: np.zeros(9))

state = np.array([['X', ' ', 'O'],
                  [' ', 'X', ' '],
                  [' ', 'O', ' ']])

#state_key = str(state.reshape(9))
state_key = get_board_state(state)
q_values = q_table[state_key]

#q_values[1] = 0.5

print(get_board_state(state))
print(q_values)

state2 = np.array([['X', ' ', 'O'],
                  [' ', 'X', ' '],
                  [' ', 'X', ' ']])

state_key2 = get_board_state(state2)
q_values2 = q_table[state_key2]
action = np.argmax(q_values2)


print(f'Ação: {action}')

print(get_board_state(state2))
print(q_values2)

print(q_table)


    
def update_q_table(history, reward, q_table):
    
def update_q_table(history, reward, q_table):
    
def update_q_table(history, reward, q_table):



"""

def board_traitment(board):
    mapp = {'X': 1, 'O': -1, ' ': 0}
    transf = np.vectorize(mapp.get)
    return transf(board).flatten()

def get_board_state(board):
    #board_s = board_traitment(board)
    return str(board.reshape(9))

def get_index_from_move(value):
    return [k for k,v in MAPP.items() if v == value][0]

def get_move_from_q_values(q_values,poss):
    act,index = MAPP[np.argmax(q_values)], np.argmax(q_values) 
    if act in poss:
        return act
    else:
        print("Impossible move, taking random action")
        return random_move(poss)
    
def update_q_table(history, reward, q_table):
    print("call funcao update")
    states_action = list(reversed(history['states_action']))
    state_after_move = list(reversed(history['state_after_movie']))
    actions = list(reversed(history['actions']))
    
    for i,action in enumerate(actions):
        print(f"MODIFICANDO O ESTADO {states_action[i]}")
        # ACTUAL
        q_values_actual_state_list = q_table[states_action[i]]
        action_2_update = get_index_from_move(action)

        # NEXT STATE
        q_values_next_state_list = q_table[state_after_move[i]]

        # UPDATE
        q_values_actual_state_list[action_2_update] = (1-LR)*q_values_actual_state_list[action_2_update] + LR*(reward + GAMMA*max(q_values_next_state_list))

        print(f"NOVO VALOR DA ACAO {action_2_update} = {q_values_actual_state_list[action_2_update]}")
        q_table[states_action[i]] = list(q_values_actual_state_list)
        print(type(q_table[states_action[i]]))

    
    return q_table


def ai_play(board,q_table):
    if np.random.uniform(0,1) < EXPLORATION:
        poss = get_possible_moves(board)
        actual_state = get_board_state(board)
        action_O = random_move(poss)
        print(f'RANDOM MOVE{action_O}')
        #HISTORY_STATES_ACTION.append(actual_state)
        #HISTORY_ACTION.append(action_O) 
        
       
    else:
        actual_state = get_board_state(board)
        q_values_actual_state = q_table[actual_state]
        poss = get_possible_moves(board)
        action_O = get_move_from_q_values(q_values_actual_state,poss)
        print(f'TRYING Q TABLE ACTION{action_O}')
        #HISTORY_STATES_ACTION.append(actual_state)
        #HISTORY_ACTION.append(action_O) 

    print("HISTORICO ADICIONADO")
    return action_O, actual_state
   


####   GAME

'''


history_states_action=[]
history_action=[]
history_after_move_states = []

board = create_game_board()

print("Q TABLE CRIADA")
q_table = defaultdict(lambda: np.zeros(9))



poss = get_possible_moves(board)
print("X MOVE")
board,_ = move('X', random_move(poss), board)
#board,_ = move('X', (0,0), board)

print_game_board(board)




print("O MOVE")
board,_ = move('O',action_O,board)
state_after_move = get_board_state(board)

history_after_move_states.append(state_after_move)



print_game_board(board) 
poss = get_possible_moves(board)
print("X MOVE")
board,_ = move('X', random_move(poss), board)


print_game_board(board)



print("O MOVE")
board,_ = move('O',action_O,board)
state_after_move = get_board_state(board)

history_after_move_states.append(state_after_move)


history = {
    "states_action": history_states_action,
    "actions": history_action,
    "state_after_movie": history_after_move_states
}

#poss = get_possible_moves(board)

#board,_ = move()
print_game_board(board) 

print("Q TABLE ANTES DA REWARD")
print(q_table)

q_dps = update_q_table(history,10000,q_table)

print("Q TABLE DEPOIS DA REWARD")
print(q_dps)

'''