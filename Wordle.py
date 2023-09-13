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
    print("the word is " + random_word)

    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            if s.lower() == random_word.lower():
                gw.show_message("You win! The word is " + s)
            else:
                if gw.get_current_row() > 4 :
                    gw.show_message("Game over")
                else: 
                    gw.show_message("Try Again")
                gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Invalid word")

    gw.add_enter_listener(enter_action)
    

# Startup code

if __name__ == "__main__":
    wordle()