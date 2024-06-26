from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ----- Password Generator ----- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    new_letters = [choice(letters) for _ in range(randint(8, 10))]
    new_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    new_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = new_letters + new_numbers + new_symbols
    shuffle(password_list)

    new_password = "".join(password_list)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)

# ----- Save Password ----- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please fill in all fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("Password_Maker_Saver/data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ----- UI Setup ----- #
main_window = Tk()
main_window.title("Password Manager")
main_window.config(padx=20, pady=20)

image_canvas = Canvas(width=200, height=200)
my_pass_image = PhotoImage(file="logo.png")
image_canvas.create_image(125, 100, image=my_pass_image)
image_canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

website_entry = Entry(width=58)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

email_entry = Entry(width=58)
email_entry.grid(row=2, column=1, columnspan=2)

email_entry.insert(END, "noorfr@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky=W)



# website = {
#     "website": [],
#     "email": [],
#     "password": []
# }

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky=E)

add_button = Button(text="Add", width=49, command=save)
add_button.grid(row=4, column=1, columnspan=2)









main_window.mainloop()