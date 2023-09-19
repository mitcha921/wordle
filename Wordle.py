# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():

    gw = WordleGWindow()

    random_word = random.choice(FIVE_LETTER_WORDS)
    print("the word is " + random_word)

    def enter_action(s):
        if s.strip().lower() == "":
            # If the input string is empty or contains only whitespace, do nothing
            return
        if s.lower() in FIVE_LETTER_WORDS:
            if s.lower() == random_word.lower():
                gw.show_message("You win! The word is " + s)
            else:
                if gw.get_current_row() > 4 :
                    gw.show_message("Game over. The correct word was \"" + random_word + "\"")
                else: 

                    correct_letter = []
                    present_letter = []
                    missing_letter = []

                    for col in range(N_COLS):
                        guess_letter = s[col]
                        word_letter = random_word[col]

                        if guess_letter.lower() == word_letter.lower():
                            correct_letter.append(col)
                        elif guess_letter.lower() in random_word.lower():
                            present_letter.append(col)
                        else:
                            missing_letter.append(col)

                    for col in correct_letter:
                        gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
                    for col in present_letter:
                        gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
                    for col in missing_letter:
                        gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)
                    gw.show_message("Try Again")
                gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Invalid word")

    gw.add_enter_listener(enter_action)
    

# Startup code

if __name__ == "__main__":
    wordle()