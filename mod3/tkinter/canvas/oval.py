from tkinter import *

root = Tk()
c = Canvas(root, width=200, height=100)
c.pack()

c.create_oval(10, 10, 190, 90, fill='orange', outline='blue', width=4, stipple='gray25', outlinestipple='gray75')
mainloop()