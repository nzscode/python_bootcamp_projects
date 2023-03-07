from tkinter import *

window = Tk()

window.title("Recipe Maker.")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

recipe_name_label = Label(text="Recipe Name: ")
recipe_name_label.grid(column=0, row=0, pady=10)

recipe_name_entry = Entry()
# recipe_name_entry.insert(END, "Enter recipe name here.")
recipe_name_entry.grid(column=1, row=0, columnspan=3)

ingredient_label = Label(text="Ingredient")
ingredient_label.grid(column=0, row=1, pady=10)

measure_label = Label(text="measure")
measure_label.grid(column=1, row=1)

quantity_label = Label(text="quantity")
quantity_label.grid(column=2, row=1)

add_ingredient_button = Button(text= "+")
add_ingredient_button.grid(column=3, row=1)

remove_ingredient_button = Button(text="-")
remove_ingredient_button.grid(column=4, row=1)









window.mainloop()
