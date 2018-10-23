# This is my first GUI in python :)

#imports
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
win.resizable(0,0)

#button click event
def clickMe():
    action.configure(text="Hello there")
    aLabel.configure(foreground='red')

#adding a button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=0)

win.mainloop()
