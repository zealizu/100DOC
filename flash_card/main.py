BACKGROUND_COLOR = "#B1DDC6"  # Set the background color for the app

from tkinter import *
from tkinter import messagebox
import pandas
import random

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")  # Set the window title
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Set padding and background color

# ---------------------------- DATA LOADING ------------------------------- #
try: 
    # Try to load the words the user still needs to learn
    data = pandas.read_csv("100DOC/flash_card/data/words_to_learn.csv")
except FileNotFoundError:
    # If not found, load the original French words file
    data = pandas.read_csv("100DOC/flash_card/data/french_words.csv")
data_dict = data.to_dict(orient="records")  # Convert data to a list of dictionaries
random_dict = random.choice(data_dict)  # Pick a random word to start

# Load card images
card_front_img = PhotoImage(file="100DOC/flash_card/images/card_front.png")
card_back_img = PhotoImage(file="100DOC/flash_card/images/card_back.png")

# ---------------------------- BUTTON FUNCTIONS ------------------------------- #
def wrong_pressed():
    """
    Called when the user clicks the 'wrong' button.
    Picks a new random word and updates the card.
    """
    global random_dict
    random_dict = random.choice(data_dict)
    handle_change()

def right_pressed():
    """
    Called when the user clicks the 'right' button.
    Removes the current word from the list, saves progress, and shows a new word.
    If all words are learned, shows a congratulatory message.
    """
    global random_dict
    try:
        data_dict.remove(random_dict)  # Remove the known word
        data_dataframe = pandas.DataFrame(data_dict)
        data_dataframe.to_csv("100DOC/flash_card/data/words_to_learn.csv", index=False)  # Save progress
        random_dict = random.choice(data_dict)  # Pick a new word
        handle_change()
    except ValueError:
        # If there are no more words left
        messagebox.showinfo("congratulations", "You have completed all the words, Delete words_to_learn.csv if you want to start again")

def handle_change():
    """
    Updates the card to show the next French word and resets the flip timer.
    """
    global random_dict, flip
    canvas.itemconfig(lang, text=list(random_dict.keys())[0], fill="black")  # Set language label (e.g., 'French')
    canvas.itemconfig(word, text=random_dict["French"], fill="black")  # Set the French word
    canvas.itemconfig(card, image=card_front_img)  # Show the front of the card
    flip = window.after(3000, flip_card)  # Schedule the card to flip after 3 seconds

def flip_card():
    """
    Flips the card to show the English translation after a delay.
    """
    canvas.itemconfig(card, image=card_back_img)  # Show the back of the card
    canvas.itemconfig(lang, fill="white", text=list(random_dict.keys())[1])  # Set language label to 'English'
    canvas.itemconfig(word, fill="white", text=random_dict["English"])  # Show the English translation
    window.after_cancel(flip)  # Cancel any scheduled flips

# ---------------------------- CANVAS SETUP ------------------------------- #
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card = canvas.create_image(400, 270, image=card_front_img)  # Card image
lang = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))  # Language label (French/English)
word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))  # Word to display
canvas.grid(row=0, column=0, columnspan=2)

handle_change()  # Show the first card
flip = window.after(3000, flip_card)  # Schedule the first flip

# ---------------------------- BUTTONS ------------------------------- #
wrong_img = PhotoImage(file="100DOC/flash_card/images/wrong.png")
right_img = PhotoImage(file="100DOC/flash_card/images/right.png")

# Wrong button: user doesn't know the word
wrong_btn = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, relief="flat", command=wrong_pressed)
wrong_btn.grid(row=1, column=0)

# Right button: user knows the word
right_btn = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, relief="flat", command=right_pressed)
right_btn.grid(row=1, column=1)

window.mainloop()  # Start the Tkinter event loop