import tkinter as tk
from tkinter import ttk

clickcount = 0

# functions
def buttonfunc():
    global clickcount
    clickcount += 1
    label.config(text="You clicked {} times".format(clickcount))

# Create a new window
window = tk.Tk()
window.geometry("800x600")

# Set the window title
window.title("Clicker Game")

# Create a label widget and pack it
label = ttk.Label(master=window, text="You clicked 0 times", font = 'Arial 20')
label.pack()

# Create a button and pack it
button = tk.Button(master=window, text='Click Me', command=buttonfunc, width = 20, height = 5)
button.pack()

# Start the GUI event loop
window.mainloop()
