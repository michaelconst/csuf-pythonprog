from tkinter import *

root = Tk()
frame = Frame(root, padx=20, pady=20)
frame.pack()

pw = PanedWindow(frame, height=100, width=650, orient=HORIZONTAL, sashpad=10, showhandle=False,
                 relief=SUNKEN, sashrelief=SUNKEN)
pw.pack()
pane1 = Frame(pw)
pw.add(pane1, minsize=100, padx=5, pady=20, sticky=N)
e1 = Entry(pane1)
e1.pack()
e2 = Entry(pane1)
e2.pack()
e3 = Entry(pw)
pw.add(e3, height=30, minsize=100, padx=5, pady=20, sticky=N)
e4 = Entry(pw)
pw.add(e4, height=30, minsize=100, padx=5, pady=20, sticky=N)

mainloop()
