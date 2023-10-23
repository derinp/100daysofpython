from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("passwords.json") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No data file found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            pyperclip.copy(password)
            messagebox.showinfo(title=website, message=f"Username: {email}\n"
                                                       f"Password: {password}\n"
                                                       f"The password has been copied to your clipboard")

        else:
            messagebox.showinfo(title="Error", message=f"No details for {website}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, "end")
    letters = string.ascii_letters + string.digits + string.punctuation
    random_pass = ''.join(random.choice(letters) for i in range(random.randint(13, 17)))
    password_entry.insert(0, string=random_pass)
    pyperclip.copy(random_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_entry_info():
    # store text in the entry fields to a variable.
    website_entry_text = website_entry.get()
    user_name_text = username_entry.get()
    password_entry_text = password_entry.get()
    new_data = {
        website_entry_text: {
            "email": user_name_text,
            "password": password_entry_text
        }
    }

    if len(website_entry_text) == 0 or len(user_name_text) == 0 or len(password_entry_text) == 0:
        messagebox.showinfo(title="Empty Fields", message="There are some empty fields, unable to save.")
    else:
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)

        website_entry.delete(0, "end")
        username_entry.delete(0, "end")
        password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=0, row=0, columnspan=2)

# website row
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=24)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")

search_button = Button(text="Search", width=8, command=find_password)
search_button.grid(column=1, row=1, sticky="e")

# username/email row
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_entry = Entry(width=36)
username_entry.insert(0, "derinperez@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2, sticky="w")

# password row
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3, sticky="w", padx=(0, 84))

password_gen_button = Button(text="Generate", width=10, command=generate_password)
password_gen_button.grid(column=1, row=3, sticky="e")

# add button row
add_button = Button(text="Add password", width=30, command=get_entry_info)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
