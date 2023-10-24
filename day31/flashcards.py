from tkinter import *
import csv
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
all_words = []
current_card = {}
try:
    with open("data/words_to_learn.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            all_words.append(row)
except:
    with open("data/french_words.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            all_words.append(row)


print(all_words)


# --------------------------------- Button Functionality ---------------------------

def is_known():
    all_words.remove(current_card)
    print(len(all_words))
    data = pandas.DataFrame(all_words)
    data.to_csv("data/words_to_learn.csv")

    next_word()


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(all_words)
    french_word = current_card["French"]

    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(card_bg, image=flashcard_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=back_card_img)


# ---------------------------------- UI SET UP --------------------------------------
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
# flashcard area of the app
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=flashcard_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# right button
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=0, row=1)

# wrong button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong_button.grid(column=1, row=1)
next_word()

window.mainloop()

