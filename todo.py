# todo.py
# Simple To-Do List CLI Application

import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    """Load tasks from file"""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("\n📭 No tasks yet!")
        return
    
    print("\n📋 Your Tasks:")
    print("-" * 30)
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "⬜"
        print(f"{status} {i}. {task['title']}")
    print("-" * 30)

def add_task(tasks):
    """Add a new task"""
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("✅ Task added!")
    else:
        print("❌ Task cannot be empty!")

def complete_task(tasks):
    """Mark task as done"""
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print("✅ Task completed!")
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("❌ Please enter a number!")

def delete_task(tasks):
    """Delete a task"""
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️ Deleted: {removed['title']}")
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("❌ Please enter a number!")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n" + "=" * 30)
        print("📝 TO-DO LIST")
        print("=" * 30)
        print("1. 📋 View tasks")
        print("2. ➕ Add task")
        print("3. ✅ Complete task")
        print("4. 🗑️ Delete task")
        print("5. 🚪 Exit")
        
        choice = input("\nChoose (1-5): ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
