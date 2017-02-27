from tkinter import *

master = Tk()
frame = Frame(master, padx=10, pady=5)
frame.pack()
Label(frame, text="Username").grid(row=0)
Label(frame, text="Password").grid(row=1)

e1 = Entry(frame)
e2 = Entry(frame)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(frame, text='Login', padx=5, pady=5).grid(row=2, columnspan=2, pady=5, sticky=E)
mainloop( )