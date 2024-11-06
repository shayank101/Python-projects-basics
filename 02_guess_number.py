# Guess the number

import random

# print(random.randint(1,5))

def guess_game(x):
    random_number = random.randint(1,x)
    guess = 0
    
    # while condition terminates only when user guessed the random number.
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 to {x} : '))

        if guess > random_number:
            print(f'Too high...\nprevious guessed number {guess}')
        elif guess < random_number:
            print(f'Too low....\nprevious guessed number {guess}')
        
    # as soon as guess is correct while loop will be terminated and this will be executed
    print(f'You won! the number is {random_number}..')

guess_game(10)