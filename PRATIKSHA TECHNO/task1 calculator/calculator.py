import tkinter as tk

#Task 1 : Calculator
"""
Create a basic calculator that can perform
basic arithmetic operations such as addition,
subtraction, multiplication, and division.using
functions
"""


def on_click(button_value):
    current = entry.get()

    if button_value == '=':
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_value == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, str(button_value))


# Create the main window
window = tk.Tk()
window.title("Stylish Calculator")

# Entry widget for input and display
entry = tk.Entry(window, width=20, font=("Arial", 20), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Define buttons with enhanced styling
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Add buttons with enhanced styling
for (text, row, col) in buttons:
    button = tk.Button(window, text=text, padx=20, pady=20, font=("Arial", 16), command=lambda t=text: on_click(t))
    button.grid(row=row, column=col, sticky="nsew")

# Configure row and column weights for responsive resizing
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Set uniform padding for all widgets
for child in window.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Footer
footer_label = tk.Label(window, text="Calculator v1.0.0 DV by Karim", font=("Arial", 10) ,foreground="#000", pady=10)
footer_label.grid(row=5, column=0, columnspan=4)

# Run the main loop
window.mainloop()
