# task_tracker.py
import json
import os
from task import Task

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return [Task.from_dict(d) for d in data]
        except json.JSONDecodeError:
            return []

def save_tasks(task_objs):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in task_objs], f, indent=4)

def next_id(tasks):
    if not tasks:
        return 1
    return max(t.id or 0 for t in tasks) + 1

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    description = input("Enter description (optional): ").strip()
    deadline = input("Deadline (YYYY-MM-DD) or press Enter to skip: ").strip() or None
    priority = input("Priority (Low/Medium/High) [Medium]: ").strip().capitalize() or "Medium"
    if priority not in ("Low","Medium","High"):
        priority = "Medium"

    t = Task(title, description, deadline, priority)
    t.id = next_id(tasks)
    tasks.append(t)
    save_tasks(tasks)
    print(f"✅ Task added (id={t.id})")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\n📋 Your Tasks:")
    print("-"*60)
    for t in tasks:
        status = "✓" if t.completed else "○"
        dl = t.deadline if t.deadline else "No deadline"
        print(f"{status} [{t.id}] {t.title} (Priority: {t.priority}, Deadline: {dl})")
        if t.description:
            print(f"    -> {t.description}")
    print("-"*60)

def mark_complete(tasks):
    view_tasks(tasks)
    try:
        tid = int(input("Enter task ID to mark complete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    for t in tasks:
        if t.id == tid:
            if t.completed:
                print("Task already completed.")
            else:
                t.mark_complete()
                save_tasks(tasks)
                print("✅ Task marked complete.")
            return
    print("Task ID not found.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        tid = int(input("Enter task ID to delete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    for i, t in enumerate(tasks):
        if t.id == tid:
            confirm = input(f"Are you sure you want to delete '{t.title}'? (y/n): ").strip().lower()
            if confirm == "y":
                tasks.pop(i)
                save_tasks(tasks)
                print("🗑️ Task deleted.")
            else:
                print("Delete cancelled.")
            return
    print("Task ID not found.")

def edit_task(tasks):
    view_tasks(tasks)
    try:
        tid = int(input("Enter task ID to edit: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    for t in tasks:
        if t.id == tid:
            print("Press Enter to keep current value.")
            new_title = input(f"Title [{t.title}]: ").strip()
            if new_title:
                t.title = new_title
            new_desc = input(f"Description [{t.description}]: ").strip()
            if new_desc:
                t.description = new_desc
            new_deadline = input(f"Deadline [{t.deadline}]: ").strip()
            if new_deadline:
                t.deadline = new_deadline
            new_priority = input(f"Priority [{t.priority}]: ").strip().capitalize()
            if new_priority in ("Low","Medium","High"):
                t.priority = new_priority
            save_tasks(tasks)
            print("✏️ Task updated.")
            return
    print("Task ID not found.")

def main_menu():
    tasks = load_tasks()
    while True:
        print("\n" + "="*40)
        print("🎯 Personal Task Tracker")
        print("="*40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit (saves automatically)")
        choice = input("Enter choice (1-6): ").strip()
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
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()
