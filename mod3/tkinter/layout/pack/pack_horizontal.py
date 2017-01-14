from tkinter import *

root = Tk()
frame = Frame(root, width=300, height=100)
frame.pack()
frame.pack_propagate(0)

Label(frame, text="Red", bg="red", fg="white").pack(side=LEFT)
Label(frame, text="Blue", bg="blue", fg="white").pack(fill=Y, padx=10, ipadx=10, side=LEFT)
Label(frame, text="Green", bg="green", fg="black").pack(side=RIGHT)
mainloop()
