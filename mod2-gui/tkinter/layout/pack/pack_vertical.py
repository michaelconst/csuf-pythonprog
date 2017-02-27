from tkinter import *

root = Tk()
frame = Frame(root, padx=10, pady=10, width=100, height=300)
frame.pack()
frame.pack_propagate(0)

Button(frame, text="Red", bg="red", fg="red", bd=3, relief=RAISED).pack(anchor=W)
Button(frame, text="Blue", bg="blue", fg="blue", bd=3, relief=RAISED).pack(pady=20)
Button(frame, text="Green", bg="green", fg="green", bd=3, relief=RAISED).pack()

Label(frame, text="Red", bg="red", fg="white").pack(fill=X)
Label(frame, text="Blue", bg="blue", fg="white").pack(fill=X, pady=10, ipady=10)
Label(frame, text="Green", bg="green", fg="black").pack(anchor=E)
mainloop()
