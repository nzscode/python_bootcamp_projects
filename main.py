from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=230)
my_pass_image = PhotoImage(file="logo.png")
canvas.create_image(125, 100, image=my_pass_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

website_input = Entry(width=57)
website_input.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

email_input = Entry(width=57)
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

password_input = Entry(width=20)
password_input.grid(row=3, column=1, sticky=W, padx=2)

password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2, sticky=E)

add_button = Button(text="Add", width=48)
add_button.grid(row=4, column=1, columnspan=2)






window.mainloop()