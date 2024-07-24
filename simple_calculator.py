from tkinter import *

# Function to handle button click
def button_click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(value))

# Function to clear the entry
def clear_entry():
    entry.delete(0, END)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")

root = Tk()
root.title("good")
root.geometry("300x400")
root.config(bg="lightblue")

entry = Entry(root, width=28, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

clear_button = Button(root, text="C", padx=20, pady=20, bg="red", command=clear_entry)
clear_button.grid(row=0, column=3, padx=10, pady=10)

# List of button values
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0

# Create buttons and place them in the grid
for button in buttons:
    if button == "=":
        btn = Button(root, text=button, padx=20, pady=20, bg="green", command=evaluate_expression)
    else:
        btn = Button(root, text=button, padx=20, pady=20, bg="green", command=lambda b=button: button_click(b))
    btn.grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
