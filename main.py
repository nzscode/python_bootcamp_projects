from tkinter import *
import pandas
import random
data = pandas.read_csv("french_words.csv")
fr_eng_dict = data.to_dict(orient="records")
print(fr_eng_dict)
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "French"
LANG_FONT = ("Ariel", 40, "italic")

WORD_FONT = ("Ariel", 60, "bold")


window = Tk()
window.title("Flash Cards")
window.minsize(width=1000, height=800)
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

chosen_word = ""
def new_card():
    rand_dict = random.choice(fr_eng_dict)
    rand_dict_fr_word = rand_dict["French"]
    rand_dict_en_word = rand_dict["English"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=rand_dict_fr_word)

def card_flip():





window.after(3000, card_flip)
canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="card_front.png")
canvas.create_image(450, 300, image=front_card_img)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(450, 200, text="", font=LANG_FONT)
card_word = canvas.create_text(450, 300, text="", font=WORD_FONT)


wrong_button_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, bd=0, command=new_card)
wrong_button.grid(column=0, row=2)

right_button_image = PhotoImage(file="right.png")
right_button = Button(image=right_button_image, highlightthickness=0, bd=0, command=new_card)
right_button.grid(column=1, row=2)

new_card()
window.mainloop()