import json
import os
from todo import Task, PRIORITIES

class TaskManager:
    def __init__(self, storage_file="storage.json"):
        self.storage_file = storage_file
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.storage_file):
            self.tasks = []
            return
        
        with open(self.storage_file, "r") as f:
            data = json.load(f)
            self.tasks = [Task.from_dict(item) for item in data]

    def save_tasks(self):
        with open(self.storage_file, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, index):
        del self.tasks[index]
        self.save_tasks()

    def mark_completed(self, index):
        self.tasks[index].completed = True
        self.save_tasks()

    def edit_task(self, index, title=None, deadline=None, priority=None):
        if title:
            self.tasks[index].title = title
        if deadline:
            self.tasks[index].deadline = deadline
        if priority:
            self.tasks[index].priority = priority
        
        self.save_tasks()

    def list_tasks(self):
        return self.tasks