import tkinter as tk
from tkinter import messagebox

# Initialize the Tkinter root window (invisible)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Show the message box
messagebox.showinfo("Message", "hi")
