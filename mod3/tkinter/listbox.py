from tkinter import *

root = Tk()
frame = Frame(root, padx=30, pady=30)
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


def print_line(event):
    index = event.widget.curselection()[0]
    print('you clicked on line {}'.format(index))

lb = Listbox(frame, bg='cyan', selectforeground='red', listvariable="zen", width=40)
lb.bind('<<ListboxSelect>>', print_line)
for item in items:
    lb.insert(END, item)
lb.pack(side=LEFT, fill=BOTH)

sby = Scrollbar(frame, orient=VERTICAL)
sby.pack(side=RIGHT, fill=Y)

sby.config(command=lb.yview)
lb.config(yscrollcommand=sby.set)

mainloop()


