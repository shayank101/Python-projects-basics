# Here we will give the number to the computer
# and computer is going to guess the number .

# we have created 2 games here 
# guess_game2 : where correct number can be harcoded
# guess_game3 : where feedback is the only way

import random


# Here you can hard code the correct number 
def guess_game2(x):
    low = 1
    high = x
    random_number = 20
    feedback = ''

    # while loop will continue to run when the condition is True
    # c : correct
    # while will terminate only when feedback is c (correct)
    # 'c' != 'c' >>> False
    # 'w' != 'c' >>> True
    while feedback != 'c':
        guess = random.randint(low, high)

        # we made a bit automated now we only have to tell low or high 
        # as soon as the guess is correct break the loop
        if guess == random_number:
            break

        # feedback = input(f'Is {guess} too high (H), too low (L) or correct (C): ').lower()
        feedback = input(f'Is {guess} too high (H) || too low (L) : ').lower()

        if feedback == 'h':
            high = guess - 1 
        elif feedback == 'l':
            low = guess + 1
        
        
    print(f'The correct number is {random_number}')
    print('You won...!')


# guess_game2(20)




# Here you will give the feedback no hardcoded random number
def guess_game3(x):
    low = 1
    high = x
    feedback = ''

    # while loop will continue to run when the condition is True
    # c : correct
    # while will terminate only when feedback is c (correct)
    # 'c' != 'c' >>> False
    # 'w' != 'c' >>> True
    while feedback != 'c':
        guess = random.randint(low, high)

        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C): ').lower()

        if feedback == 'h':
            high = guess - 1 
        elif feedback == 'l':
            low = guess + 1
        
        
    print(f'The correct number is {guess}')
    print('You won...!')


guess_game3(400)
# correct num = 287