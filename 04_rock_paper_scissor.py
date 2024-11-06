# rock - paper - Scissor

import random

def play():

    user_score = 0
    computer_score = 0

    while user_score != 2 and computer_score != 2:

        user = input("'r' for Rock, 'p' for Paper, 's' for Scissor : ")
        computer = random.choice(['r', 'p', 's'])

        if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or \
            (user == 's' and computer == 'p'):
            print(f'User : {user}, computer : {computer}')
            print('User won...!')
            user_score += 1
        elif user == computer:
            print(f'User : {user}, computer : {computer}')
            print("It's a Tie...")
        else :
            print(f'User : {user}, computer : {computer}')
            print('Computer won....') 
            computer_score += 1

    print(f'User score : {user_score}')
    print(f'Computer score : {computer_score}')

play()