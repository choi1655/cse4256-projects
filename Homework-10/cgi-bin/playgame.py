#!/usr/bin/python3

"""File: playgame.py
Author: John Choi choi.1655@osu.edu
Version: April 10, 2022

The Ohio State University CSE4256 SP22 Homework 10.
"""

import cgi
import cgitb
from cardutils import play_game, std_card_deck

cgitb.enable()

print("Content-Type: text/html")
print()

data = cgi.FieldStorage()
num_players = int(data.getvalue("nplayers"))
print(f"<TITLE>Playing the card game with {num_players} players!</TITLE>")
print("<H1>Output file has been created</H1>")

deck = std_card_deck()
output_filename = 'game.csv'

play_game(deck, num_players, output_filename)
