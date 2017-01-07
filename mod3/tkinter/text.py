from tkinter import *

root = Tk()
T = Text(root, height=2, width=35)
T.pack()
T.insert(END, "Explicit is better than implicit.\nSimple is better than complex.")
mainloop()