from tkinter import *

root = Tk()

frame = Frame(root, width=150, height=150, bg='gray')
frame.pack()
frame.pack_propagate(0)

w1 = Label(frame, bg='red')
w1.place(x=25, y=25, relwidth=1, relheight=1, width=-50, height=-50)
w2 = Label(frame, bg='blue')
w2.place(in_=w1, relx=0.5, y=-2, relwidth=0.25, anchor=S, bordermode="outside")
mainloop()
