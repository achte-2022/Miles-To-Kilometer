# Importing Libraries
import tkinter

# Constants
WINDOW_HEIGHT = 100
WINDOW_WIDTH = 100
WINDOW_PADDING = 20
FONT = ("Arial", 14)


def calculate_button_clicked():
    miles = float(miles_entry.get())
    km = miles * 1.609
    km_answer_label.config(text=str(km), font=FONT)
    return


# Object Setup
# Window
window = tkinter.Tk()
window.title("Miles to Km")
window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING)

# Entry-miles
miles_entry = tkinter.Entry(width=10)
miles_entry.grid(row=0, column=1)


# Label-miles
miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)


# Label-normal
normal_label = tkinter.Label(text="is equal to", font=FONT)
normal_label.grid(row=1, column=0)


# Label-km_answer
km_answer_label = tkinter.Label(text="0", width=10)
km_answer_label.grid(row=1, column=1)


# Label-km
km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)


# Button-calculate
calculate_button = tkinter.Button(text="Calculate", command=calculate_button_clicked)
calculate_button.grid(row=2, column=1)

window.mainloop()
