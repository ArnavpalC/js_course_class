from tkinter import *
from PIL import Image, ImageTk

root = tk()
root.title('image')
root.geometry('400x400')

upload = Image.open('cat1.jpg')

image = ImageTk.PhotoImage(upload)

lab = Label(root, image=image, height=350, width=300)
lab.place(x=50, y=0)

root.mainloop()
