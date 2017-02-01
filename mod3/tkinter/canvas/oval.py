from tkinter import *

root = Tk()
c = Canvas(root, width=120, height=200)
c.pack()

oval1 = c.create_oval(10, 10, 110, 90, fill='orange', outline='blue', width=4)
oval2 = c.create_oval(10, 110, 110, 190, fill='blue', outline='orange', width=4)
c.addtag("ovals", "all")
mainloop()
