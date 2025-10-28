# task.py
from datetime import datetime

class Task:
    """
    Represents a single task with title, description, deadline, and priority.
    """
    
    def __init__(self, title, description="", deadline=None, priority="Medium"):
        """
        Initialize a new Task.
        
        Args:
            title (str): Task title (required)
            description (str): Optional task description
            deadline (str): Deadline in YYYY-MM-DD format or None
            priority (str): "Low", "Medium", or "High"
        """
        self.id = None  # Assigned by TaskManager when saved
        self.title = title
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.completed_at = None

    def mark_complete(self):
        """Mark this task as completed with timestamp."""
        self.completed = True
        self.completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def is_overdue(self):
        """
        Check if task is past its deadline.
        
        Returns:
            bool: True if task is overdue and not completed
        """
        if not self.deadline or self.completed:
            return False
        try:
            deadline_date = datetime.strptime(self.deadline, "%Y-%m-%d")
            return datetime.now() > deadline_date
        except ValueError:
            return False

    def to_dict(self):
        """
        Convert Task object to dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at,
            "completed_at": self.completed_at
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Task object from a dictionary.
        
        Args:
            data (dict): Dictionary containing task data
            
        Returns:
            Task: Task object created from dictionary
        """
        task = Task(
            data.get("title", ""),
            data.get("description", ""),
            data.get("deadline"),
            data.get("priority", "Medium")
        )
        task.id = data.get("id")
        task.completed = data.get("completed", False)
        task.created_at = data.get("created_at")
        task.completed_at = data.get("completed_at")
        return task

    def __str__(self):
        """String representation of the task."""
        status = "✓" if self.completed else "○"
        return f"{status} [{self.id}] {self.title} (Priority: {self.priority})"