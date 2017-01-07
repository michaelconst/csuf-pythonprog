from tkinter import *

root = Tk()
c = Canvas(root, width=70, height=30)
c.pack()

c.create_line(10, 10, 70, 10, dash=(3, 1, 2, 1, 3, 3, 1, 4, 3, 2), width=30)
mainloop()