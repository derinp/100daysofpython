from tkinter import *

# set up window
window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=250, height=150)
window.config(padx=50, pady=40)


def calculate_km():
    miles = int(user_enter.get())
    km = miles * 1.609
    km_calculated_label.config(text=km)


# input user value
user_enter = Entry(width=7)
user_enter.grid(column=1, row=0)

# all labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_calculated_label = Label(text=0)
km_calculated_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)

window.mainloop()

