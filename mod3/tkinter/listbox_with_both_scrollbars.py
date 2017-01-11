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

sbx = Scrollbar(frame, orient=HORIZONTAL)
sbx.grid(row=1, column=0, columnspan=2, sticky=E+W)
sby = Scrollbar(frame, orient=VERTICAL)
sby.grid(row=0, column=1, sticky=N+S)

lb = Listbox(frame, bg='cyan', selectforeground='red', listvariable="zen",
             yscrollcommand=sby.set, xscrollcommand=sbx.set, hscroll=1, width=25)
for item in items:
    lb.insert(END, item)
lb.grid(row=0, column=0, sticky=N+S+E+W)
sbx.config(command=lb.xview)
sby.config(command=lb.yview)

mainloop()


