from tkinter import *
from PIL import ImageTk, Image

root = Tk()
pic = ImageTk.PhotoImage(Image.open('/Users/constantinm/Downloads/cheetah.png'))
lbl2 = Label(root, image=pic).pack(side="right")
txt = "cheetah"
lbl3= Label(root, text=txt, justify=LEFT, padx=20)
lbl3.pack(side="left")
root.mainloop()