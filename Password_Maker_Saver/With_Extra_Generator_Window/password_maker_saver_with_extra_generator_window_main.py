import random
from tkinter import *
from random import choice, randint, shuffle

gen_window = Tk()
gen_window.title = "Password Parameters"
gen_window.config(padx=20, pady=20)

primary_label = Label(text="Password Generator")
primary_label.grid(row=0, column=0, columnspan=2)

password_label = Label(relief="sunken", width=25, height=3)
password_label.config(text="Password will show here.")
password_label.grid(row=1, column=0, columnspan=2)


password_length_slider = Scale(from_=8, to=20, orient="horizontal")
password_length_slider.grid(row=3, column=0, columnspan=2)


var1 = IntVar()
uppercase_checkbox = Checkbutton(text="Use A-Z", onvalue=1, offvalue=0, variable=var1)
uppercase_checkbox.grid(row=4,  column=0, columnspan=2)
var2 = IntVar()
lowercase_checkbox = Checkbutton(text="Use a-z", onvalue=1, offvalue=0, variable=var2)
lowercase_checkbox.grid(row=5,  column=0, columnspan=2)
var3 = IntVar()
numbers_checkbox = Checkbutton(text="Use 0-9", onvalue=1, offvalue=0, variable=var3)
numbers_checkbox.grid(row=6,  column=0, columnspan=2)
var4 = IntVar()
symbols_checkbox = Checkbutton(text="Use !@#$%^&*", onvalue=1, offvalue=0, variable=var4)
symbols_checkbox.grid(row=7,  column=0, columnspan=2)

# number_quantity_label = Label(text="How many numbers: ")
# number_quantity_label.grid(row=8, column=0)
# number_quantity_spinbox = Spinbox(from_=0, to=5, width=5)
# number_quantity_spinbox.grid(row=8, column=1)
#
# symbol_quantity_label = Label(text="How many symbols: ")
# symbol_quantity_label.grid(row=9, column=0)
# symbol_quantity_spinbox = Spinbox(from_=0, to=5, width=5)
# symbol_quantity_spinbox.grid(row=9, column=1)
password_length = int(password_length_slider.get())
def generate_password():

    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                         'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                         'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_selection = []

    if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0):
        for char in uppercase_letters:
            password_selection.append(char)
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) & (var4.get() == 0):
        for char in lowercase_letters:
            password_selection.append(char)
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) & (var4.get() == 0):
        for char in numbers:
            password_selection.append(char)
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 1):
        for char in symbols:
            password_selection.append(char)
    elif (var1.get() == 1) & (var2.get() == 1) & (var3.get() == 0) & (var4.get() == 0):
        for char in uppercase_letters:
            password_selection.append(char)
        for char in lowercase_letters:
            password_selection.append(char)
    elif (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 1) & (var4.get() == 0):
        for char in uppercase_letters:
            password_selection.append(char)
        for char in numbers:
            password_selection.append(char)
    elif (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 1):
        for char in uppercase_letters:
            password_selection.append(char)
        for char in symbols:
            password_selection.append(char)
    elif (var1.get() == 1) & (var2.get() == 1) & (var3.get() == 1) & (var4.get() == 0):
        for char in uppercase_letters:
            password_selection.append(char)
        for char in lowercase_letters:
            password_selection.append(char)
        for char in numbers:
            password_selection.append(char)
    elif (var1.get() == 1) & (var2.get() == 1) & (var3.get() == 1) & (var4.get() == 1):
        for char in uppercase_letters:
            password_selection.append(char)
        for char in lowercase_letters:
            password_selection.append(char)
        for char in numbers:
            password_selection.append(char)
        for char in symbols:
            password_selection.append(char)
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 1) & (var4.get() == 0):
        for char in lowercase_letters:
            password_selection.append(char)
        for char in numbers:
            password_selection.append(char)
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) & (var4.get() == 1):
        for char in lowercase_letters:
            password_selection.append(char)
        for char in symbols:
            password_selection.append(char)
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) & (var4.get() == 1):
        for char in numbers:
            password_selection.append(char)
        for char in symbols:
            password_selection.append(char)

    new_password = []
    for _ in range(int(password_length_slider.get())):
        rand_char = random.choice(password_selection)
        new_password.append(rand_char)

    shuffle(new_password)
    final_password = "".join(new_password)
    password_label.config(text=final_password)

    print(password_selection)

    # shuffle(password_list)
    #
    # new_password = "".join(password_list)
    # password_label.config(text=new_password)

generate_button = Button(text="Generate", width=25, command=generate_password)
generate_button.grid(row=10, column=0, columnspan=2)


gen_window.mainloop()