# 📝 Personal Task Tracker

A command-line task management application built with Python to help organize daily tasks with priorities, deadlines, and completion tracking.

## 📖 About

This is a practical task manager I built to strengthen my Python fundamentals including file handling, data structures, and object-oriented programming. The application runs in your terminal and stores all tasks in a JSON file for persistent storage across sessions.

**Why I built this:** I wanted to create something useful that I could actually use daily while learning core Python concepts like classes, file I/O, error handling, and data validation. This project helped me understand how to structure code properly and build user-friendly interfaces.

## ✨ Features

- ➕ **Add Tasks** - Create tasks with title, description, deadline, and priority
- 📋 **View Tasks** - See all tasks with their details and status
- ✅ **Mark Complete** - Check off finished tasks with timestamp tracking
- ✏️ **Edit Tasks** - Modify existing task details
- 🗑️ **Delete Tasks** - Remove tasks with confirmation prompt
- 📊 **View Statistics** - Track completion rates and analyze productivity
- ⚠️ **Overdue Alerts** - Automatic detection of tasks past their deadline
- 💾 **Auto-save** - Changes are saved immediately to JSON file
- 📂 **Persistent Storage** - Your tasks load automatically on restart

## 🛠️ Technologies Used

- **Python 3.6+** - Core programming language
- **JSON** - Data storage and serialization
- **datetime** - Date handling and validation
- **os** - File system operations

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## 🚀 Getting Started

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ATOO7/Personal-Task-Tracker.git
   cd Personal-Task-Tracker
   ```

2. **Run the application**
   ```bash
   python task_tracker.py
   ```

That's it! No pip installations needed.

## 💻 Usage

### Main Menu

When you run the application, you'll see:

```
==================================================
       🎯 Welcome to Personal Task Tracker
==================================================

📌 Main Menu
----------------------------------------
1. ➕ Add Task
2. 📋 View All Tasks
3. ✅ Mark Task Complete
4. ✏️  Edit Task
5. 🗑️  Delete Task
6. 📊 View Statistics
7. 🚪 Exit
----------------------------------------
Enter your choice (1-7):
```

### Example Workflow

**Adding a Task:**
```bash
1
➕ Add New Task
----------------------------------------
Task title: Complete Python project
Description (optional): Finish the task tracker and push to GitHub
Deadline (YYYY-MM-DD) or press Enter to skip: 2024-11-05
Priority (Low/Medium/High) [Medium]: High
✅ Task added successfully (ID: 1)
```

**Viewing Tasks:**
```bash
2
📋 Your Tasks:
----------------------------------------------------------------------
○ [1] Complete Python project
    Priority: High | Deadline: 2024-11-05
    Note: Finish the task tracker and push to GitHub

✓ [2] Buy groceries
    Priority: Medium | Deadline: 2024-10-30
    Note: Milk, eggs, bread, vegetables
    Completed: 2024-10-28 18:45:00
----------------------------------------------------------------------
```

**Viewing Statistics:**
```bash
6
📊 Task Statistics
==================================================
Total Tasks:       3
✓ Completed:       1
○ Pending:         2
Completion Rate:   33.3%

Pending Tasks by Priority:
  🔴 High:    1
  🟡 Medium:  0
  🟢 Low:     1
==================================================
```

## 📂 Project Structure

```
Personal-Task-Tracker/
├── task.py              # Task class definition (data model)
├── task_tracker.py      # Main application logic and CLI
├── tasks.json          # Data storage (auto-generated)
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## 📊 Data Storage

Tasks are stored in `tasks.json` with the following structure:

```json
[
    {
        "id": 1,
        "title": "Complete Python project",
        "description": "Finish the task tracker and push to GitHub",
        "deadline": "2024-11-05",
        "priority": "High",
        "completed": false,
        "created_at": "2024-10-28 14:30:00",
        "completed_at": null
    }
]
```

The file is automatically created on first run and updated with every change.

## 🏗️ Code Architecture

### Object-Oriented Design

**Task Class (`task.py`):**
- Represents a single task with all its properties
- Methods: `mark_complete()`, `is_overdue()`, `to_dict()`, `from_dict()`
- Handles data validation and business logic

**Task Manager (`task_tracker.py`):**
- Handles user interface and file operations
- Functions for CRUD operations (Create, Read, Update, Delete)
- Input validation and error handling

### Key Design Decisions

1. **Separation of Concerns**: Task data model separate from application logic
2. **JSON Storage**: Human-readable format, easy to debug and backup
3. **ID Generation**: Sequential IDs with gap handling after deletions
4. **Date Validation**: Prevents invalid date entries using datetime parsing
5. **Error Handling**: Try-except blocks for file operations and user input

## 🎓 What I Learned

Building this project helped me understand:

- **Object-Oriented Programming**: Creating classes with methods and properties
- **File I/O Operations**: Reading, writing, and handling JSON files
- **Error Handling**: Using try-except blocks to handle edge cases
- **Data Validation**: Ensuring user inputs are valid before processing
- **Code Organization**: Separating concerns into different modules
- **User Experience**: Creating intuitive CLI interfaces with clear feedback
- **Data Persistence**: Maintaining state across application sessions
- **Documentation**: Writing docstrings and clear function comments

## 🚧 Known Limitations

- Single user only (no authentication or multi-user support)
- Local storage only (no cloud sync)
- Command-line interface (no GUI)
- No task categories or tags
- No recurring tasks functionality
- Manual date entry (no natural language parsing like "tomorrow")

## 🔮 Future Enhancements

Features I plan to add as I continue learning:

- [ ] Task categories and tags for better organization
- [ ] Search and filter functionality
- [ ] Export tasks to CSV or PDF
- [ ] Recurring tasks (daily/weekly/monthly)
- [ ] Task reminders with desktop notifications
- [ ] Natural language date parsing ("tomorrow", "next Monday")
- [ ] Subtasks and task dependencies
- [ ] SQLite database instead of JSON for better performance
- [ ] GUI version using Tkinter
- [ ] Web interface using Flask
- [ ] Unit tests with pytest

## 🧪 Testing

The application handles various edge cases:

- ✅ Empty JSON file or corrupted data
- ✅ Invalid date formats
- ✅ Non-existent task IDs
- ✅ Empty title validation
- ✅ Priority input validation
- ✅ Delete confirmation to prevent accidents

## 🤝 Contributing

This is a learning project, but feedback and suggestions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Aksh Thada**

- GitHub: [@ATOO7](https://github.com/ATOO7)
- Project Link: [Personal Task Tracker](https://github.com/ATOO7/Personal-Task-Tracker)

## 🙏 Acknowledgments

- Built as a hands-on learning project to practice Python fundamentals
- Inspired by the need for a simple, lightweight task manager
- Thanks to the Python community for excellent documentation and resources

---

⭐ If you found this project helpful for learning, consider giving it a star!

## 📸 Screenshots

### Adding a Task
```
➕ Add New Task
----------------------------------------
Task title: Learn Git and GitHub
Description (optional): Practice version control
Deadline (YYYY-MM-DD) or press Enter to skip: 2024-11-10
Priority (Low/Medium/High) [Medium]: High
✅ Task added successfully (ID: 1)
```

### Task Statistics
```
📊 Task Statistics
==================================================
Total Tasks:       5
✓ Completed:       3
○ Pending:         2
Completion Rate:   60.0%

Pending Tasks by Priority:
  🔴 High:    1
  🟡 Medium:  1
  🟢 Low:     0
==================================================
```