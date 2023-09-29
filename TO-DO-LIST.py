import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Set window dimensions (width x height)
        window_width = 400
        window_height = 400
        self.root.geometry(f"{window_width}x{window_height}")

        self.task_number = 1  # Initialize task numbering

        # Create and set up widgets
        self.label = tk.Label(root, text="To-Do List", font=("Helvetica", 16, "bold"), bg="lightblue", padx=10, pady=5)
        self.label.pack(fill=tk.X)

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=30)
        self.task_listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

        self.completed_listbox = tk.Listbox(root, width=30)
        self.completed_listbox.pack(pady=10)

        self.show_completed_button = tk.Button(root, text="Show Completed Tasks", command=self.show_completed_tasks)
        self.show_completed_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            task_with_number = f"{self.task_number}. {task}"
            self.task_listbox.insert(tk.END, task_with_number)
            self.task_entry.delete(0, tk.END)
            self.task_number += 1
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            completed_task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.completed_listbox.insert(tk.END, completed_task)
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def show_completed_tasks(self):
        completed_tasks = self.completed_listbox.get(0, tk.END)
        if completed_tasks:
            messagebox.showinfo("Completed Tasks", "\n".join(completed_tasks))
        else:
            messagebox.showinfo("Completed Tasks", "No tasks have been completed yet.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
