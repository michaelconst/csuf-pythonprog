from tkinter import *
from PIL import Image, ImageTk

KFC_FILE = '/Users/constantinm/Downloads/kfc.png'
MCDONALD_FILE = '/Users/constantinm/Downloads/mcdonald.jpeg'
BURGERKING_FILE = '/Users/constantinm/Downloads/burgerking.jpeg'
PIZZAHUT_FILE = '/Users/constantinm/Downloads/pizzahut.jpeg'
STARBUCKS_FILE = '/Users/constantinm/Downloads/starbucks.png'

master = Tk()

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
    vars.append(IntVar())


# function to execute when a checkbox is clicked
def change_state():
    selected = [ff[0] for ff, v in zip(fastfood, vars) if v.get()]
    result.config(text=', '.join(selected))
    # does not work if indicatoron is false
    for v, c in zip(vars, checkboxes):
        if v.get():
            c.configure(bg='green')
        else:
            c.configure(bg='red')

# create a checkbox for each fast food item
# use a grid layout
checkboxes = list()
for row, var, ff in zip(range(1, size+1), vars, fastfood):
    # background color is not applied with 'indicatoron' attribute as false
    # 'selectcolor' attribute (background color when widget is selected) does not work either (regardless of the value of 'indicatoron')
    # chk = Checkbutton(master, image=ff[1], variable=var, padx=5, pady=5, selectcolor='red', command=change_state)
    chk = Checkbutton(master, image=ff[1], variable=var, padx=5, pady=5, bg='red', indicatoron=0, command=change_state)
    chk.grid(row=row, sticky=W)
    checkboxes.append(chk)

# create a label to concatenate the names for the selected checkboxes
result = Label(master, text='', width=40, height=4, anchor='w', padx=5, pady=3)
result.grid(row=size+1)

mainloop()
