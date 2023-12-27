import tkinter as tk
from tkinter import ttk, messagebox

class Task:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

tasks = []
completed_tasks = []

def add_task():
    description = entry_description.get()
    due_date = entry_due_date.get()
    priority = entry_priority.get()
    
    if description:
        tasks.append(Task(description, due_date, priority))
        messagebox.showinfo("Success", "Task added successfully!")
        clear_entries()
        update_task_listbox()
    else:
        messagebox.showwarning("Warning", "Task description cannot be empty!")

def display_tasks():
    task_list = ""
    for i, task in enumerate(tasks):
        task_list += f"{i+1}. {task.description}\n"
        if task.due_date:
            task_list += f"   Due Date: {task.due_date}\n"
        if task.priority:
            task_list += f"   Priority: {task.priority}\n"
    messagebox.showinfo("Pending Tasks", task_list)

def mark_task_completed():
    task_index = listbox_tasks.curselection()
    if task_index:
        task_index = task_index[0]
        completed_tasks.append(tasks.pop(task_index))
        messagebox.showinfo("Success", "Task marked completed!")
        update_task_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def update_task():
    task_index = listbox_tasks.curselection()
    if task_index:
        task_index = task_index[0]
        task = tasks[task_index]

        new_description = entry_description.get()
        new_due_date = entry_due_date.get()
        new_priority = entry_priority.get()

        task.description = new_description or task.description
        task.due_date = new_due_date or task.due_date
        task.priority = new_priority or task.priority

        messagebox.showinfo("Success", "Task updated successfully!")
        clear_entries()
        update_task_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

def remove_task():
    task_index = listbox_tasks.curselection()
    if task_index:
        task_index = task_index[0]
        tasks.pop(task_index)
        messagebox.showinfo("Success", "Task removed successfully!")
        update_task_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_entries():
    entry_description.delete(0, tk.END)
    entry_due_date.delete(0, tk.END)
    entry_priority.delete(0, tk.END)

def update_task_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, task.description)

# GUI setup
root = tk.Tk()
root.title("To-Do List Application")

# Style for ttk widgets
style = ttk.Style()
style.configure("TButton", padding=5, relief="flat", background="#66d9ef")
style.configure("TLabel", padding=5, background="#f8f8f8")
style.configure("TEntry", padding=5)

# Notebook
notebook = ttk.Notebook(root)

# Pending Tasks Tab
tab_pending = ttk.Frame(notebook)
notebook.add(tab_pending, text="Pending Tasks")

label_description = ttk.Label(tab_pending, text="Task Description:")
label_due_date = ttk.Label(tab_pending, text="Due Date:")
label_priority = ttk.Label(tab_pending, text="Priority:")

entry_description = ttk.Entry(tab_pending)
entry_due_date = ttk.Entry(tab_pending)
entry_priority = ttk.Entry(tab_pending)

button_add = ttk.Button(tab_pending, text="Add Task", command=add_task)
button_display = ttk.Button(tab_pending, text="Display Tasks", command=display_tasks)
button_completed = ttk.Button(tab_pending, text="Mark Completed", command=mark_task_completed)
button_update = ttk.Button(tab_pending, text="Update Task", command=update_task)
button_remove = ttk.Button(tab_pending, text="Remove Task", command=remove_task)

listbox_tasks = tk.Listbox(tab_pending)

# Grid layout for Pending Tasks
label_description.grid(row=0, column=0, pady=5)
label_due_date.grid(row=1, column=0, pady=5)
label_priority.grid(row=2, column=0, pady=5)

entry_description.grid(row=0, column=1, pady=5)
entry_due_date.grid(row=1, column=1, pady=5)
entry_priority.grid(row=2, column=1, pady=5)

button_add.grid(row=3, column=0, columnspan=2, pady=10)
button_display.grid(row=4, column=0, columnspan=2, pady=5)
button_completed.grid(row=5, column=0, columnspan=2, pady=5)
button_update.grid(row=6, column=0, columnspan=2, pady=5)
button_remove.grid(row=7, column=0, columnspan=2, pady=10)

listbox_tasks.grid(row=8, column=0, columnspan=2, pady=10)

# Completed Tasks Tab
tab_completed = ttk.Frame(notebook)
notebook.add(tab_completed, text="Completed Tasks")

listbox_completed_tasks = tk.Listbox(tab_completed)

# Grid layout for Completed Tasks
listbox_completed_tasks.pack(pady=10)

# Pack the Notebook
notebook.pack(padx=10, pady=10)

# Run the GUI
root.mainloop()
