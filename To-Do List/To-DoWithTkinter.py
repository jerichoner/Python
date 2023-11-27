import tkinter as tk
from tkinter import messagebox
import json
import datetime
import os


class Task:
    def __init__(self, title, description, deadline, priority='Normal', completed=False):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.completed = completed

    def to_dict(self):
        return self.__dict__

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.file_path = os.path.join(os.path.dirname(__file__), 'tasks.json')
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)

    def save_tasks(self):
         with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    self.tasks.append(Task(**task_data))
        except FileNotFoundError:
            pass

class ToDoApp(tk.Tk):
    def __init__(self, todo_list):
        super().__init__()
        self.todo_list = todo_list
        self.title("To-Do List Application")
        self.geometry("500x400")

        self.task_frame = tk.Frame(self)
        self.task_frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(self.task_frame)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.task_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.populate_listbox()

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(fill=tk.X)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.remove_button = tk.Button(self.button_frame, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.complete_button = tk.Button(self.button_frame, text="Toggle Complete", command=self.toggle_complete)
        self.complete_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def check_deadlines(self):
        current_date = datetime.datetime.now()
        for task in self.todo_list.tasks:
            if not task.completed:
                task_deadline = datetime.datetime.strptime(task.deadline, '%Y-%m-%d')
                if task_deadline < current_date:
                    messagebox.showwarning("Deadline Passed", f"Task '{task.title}' has passed its deadline!")
                elif (task_deadline - current_date).days <= 2:  # for example, within 2 days
                    messagebox.showinfo("Deadline Approaching", f"Task '{task.title}' is approaching its deadline.")

    def populate_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            task_status = "[C]" if task.completed else "[ ]"
            self.listbox.insert(tk.END, f"{task_status} {task.title} - {task.description} (Deadline: {task.deadline}, Priority: {task.priority})")

    def add_task(self):
        new_task_window = tk.Toplevel(self)
        new_task_window.title("Add New Task")

        tk.Label(new_task_window, text="Title:").grid(row=0, column=0)
        title_entry = tk.Entry(new_task_window)
        title_entry.grid(row=0, column=1)

        tk.Label(new_task_window, text="Description:").grid(row=1, column=0)
        desc_entry = tk.Entry(new_task_window)
        desc_entry.grid(row=1, column=1)

        tk.Label(new_task_window, text="Deadline:").grid(row=2, column=0)
        deadline_entry = tk.Entry(new_task_window)
        deadline_entry.grid(row=2, column=1)

        tk.Label(new_task_window, text="Priority:").grid(row=3, column=0)
        priority_entry = tk.Entry(new_task_window)
        priority_entry.grid(row=3, column=1)

        add_button = tk.Button(new_task_window, text="Add",
                               command=lambda: self.create_task(title_entry.get(), desc_entry.get(), deadline_entry.get(), priority_entry.get(), new_task_window))
        add_button.grid(row=4, column=0, columnspan=2)

    def create_task(self, title, description, deadline, priority, window):
        try:
            # Validating and converting deadline
            datetime.datetime.strptime(deadline, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Invalid deadline format. Use YYYY-MM-DD.")
            return
        if title and description and deadline and priority:
            self.todo_list.add_task(Task(title, description, deadline, priority))
            self.populate_listbox()
            self.todo_list.save_tasks()
            window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required")

    def remove_task(self):
        try:
            selected_idx = self.listbox.curselection()[0]
            self.todo_list.tasks.pop(selected_idx)
            self.populate_listbox()
            self.todo_list.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove")

    def toggle_complete(self):
        try:
            selected_idx = self.listbox.curselection()[0]
            self.todo_list.tasks[selected_idx].completed = not self.todo_list.tasks[selected_idx].completed
            self.populate_listbox()
            self.todo_list.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to toggle completion")

def main():
    todo_list = ToDoList()
    app = ToDoApp(todo_list)
    app.after(60000, app.check_deadlines)  # Check deadlines every minute
    app.mainloop()

if __name__ == "__main__":
    main()
