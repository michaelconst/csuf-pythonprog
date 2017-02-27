from tkinter import *
from PIL import Image, ImageTk

BRAD_FILE = '/Users/constantinm/Downloads/brad_pitt.jpg'

root = Tk()
brad_image = ImageTk.PhotoImage(Image.open(BRAD_FILE))

frame = Frame(root, padx=10, pady=10, width=150, height=150)
frame.pack()
frame.pack_propagate(0)
# Label(frame, text="A", font=('Ariel', 32, 'bold')).place(anchor=NW)
# Label(frame, text="merican", font=('Ariel', 14, 'bold')).place(x=25, y=18)
# Label(frame, text="ctors", wraplength=1, font=('Ariel', 14, 'bold')).place(x=12, y=38)
# b = Button(frame, image=brad_image)
# b.place(x=35, y=45, anchor=NW)

a = Label(frame, text="A", font=('Arial', 32, 'bold'))
a.place(anchor=NW)
Label(frame, text="merican", font=('Arial', 14, 'bold')).place(in_=a, relx=1, rely=1, x=-2, y=-17, bordermode="outside", anchor=W)
Label(frame, text="ctors", wraplength=1, font=('Arial', 14, 'bold')).place(in_=a, relx=1, rely=1, x=-12, y=-7, bordermode="outside", anchor=N)
Button(frame, image=brad_image).place(in_=a, relx=1, rely=1, x=5, y=5, bordermode="outside", anchor=NW)

mainloop()
