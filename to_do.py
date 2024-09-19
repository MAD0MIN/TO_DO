import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('todo_list.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT 0
    )
''')
conn.commit()

def add_task():
    task = entry_task.get()
    if task:
        cursor.execute('INSERT INTO tasks (task, completed) VALUES (?, 0)', (task,))
        conn.commit()
        entry_task.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_task = listbox_tasks.get(listbox_tasks.curselection())
        task_id = selected_task[0]
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        update_task_list()
    except:
        messagebox.showwarning("Delete Error", "Please select a task to delete.")

def complete_task():
    try:
        selected_task = listbox_tasks.get(listbox_tasks.curselection())
        task_id = selected_task[0]
        cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
        conn.commit()
        update_task_list()
    except:
        messagebox.showwarning("Complete Error", "Please select a task to complete.")

def update_task_list():
    listbox_tasks.delete(0, tk.END)
    cursor.execute('SELECT id, task, completed FROM tasks')
    tasks = cursor.fetchall()
    for task in tasks:
        status = "Done" if task[2] else "Pending"
        listbox_tasks.insert(tk.END, (task[0], f"{task[1]} - {status}"))

root = tk.Tk()
root.title("To-Do List")

entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=10)

button_add_task = tk.Button(root, text="Add Task", width=15, command=add_task)
button_add_task.pack(pady=5)

button_delete_task = tk.Button(root, text="Delete Task", width=15, command=delete_task)
button_delete_task.pack(pady=5)

button_complete_task = tk.Button(root, text="Complete Task", width=15, command=complete_task)
button_complete_task.pack(pady=5)

listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

update_task_list()

root.mainloop()

conn.close()
