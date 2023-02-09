import tkinter.ttk
from tkinter import *




window = Tk()
window.title("Example of Tree View")
window.geometry("500x500")

tree = tkinter.ttk.Treeview(window)
tree.insert("","end", text="Applications")
tree.insert("", 0, "gallery", text="Applications")

id = tree.insert("", "end", text="Tutorial")


tree.insert(id, 'end', text='Tree')

window.mainloop()