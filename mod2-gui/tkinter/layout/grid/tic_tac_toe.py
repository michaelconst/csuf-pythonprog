from tkinter import *
from PIL import Image, ImageTk
from random import randint

X_FILE = '/Users/constantinm/Downloads/x.png'
O_FILE = '/Users/constantinm/Downloads/o.png'

root = Tk()
images = (ImageTk.PhotoImage(Image.open(X_FILE)), ImageTk.PhotoImage(Image.open(O_FILE)))

frame = Frame(root, padx=10, pady=10)
frame.pack()

# use separators
# from tkinter.ttk import Separator
#
# for i in range(0, 5):
#     if i % 2 == 0:
#         for j in range(0, 5):
#             if j % 2 == 0:
#                 idx = randint(1, 100) % 2
#                 Label(frame, image=images[idx]).grid(row=i, column=j)
#             else:
#                 Separator(frame, orient=VERTICAL).grid(row=0, rowspan=5, column=j, sticky=NS)
#     else:
#         Separator(frame, orient=HORIZONTAL).grid(row=i, column=0, columnspan=5, sticky=EW)

# use a grid image
GRID_FILE = '/Users/constantinm/Downloads/grid.png'
grid_image = ImageTk.PhotoImage(Image.open(GRID_FILE))
Label(frame, image=grid_image).grid(row=0, column=0, rowspan=3, columnspan=3)
for i in range(0, 3):
    for j in range(0, 3):
        idx = randint(1, 100) % 2
        Label(frame, image=images[idx]).grid(row=i, column=j)

mainloop()
