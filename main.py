from tkinter import *
window = Tk()

window.title("Test 1")
window.minsize(300, 100)

##Label
my_label = Label(text="Result will go here.", font=("Courier", 18, "bold"))
my_label.pack()

## Entry
us_label1 = Label(text="Please enter the 1st number below:")
us_label1.pack()
us_input1 = Entry()
us_input1.pack()

us_label2 = Label(text="Please enter the 2nd number below:")
us_label2.pack()
us_input2 = Entry()
us_input2.pack()

def calculate():
    user_input1 = us_input1.get()
    user_input2 = us_input2.get()
    print(radio_state)
    if radio_state.get() == 1:
        result = int(user_input1) + int(user_input2)
        my_label.config(text=result)
    elif radio_state.get() == 2:
        result = int(user_input1) - int(user_input2)
        my_label.config(text=result)
    elif radio_state.get() == 3:
        result = int(user_input1) * int(user_input2)
        my_label.config(text=result)
    else:
        result = int(user_input1) / int(user_input2)
        my_label.config(text=result)


radio_state = IntVar()
radiobutton_add = Radiobutton(text="+ or add", value=1, variable=radio_state, command=calculate)
radiobutton_add.pack()
radiobutton_minus = Radiobutton(text="- or subtract", value=2, variable=radio_state, command=calculate)
radiobutton_minus.pack()
radiobutton_multiply = Radiobutton(text="* or multiply", value=3, variable=radio_state, command=calculate)
radiobutton_multiply.pack()
radiobutton_divide = Radiobutton(text="/ or divide", value=4, variable=radio_state, command=calculate)
radiobutton_divide.pack()



window.mainloop()
