"""File: main.py
Author: John Choi choi.1655@osu.edu
Version: April 3, 2022

The Ohio State University CSE4256 SP22 Homework 9.
"""

import cards

# TODO: This main program should raise no exceptions when run with "python3 main.py".
# Implement the functions in cards.py and change the csv filename and n_players argument as needed,
# but do not otherwise change this code.
the_deck = cards.std_card_deck()
cards.play_game(the_deck, 4, "game.csv")
# cards.review_game("game.csv", 4)
