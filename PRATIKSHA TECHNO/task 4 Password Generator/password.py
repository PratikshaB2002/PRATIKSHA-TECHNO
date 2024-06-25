import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip
#dv by karim
class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        # Styling
        font_style = ("Arial", 12)
        padding = 10

        # Label and Entry for password length
        self.length_label = tk.Label(self.master, text="Password Length:", font=font_style)
        self.length_label.grid(row=0, column=0, padx=padding, pady=padding, sticky="w")

        self.length_entry = ttk.Combobox(self.master, values=[8, 10, 12, 16, 20], font=font_style, state="readonly")
        self.length_entry.set(12)  # Default value
        self.length_entry.grid(row=0, column=1, padx=padding, pady=padding, sticky="ew")

        # Label and Combobox for password complexity
        self.complexity_label = tk.Label(self.master, text="Password Complexity:", font=font_style)
        self.complexity_label.grid(row=1, column=0, padx=padding, pady=padding, sticky="w")

        self.complexity_combobox = ttk.Combobox(self.master, values=["Low", "Medium", "High"], font=font_style,
                                                state="readonly")
        self.complexity_combobox.set("Medium")  # Default value
        self.complexity_combobox.grid(row=1, column=1, padx=padding, pady=padding, sticky="ew")

        # Button to generate password
        self.generate_button = tk.Button(self.master, text="Generate Password", command=self.generate_password,
                                         font=font_style)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=padding, sticky="ew")

        # Label to display generated password
        self.password_label = tk.Label(self.master, text="", font=font_style)
        self.password_label.grid(row=3, column=0, columnspan=2, pady=padding, sticky="ew")

        # Button to copy password to clipboard
        self.copy_button = tk.Button(self.master, text="Copy to Clipboard", command=self.copy_to_clipboard,
                                     font=font_style)
        self.copy_button.grid(row=4, column=0, columnspan=2, pady=padding, sticky="ew")

        # Footer label
        footer_label = tk.Label(self.master, text="Password Generator v1.1.0 DV by Karim", font=("Arial", 10),
                                pady=padding, foreground="#555")
        footer_label.grid(row=5, column=0, columnspan=2, pady=padding)

        # Configure row and column weights for responsive resizing
        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

        # Set uniform padding for all widgets
        for child in self.master.winfo_children():
            child.grid_configure(padx=padding, pady=padding)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            complexity = self.complexity_combobox.get().lower()

            if complexity == "low":
                characters = string.ascii_letters + string.digits
            elif complexity == "medium":
                characters = string.ascii_letters + string.digits + string.punctuation
            elif complexity == "high":
                characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper() + string.punctuation

            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid password length.")

    def copy_to_clipboard(self):
        password = self.password_label.cget("text").split(": ")[1]
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Your Password copied !")


if __name__ == "__main__":
    root = tk.Tk()
    password_app = PasswordGeneratorApp(root)
    root.mainloop()
