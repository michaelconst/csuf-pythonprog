from tkinter import *

root = Tk()
frame = Frame(root, padx=30, pady=30, width=25)
frame.pack()

zen = StringVar()
items = ["Beautiful is better than ugly",
"Explicit is better than implicit",
"Simple is better than complex",
"Complex is better than complicated",
"Flat is better than nested",
"Sparse is better than dense",
"Readability counts",
"Special cases aren't special enough to break the rules",
"Although practicality beats purity",
"Errors should never pass silently",
"Unless explicitly silenced",
"In the face of ambiguity, refuse the temptation to guess"]


# The sticky options on the .grid() method calls for the scrollbars
# force them to stretch just enough to fit the corresponding dimension of the canvas.
sbx = Scrollbar(frame, orient=HORIZONTAL)
sbx.grid(row=1, column=0, columnspan=2, sticky=E+W)
sby = Scrollbar(frame, orient=VERTICAL)
sby.grid(row=0, column=1, sticky=N+S)

lb = Listbox(frame, bg='cyan', selectforeground='red', listvariable="zen",
             yscrollcommand=sby.set, xscrollcommand=sbx.set, width=25)
for item in items:
    lb.insert(END, item)
lb.grid(row=0, column=0, sticky=N+S+E+W)
sbx.config(command=lb.xview)
sby.config(command=lb.yview)

entry = Entry(frame, width=7)
entry.grid(row=2, columnspan=2, sticky=E+W)


def scroll_handler(*scroll_args):
    if scroll_args:
        operation, num_units = scroll_args[0], scroll_args[1]
        if operation == SCROLL:
            # clicked on the arrows or in the scrollbar's trough, left ot right of the slider
            unit_type = scroll_args[2]
            entry.xview_scroll(num_units, unit_type)
        elif operation == MOVETO:
            # dragged the slider
            entry.xview_moveto(num_units)


sb_entry = Scrollbar(frame, orient=HORIZONTAL, command=scroll_handler)
sb_entry.grid(row=3, columnspan=2, sticky=E+W)
entry.config(xscrollcommand=sb_entry.set)

mainloop()


