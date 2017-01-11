from tkinter import *

root = Tk()
frame = Frame(root, padx=30, pady=30)
frame.pack()

pw = PanedWindow(frame, height=100, width=600, orient=HORIZONTAL, sashpad=10, showhandle=False,
                 relief=SUNKEN, sashrelief=SUNKEN)
pw.pack()
e1 = Entry(pw)
pw.add(e1, height=30, minsize=100, padx=5, pady=20, sticky=N)
e2 = Entry(pw)
pw.add(e2, height=30, minsize=100, padx=5, pady=20, sticky=N)
e3 = Entry(pw)
pw.add(e3, height=30, minsize=100, padx=5, pady=20, sticky=N)

mainloop()
