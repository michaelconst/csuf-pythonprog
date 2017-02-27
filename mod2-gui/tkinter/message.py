from tkinter import *

root = Tk()
message = Message(root, text="How are you on this first day of 2017?")
message.config(bg="blue", fg="yellow", width=300, font=("Comic Sans MS", 18))
message.pack()
root.mainloop()