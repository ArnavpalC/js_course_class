from tkinter import *
from tkinter import messagebox
#from PIL import Image, ImageTk

root = Tk()
root.geometry('200x200')

#upload = Image.open('cat1.jpg')

#image = ImageTk.PhotoImage(upload)

#lab = Label(root, image=image, height=350, width=300)
#lab.place(x=50, y=0)

def msg():
    messagebox.showwarning('Alert', 'Stop! Virus Found.')

button = Button(root, text='scan for virus', command=msg)
button.place(x=40, y=80)

root.mainloop()
