from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, "end")
    letters = string.ascii_letters + string.digits + string.punctuation
    random_pass = ''.join(random.choice(letters) for i in range(random.randint(13, 17)))
    password_entry.insert(0, string=random_pass)
    pyperclip.copy(random_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_entry_info():
    # store text in the entry fields to a varialble.
    website_entry_text = website_entry.get()
    user_name_text = username_entry.get()
    password_entry_text = password_entry.get()

    if len(website_entry_text) == 0 or len(user_name_text) == 0 or len(password_entry_text) == 0:
        messagebox.showinfo(title="Empty Fields", message="There are some empty fields, unable to save.")
    else:
        is_ok = messagebox.askokcancel(title=website_entry_text, message=f"Confirm.\n"
                                                                         f"Website: {website_entry_text}\n"
                                                                         f"Username: {user_name_text}\n"
                                                                         f"Password: {password_entry_text}"
                                                                         f"is this ok to save?")
        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"{website_entry_text} | {user_name_text} | {password_entry_text}\n")

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

website_entry = Entry(width=36)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")

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

