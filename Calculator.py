from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Arithmetic Operations")
window.geometry("350x250")

# Labels and Entries
Label(window, text="Input A").grid(column=0, row=0, padx=10, pady=5)
txt1 = Entry(window, width=15)
txt1.grid(column=1, row=0)

Label(window, text="Input B").grid(column=0, row=1, padx=10, pady=5)
txt2 = Entry(window, width=15)
txt2.grid(column=1, row=1)

Label(window, text="Result").grid(column=0, row=2, padx=10, pady=5)
txt3 = Entry(window, width=15)
txt3.grid(column=1, row=2)

# Helper function to get inputs safely
def get_values():
    try:
        a = float(txt1.get())
        b = float(txt2.get())
        return a, b
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
        return None, None

def clear_result():
    txt3.delete(0, END)

# Operations
def add():
    a, b = get_values()
    if a is not None:
        clear_result()
        txt3.insert(0, a + b)

def subtract():
    a, b = get_values()
    if a is not None:
        clear_result()
        txt3.insert(0, a - b)

def multiply():
    a, b = get_values()
    if a is not None:
        clear_result()
        txt3.insert(0, a * b)

def divide():
    a, b = get_values()
    if a is not None:
        if b == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
            return
        clear_result()
        txt3.insert(0, a / b)

# Buttons
Button(window, text="Add", width=10, command=add).grid(column=0, row=3, pady=10)
Button(window, text="Subtract", width=10, command=subtract).grid(column=1, row=3)

Button(window, text="Multiply", width=10, command=multiply).grid(column=0, row=4)
Button(window, text="Divide", width=10, command=divide).grid(column=1, row=4)

window.mainloop()
