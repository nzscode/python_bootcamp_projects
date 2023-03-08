from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "French"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# data = pandas.read_csv("french_words.csv")
data = pandas.read_csv("tests.csv")
fr_eng_dict = data.to_dict(orient="records")

window = Tk()
window.title("Flash Cards")
window.minsize(width=1000, height=800)
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

rand_dict = {}
def new_card():
    global rand_dict, flip_timer
    window.after_cancel(flip_timer)
    rand_dict = random.choice(fr_eng_dict)
    rand_dict_fr_word = rand_dict["French"]
    canvas.itemconfig(card_image, image=front_card_img)
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_word, text=rand_dict_fr_word, fill="Black")
    flip_timer = window.after(3000, card_flip)



def card_flip():
    canvas.itemconfig(card_title, text="English", fill="white")
    rand_dict_en_word = rand_dict["English"]
    canvas.itemconfig(card_word, text=rand_dict_en_word)
    canvas.itemconfig(card_image, image=back_card_img)
    canvas.itemconfig(card_word, fill="white")

def remove_from_dict():
    global fr_eng_dict
    new_dict = fr_eng_dict.remove(rand_dict)
    to_learn = pandas.DataFrame(new_dict)
    to_learn.to_csv("words_To_Learn.csv")
    print(fr_eng_dict)

flip_timer = window.after(3000, card_flip)
canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="card_front.png")
back_card_img = PhotoImage(file="card_back.png")
card_image = canvas.create_image(450, 300)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(450, 200, text="", font=LANG_FONT)
card_word = canvas.create_text(450, 300, text="", font=WORD_FONT)

wrong_button_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, bd=0, command=new_card)
wrong_button.grid(column=0, row=2)

right_button_image = PhotoImage(file="right.png")
right_button = Button(image=right_button_image, highlightthickness=0, bd=0,
                      command=lambda: [new_card(), remove_from_dict()])
right_button.grid(column=1, row=2)


new_card()
window.mainloop()



