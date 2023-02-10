from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("IMAGE")
image = ImageTk.PhotoImage(Image.open(r"H:\Documents\GitHub\image1.jfif"))
label = Label(window, image=image)
label.pack()
window.mainloop()
