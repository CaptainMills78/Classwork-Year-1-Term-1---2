# It is recommended to use these instead of buttons in some cases
from tkinter import *

window = Tk() # Base root
window.title("Menu Demo")

menubar = Menu(window)  # Base menu
window.config(menu=menubar) # Set the menu as the base

file_menu = Menu(menubar)  # Add a file tab onto base menu
file_menu.add_command(label="Exit", command=window.destroy,)   # Add a command to tab
menubar.add_cascade(label="File", menu=file_menu, underline=0)  # Add way to access tab (through click or Alt+f)
window.mainloop()
