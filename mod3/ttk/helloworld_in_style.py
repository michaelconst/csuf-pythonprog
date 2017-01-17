from tkinter.ttk import *
import tkinter as tk

root = tk.Tk()
s = Style()
s.configure('Big.TLabel', font='Arial 24')
s.map('Big.TLabel', font=[('pressed', 'Arial 30')])
lbl = Label(root, text="Hello, World!", padding=20, style='Big.TLabel')
lbl.pack()

s.configure('BigButton.TButton', font='Arial 24', foreground='red', relief=tk.RAISED)
s.map('BigButton.TButton', relief=[('pressed', '!disabled', tk.SUNKEN)])
Button(root, text='Click Me', style='BigButton.TButton').pack()

print('Button.border options={}'.format(s.element_options('Button.border')))
root.mainloop()
