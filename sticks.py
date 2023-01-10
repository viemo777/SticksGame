import random

start_num = 15
first_player = 'Player 1'
second_player = 'Player 2'
last_player = random.choice(['Player 1', 'Player 2'])

def num_verif(num):
    if num < 1 or num > 3:
        print(f'Wrong number')
    return num < 1 or num > 3

def max_num(num):
    if num < 0:
        print(f'Wrong number')
    return num < 0

while start_num > 0:
    print(f'Max number of sticks is {start_num}')

    next_player = first_player if last_player == second_player else second_player
    num = int(input(f'{next_player}, choose sticks from 1 to 3: '))
    if num_verif(num):
        continue
    if max_num(start_num - num):
        continue
    elif start_num - num == 0:
        print(f'{next_player} is a winner')
        break
    last_player = next_player
    start_num -= num