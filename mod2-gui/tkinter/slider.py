from tkinter import *


root = Tk()
temp = Scale(root, from_=-10, to=120, tickinterval=10, length=300)
temp.set(67)
temp.pack()

humid = Scale(root, from_=30, to=80, tickinterval=5, orient=HORIZONTAL, length=300)
humid.set(55)
humid.pack()


def print_values():
    print('temp={}'.format(temp.get()))
    print('humidity={}'.format(humid.get()))

Button(root, text='Print', command=print_values).pack()
root.mainloop()