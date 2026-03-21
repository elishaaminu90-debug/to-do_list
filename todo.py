from datetime import datetime

PRIORITIES = ["Critical", "High", "Medium", "Low", "Optional"]

class Task:
    def __init__(self, title, deadline, priority, completed=False):
        self.title = title
        self.deadline = deadline  # string: "YYYY-MM-DD HH:MM"
        self.priority = priority  # one of PRIORITIES[]
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "deadline": self.deadline,
            "priority": self.priority,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            deadline=data["deadline"],
            priority=data["priority"],
            completed=data["completed"]
        )