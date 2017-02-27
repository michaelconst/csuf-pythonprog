from tkinter import *

root = Tk()
root.geometry('200x200+10+100')

Label(root, text='Label1', bg='green').pack(expand=1, fill=Y)
Label(root, text='Label2', bg='blue').pack(expand=1, fill=Y)
Label(root, text='Label3', bg='red').pack(fill=BOTH)

root.mainloop()