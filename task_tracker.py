# task_tracker.py
import json
import os
from datetime import datetime
from task import Task

TASK_FILE = "tasks.json"

def load_tasks():
    """
    Load tasks from JSON file.
    
    Returns:
        list: List of Task objects
    """
    if not os.path.exists(TASK_FILE):
        return []
    
    with open(TASK_FILE, "r", encoding="utf-8") as f:
        try:
            content = f.read().strip()
            if not content:  # Handle empty file
                return []
            data = json.loads(content)
            return [Task.from_dict(d) for d in data]
        except json.JSONDecodeError:
            print("⚠️ tasks.json is corrupted. Starting with empty task list.")
            return []

def save_tasks(task_objs):
    """
    Save tasks to JSON file.
    
    Args:
        task_objs (list): List of Task objects to save
    """
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in task_objs], f, indent=4)

def next_id(tasks):
    """
    Generate next available task ID.
    
    Args:
        tasks (list): List of existing tasks
        
    Returns:
        int: Next available ID
    """
    if not tasks:
        return 1
    return max(t.id or 0 for t in tasks) + 1

def validate_date(date_str):
    """
    Validate date format (YYYY-MM-DD).
    
    Args:
        date_str (str): Date string to validate
        
    Returns:
        bool: True if valid format, False otherwise
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_task(tasks):
    """Add a new task with user input."""
    print("\n➕ Add New Task")
    print("-" * 40)
    
    title = input("Task title: ").strip()
    if not title:
        print("❌ Title cannot be empty.")
        return
    
    description = input("Description (optional): ").strip()
    
    deadline = input("Deadline (YYYY-MM-DD) or press Enter to skip: ").strip()
    if deadline:
        if not validate_date(deadline):
            print("⚠️ Invalid date format. Skipping deadline.")
            deadline = None
    else:
        deadline = None
    
    priority = input("Priority (Low/Medium/High) [Medium]: ").strip().capitalize()
    if priority not in ("Low", "Medium", "High"):
        priority = "Medium"
    
    task = Task(title, description, deadline, priority)
    task.id = next_id(tasks)
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added successfully (ID: {task.id})")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\n📋 No tasks found. Add your first task!")
        return
    
    print("\n📋 Your Tasks:")
    print("-" * 70)
    
    for t in tasks:
        status = "✓" if t.completed else "○"
        deadline_str = t.deadline if t.deadline else "No deadline"
        
        # Check if overdue
        overdue = ""
        if t.is_overdue():
            overdue = " ⚠️ OVERDUE"
        
        print(f"{status} [{t.id}] {t.title}{overdue}")
        print(f"    Priority: {t.priority} | Deadline: {deadline_str}")
        
        if t.description:
            print(f"    Note: {t.description}")
        
        if t.completed and t.completed_at:
            print(f"    Completed: {t.completed_at}")
        
        print()
    
    print("-" * 70)

def mark_complete(tasks):
    """Mark a task as complete."""
    if not tasks:
        print("\n📋 No tasks available.")
        return
    
    view_tasks(tasks)
    
    try:
        task_id = int(input("Enter task ID to mark complete: ").strip())
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")
        return
    
    for t in tasks:
        if t.id == task_id:
            if t.completed:
                print("ℹ️ Task is already completed.")
            else:
                t.mark_complete()
                save_tasks(tasks)
                print("✅ Task marked as complete!")
            return
    
    print("❌ Task ID not found.")

def delete_task(tasks):
    """Delete a task after confirmation."""
    if not tasks:
        print("\n📋 No tasks available.")
        return
    
    view_tasks(tasks)
    
    try:
        task_id = int(input("Enter task ID to delete: ").strip())
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")
        return
    
    for i, t in enumerate(tasks):
        if t.id == task_id:
            confirm = input(f"⚠️ Delete '{t.title}'? (y/n): ").strip().lower()
            if confirm == "y":
                tasks.pop(i)
                save_tasks(tasks)
                print("🗑️ Task deleted successfully.")
            else:
                print("❌ Delete cancelled.")
            return
    
    print("❌ Task ID not found.")

def edit_task(tasks):
    """Edit an existing task."""
    if not tasks:
        print("\n📋 No tasks available.")
        return
    
    view_tasks(tasks)
    
    try:
        task_id = int(input("Enter task ID to edit: ").strip())
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")
        return
    
    for t in tasks:
        if t.id == task_id:
            print("\n✏️ Edit Task (press Enter to keep current value)")
            print("-" * 40)
            
            new_title = input(f"Title [{t.title}]: ").strip()
            if new_title:
                t.title = new_title
            
            new_desc = input(f"Description [{t.description}]: ").strip()
            if new_desc:
                t.description = new_desc
            
            new_deadline = input(f"Deadline [{t.deadline}]: ").strip()
            if new_deadline:
                if validate_date(new_deadline):
                    t.deadline = new_deadline
                else:
                    print("⚠️ Invalid date format. Keeping old deadline.")
            
            new_priority = input(f"Priority [{t.priority}]: ").strip().capitalize()
            if new_priority in ("Low", "Medium", "High"):
                t.priority = new_priority
            
            save_tasks(tasks)
            print("✅ Task updated successfully.")
            return
    
    print("❌ Task ID not found.")

def view_stats(tasks):
    """Display task statistics."""
    if not tasks:
        print("\n📊 No tasks to analyze.")
        return
    
    total = len(tasks)
    completed = sum(1 for t in tasks if t.completed)
    pending = total - completed
    overdue = sum(1 for t in tasks if t.is_overdue())
    
    high = sum(1 for t in tasks if t.priority == "High" and not t.completed)
    medium = sum(1 for t in tasks if t.priority == "Medium" and not t.completed)
    low = sum(1 for t in tasks if t.priority == "Low" and not t.completed)
    
    print("\n📊 Task Statistics")
    print("=" * 50)
    print(f"Total Tasks:       {total}")
    print(f"✓ Completed:       {completed}")
    print(f"○ Pending:         {pending}")
    if total > 0:
        print(f"Completion Rate:   {(completed/total)*100:.1f}%")
    print()
    
    if overdue > 0:
        print(f"⚠️ Overdue Tasks:   {overdue}")
        print()
    
    if pending > 0:
        print("Pending Tasks by Priority:")
        print(f"  🔴 High:    {high}")
        print(f"  🟡 Medium:  {medium}")
        print(f"  🟢 Low:     {low}")
    
    print("=" * 50)

def main_menu():
    """Main application loop."""
    tasks = load_tasks()
    
    print("\n" + "=" * 50)
    print("       🎯 Welcome to Personal Task Tracker")
    print("=" * 50)
    
    while True:
        print("\n📌 Main Menu")
        print("-" * 40)
        print("1. ➕ Add Task")
        print("2. 📋 View All Tasks")
        print("3. ✅ Mark Task Complete")
        print("4. ✏️  Edit Task")
        print("5. 🗑️  Delete Task")
        print("6. 📊 View Statistics")
        print("7. 🚪 Exit")
        print("-" * 40)
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            view_stats(tasks)
        elif choice == "7":
            save_tasks(tasks)
            print("\n✨ All tasks saved. Goodbye! ✨\n")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1-7.")

if __name__ == "__main__":
    main_menu()