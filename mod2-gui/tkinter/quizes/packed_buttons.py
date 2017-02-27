from tkinter import *

root = Tk()
frame = Frame(root, padx=10, pady=10)
frame.pack(fill=BOTH, expand=YES)

Button(frame, text="Top").pack(side=BOTTOM, fill=X)
Button(frame, text="VCenter").pack(side=BOTTOM, fill=X)
Button(frame, text="Bottom").pack(fill=X)

Button(frame, text="Left").pack(side=RIGHT)
Button(frame, text="HCenter").pack(side=LEFT)
Button(frame, text="Right").pack(side=RIGHT)

mainloop()
