import random
import tkinter

from WordleDictionary import FIVE_LETTER_WORDS
from WordleDictionarySpanish import FIVE_LETTER_SPANISH_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Create window for language and color scheme selection
    selection_window = tkinter.Tk()
    selection_window.title("Wordle Settings")

    # Create label for language selection
    language_label = tkinter.Label(selection_window, text="Preferred language:")
    language_label.pack()

    # Create radio buttons for language selection
    var_language = tkinter.StringVar()
    var_language.set("English")  # Default selection
    english_radio = tkinter.Radiobutton(selection_window, text="English", variable=var_language, value="English")
    spanish_radio = tkinter.Radiobutton(selection_window, text="Spanish", variable=var_language, value="Spanish")
    english_radio.pack()
    spanish_radio.pack()

    # Create label for color scheme selection
    color_label = tkinter.Label(selection_window, text="Preferred color scheme:")
    color_label.pack()

    # Create radio buttons for color scheme selection
    var_color = tkinter.StringVar()
    var_color.set("Default")  # Default selection
    default_color_radio = tkinter.Radiobutton(selection_window, text="Normal", variable=var_color, value="Default")
    alternate_color_radio = tkinter.Radiobutton(selection_window, text="Color-blind", variable=var_color, value="Alternate")
    default_color_radio.pack()
    alternate_color_radio.pack()

    # Create button to start game
    start_button = tkinter.Button(selection_window, text="Start Game", command=lambda: start_game(var_language.get(), var_color.get(), selection_window))
    start_button.pack()

    selection_window.mainloop()

def start_game(selected_language, selected_color_scheme, selection_window):
    # Close the language selection window
    selection_window.destroy()

    gw = WordleGWindow()

    if selected_language == "Spanish":
        dictionary = FIVE_LETTER_SPANISH_WORDS
    else:
        dictionary = FIVE_LETTER_WORDS

    random_word = random.choice(dictionary)
    print("The word is " + random_word)

    # Keep track of which letters in the random word have been matched
    matched_indices = set()

    def enter_action(s):
        correct_color = CORRECT_COLOR
        present_color = PRESENT_COLOR
        missing_color = MISSING_COLOR

        if selected_color_scheme == "Alternate":
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
                    matched_indices.add(col)
                elif guess_letter.lower() in random_word.lower() and col not in matched_indices:
                    present_letter.append(col)
                    matched_indices.add(col)
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


