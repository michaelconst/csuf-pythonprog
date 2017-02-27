from tkinter import *
from tkinter.font import *


root = Tk()
c = Canvas(root, width=200, height=180)
c.pack()

# create body
c.create_rectangle(20, 100, 170, 150, fill='black')
# create the caboose
c.create_rectangle(140, 70, 170, 100, fill='yellow')
# create the chimney
pts = [30, 70, 50, 70, 40, 100]
c.create_polygon(pts, fill='green')
# create the wheels
c.create_oval(30, 150, 50, 170, fill='red')
c.create_oval(140, 150, 160, 170, fill='red')
# write
font = Font(family='Lucida Handwriting', size=14, weight="bold")
c.create_text((20+170)/2, (100+150)/2, text="Soul Train", fill="white", font=font)
mainloop()

