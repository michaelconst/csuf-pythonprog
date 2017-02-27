from tkinter import *

root = Tk()

visibility = IntVar()
visibility.set(1)

def print_value():
    lbl_value.configure(text=visibility.get())

Label(root,
      text="""Select the blog visibility:""",
      justify=LEFT,
      padx=10).pack()
Radiobutton(root,
            text="Public",
            padx=10,
            indicatoron=0,
            width=7,
            variable=visibility,
            command=print_value,
            value=1).pack(anchor=W)
Radiobutton(root,
            text="Team",
            padx=10,
            indicatoron=0,
            width=7,
            variable=visibility,
            command=print_value,
            value=2).pack(anchor=W)
lbl_value = Label(root,
                  text=str(visibility.get()),
                  justify=LEFT,
                  padx=10, pady=5)
lbl_value.pack()

mainloop()
