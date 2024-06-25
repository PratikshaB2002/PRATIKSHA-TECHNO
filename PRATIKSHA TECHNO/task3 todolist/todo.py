import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        # Styling
        font_style = ("Arial", 14)
        button_style = ("Arial", 12)
        padding = 10

        # Entry for adding new task
        self.task_entry = tk.Entry(self.master, width=30, font=font_style)
        self.task_entry.grid(row=0, column=0, padx=padding, pady=padding, sticky="ew")

        # Button to add new task
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task, font=button_style)
        self.add_button.grid(row=0, column=1, padx=padding, pady=padding, sticky="ew")

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.master, height=10, width=40, font=font_style, selectbackground="#a6a6a6")
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=padding, pady=padding, sticky="ew")

        # Button to mark task as complete
        self.complete_button = tk.Button(self.master, text="Mark Complete", command=self.mark_complete, font=button_style)
        self.complete_button.grid(row=2, column=0, padx=padding, pady=padding, sticky="ew")

        # Button to view current to-do list
        self.view_button = tk.Button(self.master, text="View To-Do List", command=self.view_list, font=button_style)
        self.view_button.grid(row=2, column=1, padx=padding, pady=padding, sticky="ew")

        # Footer label
        footer_label = tk.Label(self.master, text="To-Do List App v1.0.0 DV by Karim", font=("Arial", 10), pady=padding, foreground="#555")
        footer_label.grid(row=3, column=0, columnspan=2, pady=padding)

        # Configure row and column weights for responsive resizing
        for i in range(4):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

        # Set uniform padding for all widgets
        for child in self.master.winfo_children():
            child.grid_configure(padx=padding, pady=padding)

    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            completed_task = self.tasks.pop(selected_task_index)
            messagebox.showinfo("Task Completed", f"Task '{completed_task}' marked as complete.")
            self.update_task_list()

    def view_list(self):
        if self.tasks:
            task_list = "\n".join(self.tasks)
            messagebox.showinfo("To-Do List", f"Current To-Do List:\n{task_list}")
        else:
            messagebox.showinfo("To-Do List", "Your to-do list is empty.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoListApp(root)
    root.mainloop()
