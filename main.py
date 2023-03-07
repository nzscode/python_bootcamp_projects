from tkinter import *
import pandas
import random
data = pandas.read_csv("french_words.csv")
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "French"
LANG_FONT = ("Ariel", 40, "italic")

FRENCH_WORD = random.choice(data.French)
english_word = data[data.French == FRENCH_WORD]
anglais = english_word.English
ENGLISH_WORD = data[data.French == FRENCH_WORD]
WORD_FONT = ("Ariel", 60, "bold")


window = Tk()
window.title("Flash Cards")
window.minsize(width=1000, height=800)
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas1 = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="card_front.png")
canvas1.create_image(450, 300, image=front_card_img)
canvas1.create_text(450, 200, text=LANGUAGE, font=LANG_FONT)
canvas1.create_text(450, 300, text=FRENCH_WORD, font=WORD_FONT)
canvas1.grid(column=0, row=0, columnspan=2)
#
# lang_label = Label(text=LANGUAGE, font=LANG_FONT)
# lang_label.config(pady=30)
# lang_label.grid(column=1, row=0)
#
# word_label = Label(text=FRENCH_WORD, font=WORD_FONT)
# word_label.grid(column=1, row=1)


def card_flip():
    canvas2 = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
    back_card_img = PhotoImage(file="card_back.png")
    canvas2.create_image(450, 300, image=back_card_img)
    canvas2.create_text(450, 200, text="English", font=LANG_FONT)
    canvas2.create_text(450, 300, text=anglais, font=WORD_FONT)

wrong_button_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0)
wrong_button.grid(column=0, row=2)


# flip_button = Button(text="Flip", command=card_flip)
# flip_button.grid(column=1, row=2)

right_button_image = PhotoImage(file="right.png")
right_button = Button(image=right_button_image, highlightthickness=0)
right_button.grid(column=1, row=2)

window.mainloop()