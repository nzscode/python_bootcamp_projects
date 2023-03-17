from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "French"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
to_learn = {}

try:
    data = pandas.read_csv("Flash_Cards/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Flash_Cards/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

window = Tk()
window.title("Flash Cards")
window.minsize(width=1000, height=800)
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

current_card = {}
def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    rand_dict_fr_word = current_card["French"]
    canvas.itemconfig(card_image, image=front_card_img)
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_word, text=rand_dict_fr_word, fill="Black")
    flip_timer = window.after(3000, card_flip)


def card_flip():
    canvas.itemconfig(card_title, text="English", fill="white")
    rand_dict_en_word = current_card["English"]
    canvas.itemconfig(card_word, text=rand_dict_en_word)
    canvas.itemconfig(card_image, image=back_card_img)
    canvas.itemconfig(card_word, fill="white")

def is_known():
    to_learn.remove(current_card)
    datax = pandas.DataFrame(to_learn)
    datax.to_csv("Flash_Cards/words_to_learn.csv")
    new_card()


flip_timer = window.after(3000, card_flip)
canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="Flash_Cards/images/card_front.png")
back_card_img = PhotoImage(file="Flash_Cards/images/card_back.png")
card_image = canvas.create_image(450, 300)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(450, 200, text="", font=LANG_FONT)
card_word = canvas.create_text(450, 300, text="", font=WORD_FONT)

wrong_button_image = PhotoImage(file="Flash_Cards/images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, bd=0, command=new_card)
wrong_button.grid(column=0, row=2)

right_button_image = PhotoImage(file="Flash_Cards/images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, bd=0, command=is_known)
right_button.grid(column=1, row=2)


new_card()
window.mainloop()



