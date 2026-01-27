from tkinter import *


window = Tk()
window.title('Tkinter Sample window')
window.geometry('300x300')

greeting = Label(text='hello user', fg='black', bg='white')
button = Button(text='click me', fg='white', bg='black')
entry = Entry(fg='yellow', bg='blue', width=50 )
greeting.pack()
button.pack()
entry.pack()


frame = Frame(master = window, relief = RAISED , borderwidth = 5)
frame.pack()
label = Label(master = frame, text = 'sample frame')
label.pack()

tb = Text(fg='green', bg='yellow')
tb.pack()
