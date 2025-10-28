# task.py
from datetime import datetime

class Task:
    def __init__(self, title, description="", deadline=None, priority="Medium"):
        """
        Simple Task object.
        - title: short string
        - description: optional details
        - deadline: YYYY-MM-DD string or None
        - priority: "Low", "Medium", "High"
        """
        self.id = None  # assigned by TaskManager when saved
        self.title = title
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(d):
        t = Task(d.get("title",""), d.get("description",""), d.get("deadline"), d.get("priority","Medium"))
        t.id = d.get("id")
        t.completed = d.get("completed", False)
        t.created_at = d.get("created_at")
        return t
