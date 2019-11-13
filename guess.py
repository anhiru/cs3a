"""
guessing game using while loop
"""
import random

# create constant secret int value
SECRET_VALUE = random.randint(1, 101)

# welcome message
print('Try to guess the secret integer value...', end='\n\n')

# prompt for user's guesses
guessed_correctly = False
while not guessed_correctly:
    guess = int(input('Guess the number between 1-100: '))
    if guess > SECRET_VALUE:
        print('Too high, guess lower.')
    elif guess < SECRET_VALUE:
        print('Too low, guess higher.')
    else:
        print('\nYou found the secret number, ' + str(SECRET_VALUE) + '.')
        print('Congratulations!')
        guessed_correctly = True
