from tkinter import *

root = Tk()
frame = Frame(root, padx=30, pady=30)
frame.pack()
lf = LabelFrame(frame, width=300, height=200, padx=10, pady=10, bd=4, labelanchor='ne', text="Gender")
lf.pack(fill=BOTH)

Radiobutton(lf, text='Male', justify=LEFT, anchor=W).pack(side=BOTTOM, fill=X)
Radiobutton(lf, text='Female', justify=LEFT, anchor=W).pack(side=BOTTOM, fill=X)

mainloop()