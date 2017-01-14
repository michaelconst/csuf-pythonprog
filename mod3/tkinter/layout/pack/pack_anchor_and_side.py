from tkinter import *

root = Tk()
frame = Frame(root, padx=30)
frame.pack()

colors = ('red', 'green', 'blue', 'teal', 'orange')
heights = (9, 7, 6, 8, 5)
for i in range(0, 5):
    Label(frame, text=chr(ord('a') + i), bg=colors[i], height=heights[i]).pack(side=LEFT)
    # Label(frame, text=chr(ord('a')+i), bg=colors[i], height=heights[i], anchor='n').pack(side=LEFT, anchor='n')

root.mainloop()
