from tkinter import *
import pandas
import random
data = pandas.read_csv("french_words.csv")
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "French"
LANG_FONT = ("Ariel", 40, "italic")

WORD_FONT = ("Ariel", 60, "bold")


window = Tk()
window.title("Flash Cards")
window.minsize(width=1000, height=800)
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

def new_card():
    french_word = random.choice(data.French)
    # english_word = data[data.French == french_word]
    # anglais = english_word.English
    # english_word = data[data.French == french_word]


canvas1 = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="card_front.png")
canvas1.create_image(450, 300, image=front_card_img)
canvas1.grid(column=0, row=0, columnspan=2)
canvas1.create_text(450, 200, text=LANGUAGE, font=LANG_FONT)
canvas1.create_text(450, 300, font=WORD_FONT)


wrong_button_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, bd=0, command=new_card)
wrong_button.grid(column=0, row=2)

right_button_image = PhotoImage(file="right.png")
right_button = Button(image=right_button_image, highlightthickness=0, bd=0, command=new_card)
right_button.grid(column=1, row=2)

window.mainloop()