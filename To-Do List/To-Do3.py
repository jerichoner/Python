import json
import os

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline

    def __str__(self):
        return f"'{self.title}' - {self.description} (Deadline: {self.deadline})"

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description, deadline):
        self.tasks.append(Task(title, description, deadline))
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
            return
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def edit_task(self, index, title=None, description=None, deadline=None):
        if 1 <= index <= len(self.tasks):
            if title:
                self.tasks[index-1].title = title
            if description:
                self.tasks[index-1].description = description
            if deadline:
                self.tasks[index-1].deadline = deadline
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index-1]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    self.tasks.append(Task(**task_data))

def main():
    todo_list = ToDoList()

    while True:
        print("\nTodo List - Choose an action:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            deadline = input("Enter task deadline: ")
            todo_list.add_task(title, description, deadline)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to edit: "))
            title = input("Enter new title (leave blank for no change): ")
            description = input("Enter new description (leave blank for no change): ")
            deadline = input("Enter new deadline (leave blank for no change): ")
            todo_list.edit_task(index, title, description, deadline)
        elif choice == '4':
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.save_tasks()
            print("Tasks saved. Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
