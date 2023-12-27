import datetime

class Task:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

tasks = []
completed_tasks = []

def add_task():
    description = input("Enter task description: ")
    due_date = input("Enter due date (DD--MM-YYYY) or leave blank: ")
    priority = input("Enter priority (low/medium/high) or leave blank: ")
    tasks.append(Task(description, due_date, priority))
    print("Task added successfully!")

def display_tasks():
    print("Pending Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task.description}")
        if task.due_date:
            print(f"   Due Date: {task.due_date}")
        if task.priority:
            print(f"   Priority: {task.priority}")
    print("\nCompleted Tasks:")
    for i, task in enumerate(completed_tasks):
        print(f"{i+1}. {task.description}")

def mark_task_completed():
    task_index = int(input("Enter task number to mark as completed: "))
    completed_tasks.append(tasks.pop(task_index - 1))
    print("Task marked completed!")

def update_task():
    task_index = int(input("Enter task number to update: "))
    task = tasks[task_index - 1]
    new_description = input("Enter new description (or leave blank to keep current): ")
    new_due_date = input("Enter new due date (or leave blank to keep current): ")
    new_priority = input("Enter new priority (or leave blank to keep current): ")
    task.description = new_description or task.description
    task.due_date = new_due_date or task.due_date
    task.priority = new_priority or task.priority
    print("Task updated successfully!")

def remove_task():
    task_index = int(input("Enter task number to remove: "))
    tasks.pop(task_index - 1)
    print("Task removed successfully!")

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task Completed")
    print("4. Update Task")
    print("5. Remove Task")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        update_task()
    elif choice == "5":
        remove_task()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
