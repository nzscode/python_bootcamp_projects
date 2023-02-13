from tkinter import *
window = Tk()

window.title("Test 1")
window.minsize(300, 100)

##Label
my_label = Label(text="I am a label.", font=("Courier", 20, "bold"))
my_label.pack()

my_label["text"] = "Hello, I am Labello."
my_label.config(text="Hello, I'm Larabel.")

##Button


def button_clicked():
    my_label.config(text="Button got clicked.")


button = Button(text="Click Me", command=button_clicked)
button.pack()

## Entry
input = Entry()
input.pack()


def Print_Response():
    user_input = input.get()
    my_label.config(text=user_input)


print_response_button = Button(text="Print", command=Print_Response)
print_response_button.pack()

def calculate():
    user_input = input.get()
    result = int(user_input) + 5
    my_label.config(text=result)


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.pack()





window.mainloop()
