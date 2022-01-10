
# CSE4256 Homework 1.
# Author: John Choi choi.1655@osu.edu
# Version: Jan 10, 2022

def guessing_game():
    """
    Problem 1.
    1. Generate a uniformly-distributed random number in the interval [1, 100]
    2. Prompt the user to enter a number (you may assume the user does, in fact, enter an integer, though not
        that it's a number in the appropriate range)
    3. Display a message to the user letting them know whether their guess was too high, too low, or correct
    4. If the guess was incorrect, prompt the user for another guess (again, assume the input is a valid integer)
    5. If the guess was correct, congratulate the user and tell them how many guesses it took to reach the correct answer.
    """
    # import random library for generating random number
    import random

    # welcome message
    print('Starting guessing game...')

    # generate a target number between 1 and 100 inclusive
    generated_number = random.randint(1, 100)

    counter = 1  # keep track of the user tries

    user_guess = int(input('Enter a number: '))

    # check if the guess was correct. If not, ask again
    while user_guess != generated_number:
        counter += 1  # increment the counter

        if user_guess > generated_number:
            print('Too high!')
        else:
            print('Too low!')
    
        user_guess = int(input('Enter another number: '))
    
    print('Correct!')
    print('You guessed the number in {} tries!'.format(counter))



if __name__ == '__main__':
    guessing_game()