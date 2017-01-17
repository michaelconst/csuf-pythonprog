from tkinter.ttk import *
import tkinter as tk
from PIL import Image, ImageTk

KFC_FILE = '/Users/constantinm/Downloads/kfc.png'
MCDONALD_FILE = '/Users/constantinm/Downloads/mcdonald.jpeg'
BURGERKING_FILE = '/Users/constantinm/Downloads/burgerking.jpeg'
PIZZAHUT_FILE = '/Users/constantinm/Downloads/pizzahut.jpeg'
STARBUCKS_FILE = '/Users/constantinm/Downloads/starbucks.png'

master = tk.Tk()

# load images
image_kfc = ImageTk.PhotoImage(Image.open(KFC_FILE))
image_mcdonald = ImageTk.PhotoImage(Image.open(MCDONALD_FILE))
image_burgerking = ImageTk.PhotoImage(Image.open(BURGERKING_FILE))
image_pizzahut = ImageTk.PhotoImage(Image.open(PIZZAHUT_FILE))
image_starbucks = ImageTk.PhotoImage(Image.open(STARBUCKS_FILE))

fastfood = [
    ("KFC", image_kfc),
    ("McDonald's", image_mcdonald),
    ("BurgerKing", image_burgerking),
    ("PizzaHut", image_pizzahut),
    ("Starbucks", image_starbucks)
]

size = len(fastfood)
# initialize list of widget variables
vars = list()
for _ in range(0, size):
    vars.append(tk.IntVar())


# function to execute when a checkbox is clicked
def change_state():
    selected = [ff[0] for ff, v in zip(fastfood, vars) if v.get()]
    result.config(text=', '.join(selected))
    s = Style()
    for v, c in zip(vars, checkboxes):
        chkbtn_style = c.cget('style')
        if not chkbtn_style:
            chkbtn_style = 'TCheckbox'
        if v.get():
            s.configure(chkbtn_style, background='green')
        else:
            s.configure(chkbtn_style, background='red')

# create a checkbox for each fast food item
# use a grid layout
checkboxes = list()
s = Style()

for row, var, ff in zip(range(1, size+1), vars, fastfood):
    chk = Checkbutton(master, image=ff[1], variable=var, padding=5, command=change_state)
    chkbtn_style = chk.cget('style')
    if not chkbtn_style:
        chkbtn_style = 'TCheckbox'
    s.configure(chkbtn_style, background='red')
    chk.grid(row=row, sticky=tk.W)
    checkboxes.append(chk)

# create a label to concatenate the names for the selected checkboxes
result = Label(master, text='', width=40, anchor='w', padding=(5, 3))
result.grid(row=size+1)

tk.mainloop()
