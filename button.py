import tkinter as tk
from time import sleep
import threading

# Create the main window
root = tk.Tk()
root.title("Hello")
root.geometry("400x300")

# Hide the default title bar
root.overrideredirect(True)

# Create a custom title bar
title_bar = tk.Frame(root, bg='lightgray', relief='raised', bd=0)
title_bar.pack(fill=tk.X)

def close_window():
    label.config(text="Huh???")
    def delay_close():
        sleep(1)
        root.destroy()
    threading.Thread(target=delay_close).start()

def minimize_window():
    root.iconify()

def maximize_window():
    root.attributes("-zoomed", True)

# Create custom circular buttons for close, minimize, and maximize
close_button = tk.Canvas(title_bar, width=15, height=15, bg='lightgray', highlightthickness=0)
close_button.create_oval(2, 2, 15, 15, fill='red')
close_button.bind("<Button-1>", lambda e: close_window())

minimize_button = tk.Canvas(title_bar, width=15, height=15, bg='lightgray', highlightthickness=0)
minimize_button.create_oval(2, 2, 15, 15, fill='yellow')
minimize_button.bind("<Button-1>", lambda e: minimize_window())

maximize_button = tk.Canvas(title_bar, width=15, height=15, bg='lightgray', highlightthickness=0)
maximize_button.create_oval(2, 2, 15, 15, fill='green')
maximize_button.bind("<Button-1>", lambda e: maximize_window())

close_button.pack(side=tk.LEFT, padx=5, pady=2)
minimize_button.pack(side=tk.LEFT, padx=5, pady=2)
maximize_button.pack(side=tk.LEFT, padx=5, pady=2)

# Create a label with the text
label = tk.Label(root, text="Do not close this window")
label.pack(pady=50)  # Add some padding

# Function to drag the window
def move_window(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')

title_bar.bind('<B1-Motion>', move_window)

# Run the Tkinter event loop
root.mainloop()
