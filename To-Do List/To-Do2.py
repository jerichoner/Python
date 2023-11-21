import json

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline

    def __repr__(self):
        return f"Task('{self.title}', '{self.description}', '{self.deadline}')"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        new_task = Task(title, description, deadline)
        self.tasks.append(new_task)
        print(f"Added task: {new_task}")

    def view_tasks(self):
        for task in self.tasks:
            print(f"Title: {task.title}, Description: {task.description}, Deadline: {task.deadline}")

    def edit_task(self, task_title, new_title=None, new_description=None, new_deadline=None):
        for task in self.tasks:
            if task.title == task_title:
                if new_title:
                    task.title = new_title
                if new_description:
                    task.description = new_description
                if new_deadline:
                    task.deadline = new_deadline
                print(f"Task updated: {task}")
                return
        print(f"Task with title '{task_title}' not found.")

    def delete_task(self, task_title):
        for i, task in enumerate(self.tasks):
            if task.title == task_title:
                del self.tasks[i]
                print(f"Deleted task '{task_title}'")
                return
        print(f"Task with title '{task_title}' not found.")

    def save_tasks(self, file_path):
        with open(file_path, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def load_tasks(self, file_path):
        with open(file_path, 'r') as f:
            tasks_data = json.load(f)
            for task_data in tasks_data:
                self.add_task(task_data['title'], task_data['description'], task_data['deadline'])

# Main program flow
def main():
    todo_list = ToDoList()
    todo_list.add_task('Grocery Shopping', 'Buy milk, bread, and eggs', '2023-11-25')
    todo_list.view_tasks()
    # Add more interaction code here

if __name__ == "__main__":
    main()
