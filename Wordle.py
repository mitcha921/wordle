# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    gw = WordleGWindow()

    random_word = random.choice(FIVE_LETTER_WORDS)

    for col in range(N_COLS):
        gw.set_square_letter(0, col, random_word[col])

    def enter_action(s):
        if s in FIVE_LETTER_WORDS:
            gw.show_message("'{}' is a possible word, great job!")
        else:
            gw.show_message("Sorry, '{}' is not in the word list.")

    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()