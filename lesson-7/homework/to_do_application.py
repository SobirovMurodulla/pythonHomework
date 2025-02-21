from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass


class Task:
    def __init__(self, task_id, title, description, due_date=None, status='Pending'):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


class TaskManager:
    def __init__(self, storage):
        self.tasks = []
        self.storage = storage

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if status:
                    task.status = status
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print("No tasks found with the specified status.")
        else:
            for task in filtered_tasks:
                print(task)

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.storage.load()
        print("Tasks loaded successfully!")

