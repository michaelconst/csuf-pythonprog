from tkinter import *
from PIL import Image, ImageTk

BRAD_FILE = '/Users/constantinm/Downloads/brad_pitt.jpg'

root = Tk()
brad_image = ImageTk.PhotoImage(Image.open(BRAD_FILE))

frame = Frame(root, padx=10, pady=10)
frame.pack()

Label(frame, text='First').grid(sticky=E)
Label(frame, text='Last').grid(sticky=E)
Label(frame, text='Country').grid(sticky=E)

Entry(frame).grid(row=0, column=1)
Entry(frame).grid(row=1, column=1)
Entry(frame).grid(row=2, column=1)

Checkbutton(frame, text='Remember').grid(row=3, sticky=W)

Label(frame, image=brad_image).grid(row=0, column=2, rowspan=3, sticky=W + E + N + S, padx=5, pady=5)

# Button(frame, text='Cancel').grid(row=3, column=1, sticky=E)
# Button(frame, text='Ok').grid(row=3, column=2)
btnok = Button(frame, text='Cancel')
btnok.grid(row=3, column=1, sticky=E)
btncancel = Button(frame, text='Ok')
btncancel.grid(row=3, column=2)
btnok.rowconfigure(3, pad=5)
btncancel.columnconfigure(2, weight=2)
mainloop()
