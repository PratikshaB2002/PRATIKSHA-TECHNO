from tkinter import *

class CustomButton(Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

# Function to update the display
def button_click(value):
    current = str(entry.get())
    entry.delete(0, END)
    entry.insert(0, current + value)

# Function to perform calculations
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Function to clear the display
def clear():
    entry.delete(0, END)

# Create the main window
root = Tk()
root.resizable(False, False)
root.title("Simple Calculator")

# Create the display
entry = Entry(root, width=22, font=("Arial", 18), insertontime=0, bd=5, borderwidth=8, foreground="#ff0000", highlightthickness=3, highlightcolor="#f5d0d0", highlightbackground="#f5d0d0", justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, ipadx=11, ipady=8)

# Define button layout
button_layout = ["C", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", "0", ".", "="]

# Create buttons
for button in button_layout:
    if button == "C":
        Button(
            root,
            text=button,
            width=12,
            height=1,
            padx=68,
            pady=10,
            activebackground="#ff4d4d",
            bg="#6699ff",
            font=("20"),
            command=clear,
        ).grid(row=1, column=0, columnspan=3)
    elif button == "/":
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#ffe46b',
            bg="#d0c6f5",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=1, column=3)
    elif button == "7":
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#73f5d7',
            bg="#FFFFFF",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=2, column=0)
    elif button == "8":
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#73f5d7',
            bg="#FFFFFF",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=2, column=1)
    elif button == "9":
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#73f5d7',
            bg="#FFFFFF",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=2, column=2)
    elif button == "*":
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#ffe46b',
            bg="#d0c6f5",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=2, column=3)
    elif button == "4":
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#73f5d7',
            bg="#FFFFFF",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=3, column=0)
    elif button == "5":
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#73f5d7',
            bg="#FFFFFF",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=3, column=1)
    elif button == "6":
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#73f5d7',
            bg="#FFFFFF",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=3, column=2)
    elif button == "-":
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#ffe46b',
            bg="#d0c6f5",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=3, column=3)
    elif button == "1":
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#73f5d7',
            bg="#FFFFFF",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=4, column=0)
    elif button == "2":
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#73f5d7',
            bg="#FFFFFF",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=4, column=1)
    elif button == "3":
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#73f5d7',
            bg="#FFFFFF",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=4, column=2)
    elif button == "+":
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#ffe46b',
            bg="#d0c6f5",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=4, column=3)
    elif button == "0":
        Button(
            root,
            text=button,
            width=9,
            height=1,
            padx=39.4,
            pady=10,
            activebackground='#73f5d7',
            bg="#FFFFFF",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=5, column=0, columnspan=2)
    elif button == ".":
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#73f5d7',
            bg="#FFFFFF",
            font=("20"),
            command=lambda value=button: button_click(value),
        ).grid(row=5, column=2)
    else:
        Button(
            root,
            text=button,
            width=4,
            height=1,
            padx=20,
            pady=10,
            activebackground='#6dff6b',
            bg="#c6f5ea",
            font=("20"),
            command=calculate,
        ).grid(row=5, column=3)

# Run the application
root.mainloop()