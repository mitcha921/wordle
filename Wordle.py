# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
import tkinter 

from WordleDictionary import FIVE_LETTER_WORDS
from WordleDictionarySpanish import FIVE_LETTER_SPANISH_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Create window for language selection
    selection_window = tkinter.Tk()
    selection_window.title("Wordle Settings")

    # Create label for window
    label = tkinter.Label(selection_window, text="Select your game settings:")
    label.pack()

    # Create radio buttons 
    var = tkinter.StringVar()
    var.set("English")  # Default selection
    english_radio = tkinter.Radiobutton(selection_window, text="English", variable=var, value="English")
    spanish_radio = tkinter.Radiobutton(selection_window, text="Spanish", variable=var, value="Spanish")
    english_radio.pack()
    spanish_radio.pack()

    # Create button to start game
    start_button = tkinter.Button(selection_window, text="Start Game", command=lambda: start_game(var.get(), selection_window))
    start_button.pack()

    selection_window.mainloop()

def start_game(selected_language, selection_window):
    # Close the language selection window
    selection_window.destroy()

    gw = WordleGWindow()
    
    if selected_language == "Spanish":
        dictionary = FIVE_LETTER_SPANISH_WORDS
    else:
        dictionary = FIVE_LETTER_WORDS

    random_word = random.choice(dictionary)
    print("The word is " + random_word)

    def enter_action(s):
        correct_color = CORRECT_COLOR
        present_color = PRESENT_COLOR
        missing_color = MISSING_COLOR

        is_alternate_color_scheme = True  # must change manually for now

        if is_alternate_color_scheme:
            correct_color = "#85BFF9"
            present_color = "#F5793A"

        if s.strip().lower() == "":
            # If the input string is empty or contains only whitespace, do nothing
            return

        if s.lower() in dictionary:
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
                gw.set_square_color(gw.get_current_row(), col, correct_color)
            for col in present_letter:
                gw.set_square_color(gw.get_current_row(), col, present_color)
            for col in missing_letter:
                gw.set_square_color(gw.get_current_row(), col, missing_color)
            if s.lower() == random_word.lower():
                gw.show_message("You win! The word is " + s)
                gw.set_current_row(7)
            else:
                if gw.get_current_row() > 4:
                    gw.show_message("Game over. The correct word was \"" + random_word + "\"")
                else:
                    gw.show_message("Try Again")
                gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Invalid word")

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()
