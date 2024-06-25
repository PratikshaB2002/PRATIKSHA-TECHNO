import tkinter as tk

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0/5.0 + 32

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        unit = temperature_unit.get()

        if unit == 'F':
            result = fahrenheit_to_celsius(temperature)
            result_label.config(text=f"{temperature:.2f} Fahrenheit is equal to {result:.2f} Celsius.")
        elif unit == 'C':
            result = celsius_to_fahrenheit(temperature)
            result_label.config(text=f"{temperature:.2f} Celsius is equal to {result:.2f} Fahrenheit.")
        else:
            result_label.config(text="Invalid unit. Please enter 'F' or 'C'.")
    except ValueError:
        result_label.config(text="Invalid temperature. Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Styling
font_style = ("Arial", 14)
padding = 10

# Entry widget for temperature value
entry_temperature = tk.Entry(window, width=10, font=font_style, justify="center")
entry_temperature.grid(row=0, column=0, padx=padding, pady=padding, sticky="ew")

# Dropdown menu for temperature unit
temperature_unit = tk.StringVar(value='F')
unit_menu = tk.OptionMenu(window, temperature_unit, 'F', 'C')
unit_menu.config(font=font_style)
unit_menu.grid(row=0, column=1, padx=padding, pady=padding, sticky="ew")

# Button to perform conversion
convert_button = tk.Button(window, text="Convert", command=convert_temperature, font=font_style)
convert_button.grid(row=1, column=0, columnspan=2, pady=padding, sticky="ew")

# Label to display the result
result_label = tk.Label(window, text="", font=font_style)
result_label.grid(row=2, column=0, columnspan=2, pady=padding)

# Footer label
footer_label = tk.Label(window, text="Temperature Converter v1.0.0 DV by Karim", font=("Arial", 10), pady=padding, foreground="#555")
footer_label.grid(row=3, column=0, columnspan=2, pady=padding)

# Configure row and column weights for responsive resizing
for i in range(4):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Set uniform padding for all widgets
for child in window.winfo_children():
    child.grid_configure(padx=padding, pady=padding)

# Run the main loop
window.mainloop()
