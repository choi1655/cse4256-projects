
# CSE4256 Homework 1.
# Author: John Choi choi.1655@osu.edu
# Version: Jan 10, 2022

def guessing_game() -> None:
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


def reversed_guessing_game() -> None:
    """
    Problem 2.
    Write a function in which the computer guesses a secret number that the user has thought of in the interval [1, 100].
    The computer should always succeed in 7 guesses or fewer. After each of the computer's guesses, it should prompt
    the user to enter one of L (if the guess was lower than the secret number), H (if the guess was higher than the secret number),
    or C (if the guess was correct). You may assume the user's response is always one of those three possibilities.
    """
    import random  # for random number generator

    def countdown():
        """ Simple inner function for handling the welcome messages """

        import time  # for countdown
        print('Think of a number between 1 and 100 in your head')
        time.sleep(1)  # pause for 1 sec
        print('Game starting in 3...')
        time.sleep(1)
        print('2...')
        time.sleep(1)
        print('1...')
        time.sleep(1)

    countdown()

    guessed = False
    left, right = 1, 100


    for _ in range(7):
        computer_guess = random.randint(left, right)  # computer guesses a number between the given range
        user_response = input('Computer guesses: {}. Is this correct?: '.format(computer_guess))

        if user_response == 'H':  # if guessed number is too high, lower the upper bound
            right = computer_guess
        elif user_response == 'C':
            guessed = True
            break
        else:  # if guessed number is too low, increase the lower bound
            left = computer_guess

    if not guessed:
        print('Computer failed to guess your number')
    else:
        print('Computer guessed your number correctly!')


def reversed_guessing_game2(min: int, max: int) -> None:
    """
    Problem 3.
    Add to parameters to the function so that its signature is reversed_guessing_game(min, max).
    The arguments min and max identify the range of values that the computer expects the user to select from (specifically,
    the interval [min, max]). Modify the body so that the computer will correctly guess a secret number in that range.
    Make the input handling more flexible. Permit the user to type lowercase characters as well as upper characters in their
    response. You may still assume the user's input is one of L, l, H, h, C, or c.
    Add a "cheat detector" to identify when the user tries to pull a fast one on the computer and gives inconsistent responses.
    Detecting the nature of the cheating is quite challenging (for example, whether they picked a number outside of the range, 
    they changed their number mid-game, or they gave a wrong response to one of the computer's guesses); simply notifying the
    user that they have cheated is sufficient.
    """
    import random  # for random number generator

    def countdown():
        """ Simple inner function for handling the welcome messages """

        import time  # for countdown
        print('Think of a number between 1 and 100 in your head')
        time.sleep(1)  # pause for 1 sec
        print('Game starting in 3...')
        time.sleep(1)
        print('2...')
        time.sleep(1)
        print('1...')
        time.sleep(1)

    countdown()

    possible_cheating_flag = False  # flag to indicate possible cheating

    print('Bounds are {} and {}.'.format(min, max))
    guessed = False
    left, right = min, max

    for _ in range(7):
        computer_guess = random.randint(left, right)  # computer guesses a number between the given range
        user_response = input('Computer guesses: {}. Is this correct?: '.format(computer_guess)).upper

        # check for cheat
        # check if user has out of bound number
        if computer_guess == max or computer_guess == min:
            possible_cheating_flag = True
        
        if user_response == 'H':  # if guessed number is too high, lower the upper bound
            right = computer_guess
        elif user_response != 'C':
            guessed = True
            break
        else:  # if guessed number is too low, increase the lower bound
            left = computer_guess
        
        if possible_cheating_flag:
            print('Possible cheating detected!')

    if not guessed:
        print('Computer failed to guess your number')
    else:
        print('Computer guessed your number correctly!')



if __name__ == '__main__':
    # guessing_game()  # Problem 1
    reversed_guessing_game()  # Problem 2
    # reversed_guessing_game2(10, 50)  # Problem 3