import json
import os

class Task:
    def __init__(self, title, description, deadline, priority='Normal', completed=False):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.completed = completed

    def __str__(self):
        status = 'Completed' if self.completed else 'Not Completed'
        return f"'{self.title}' - {self.description} (Deadline: {self.deadline}, Priority: {self.priority}, Status: {status})"

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description, deadline, priority):
        self.tasks.append(Task(title, description, deadline, priority))
        print("Task added successfully.")

    def view_tasks(self, show_all=True, show_completed=False):
        tasks_to_show = self.tasks
        if not show_all:
            tasks_to_show = [task for task in self.tasks if task.completed == show_completed]

        if not tasks_to_show:
            print("No tasks to display.")
            return

        for index, task in enumerate(tasks_to_show, start=1):
            print(f"{index}. {task}")

    def edit_task(self, index, title=None, description=None, deadline=None, priority=None, completed=None):
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            task.title = title if title else task.title
            task.description = description if description else task.description
            task.deadline = deadline if deadline else task.deadline
            task.priority = priority if priority else task.priority
            if completed is not None:
                task.completed = completed
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
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

    def search_tasks(self, keyword):
        found_tasks = [task for task in self.tasks if keyword.lower() in task.title.lower()]
        if not found_tasks:
            print("No tasks match your search.")
            return
        for index, task in enumerate(found_tasks, start=1):
            print(f"{index}. {task}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTodo List - Choose an action:")
        print("1. Add task")
        print("2. View all tasks")
        print("3. View completed tasks")
        print("4. View incomplete tasks")
        print("5. Edit task")
        print("6. Delete task")
        print("7. Search for a task by keyword")
        print("8. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            deadline = input("Enter task deadline: ")
            priority = input("Enter task priority (Low, Normal, High): ")
            todo_list.add_task(title, description, deadline, priority)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks(show_all=False, show_completed=True)
        elif choice == '4':
            todo_list.view_tasks(show_all=False, show_completed=False)
        elif choice == '5':
            index = int(input("Enter task index to edit: "))
            title = input("Enter new title (leave blank for no change): ")
            description = input("Enter new description (leave blank for no change): ")
            deadline = input("Enter new deadline (leave blank for no change): ")
            priority = input("Enter new priority (leave blank for no change): ")
            completed_input = input("Is the task completed? (yes/no, leave blank for no change): ")
            completed = None
            if completed_input.lower() in ['yes', 'no']:
                completed = completed_input.lower() == 'yes'
            todo_list.edit_task(index, title, description, deadline, priority, completed)
        elif choice == '6':
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '7':
            keyword = input("Enter a keyword to search for tasks: ")
            todo_list.search_tasks(keyword)
        elif choice == '8':
            todo_list.save_tasks()
            print("Tasks saved. Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
