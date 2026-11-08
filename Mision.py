import tkinter as tk
from tkinter import messagebox

# ---------- Main Window ----------
root = tk.Tk()
root.title("To-Do App")
root.geometry("400x455")

# List to store tasks in memory
tasks = []

# ---------- Functions ----------
def add_task():
    task = entry.get().strip()  # Get text and remove extra spaces
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return
    
    tasks.append(task)           # Add to data list
    listbox.insert(tk.END, task) # Add to UI list
    entry.delete(0, tk.END)      # Clear input field

def delete_task():
    selected = listbox.curselection()  # Get selected item index
    if not selected:
        messagebox.showwarning("Warning", "Please select a task to delete!")
        return
    
    index = selected[0]
    listbox.delete(index)        # Remove from UI
    tasks.pop(index)             # Remove from data list

# ---------- UI Elements ----------
tk.Label(root, text="My Tasks", font=("Arial", 16, "bold")).pack(pady=10)

entry = tk.Entry(root, width=35, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Add Task", width=20, command=add_task).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=12, font=("Arial", 12))
listbox.pack(pady=10)

tk.Button(root, text="Delete Selected Task", width=25, command=delete_task).pack(pady=5)

# Start the application
root.mainloop()