from tkinter import *

root = Tk()
frame = Frame(root, padx=10, pady=10)
frame.pack()


def print_value():
    print('value={}'.format(sb.get()))

sb = Spinbox(frame, from_=1, to=10, justify=RIGHT, width=3, command=print_value)
sb.pack()
mainloop()
