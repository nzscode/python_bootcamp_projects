from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
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
    website = website_entry.get().title()
    email = email_entry.get().lower()
    password = password_entry.get()
    new_data_dict = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please fill in all fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data_dict)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data_dict, data_file, indent=4)

        else:
            data.update(new_data_dict)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = (website_entry.get()).title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")




# ----- UI Setup ----- #
main_window = Tk()
main_window.title("Password Manager")
main_window.config(padx=20, pady=20, bg="#FFFFFF")

image_canvas = Canvas(width=200, height=200, bg="#FFFFFF", highlightthickness=0)
my_pass_image = PhotoImage(file="Password_Maker_Saver/logo.png")
image_canvas.create_image(125, 100, image=my_pass_image)
image_canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", bg="#FFFFFF")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky=W)
website_entry.focus()

search = Button(text="Search", width=15, bg="#FFFFFF", command=find_password)
search.grid(row=1, column=2, sticky=E, pady=5)

email_label = Label(text="Email/Username: ", bg="#FFFFFF")
email_label.grid(row=2, column=0)

email_entry = Entry(width=58)
email_entry.grid(row=2, column=1, sticky=W, columnspan=2, pady=5)
email_entry.insert(END, "noorfr@gmail.com")

password_label = Label(text="Password: ", bg="#FFFFFF")
password_label.grid(row=3, column=0)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky=W, pady=5)

# website = {
#     "website": [],
#     "email": [],
#     "password": []
# }

password_button = Button(text="Generate Password", command=generate_password, width=15, bg="#FFFFFF")
password_button.grid(row=3, column=2, sticky=E)

add_button = Button(text="Add", width=49, command=save, bg="#FFFFFF")
add_button.grid(row=4, column=1, columnspan=2, pady=5)

main_window.mainloop()