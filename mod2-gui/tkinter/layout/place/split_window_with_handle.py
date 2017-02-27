from tkinter import *

root = Tk()

frame = Frame(root, width=200, height=200)
frame.pack(fill=BOTH, expand=1)

bd = 2
split = 0.5
y1 = y2 = None
drag1 = drag2 = False

f1 = Frame(frame, bd=bd, relief=SUNKEN)
f2 = Frame(frame, bd=bd, relief=SUNKEN)
# handle = Frame(frame, bd=2, relief=RAISED, width=8, height=8, bg='red')
f1.place(rely=0, relheight=split, relwidth=1)
f2.place(rely=split, relheight=1.0 - split, relwidth=1)
# handle.place(relx=0.9, rely=split, width=8, height=8, anchor=E)

# TODO create classes to encapsulate this
def click1(event):
    y = event.y
    global y1
    y1 = y
    print('clicked1, y1={}'.format(y1))


def _adjust1(event, drag):
    y = event.y
    offset = y - y1
    if abs(offset) < 10:
        return
    global y1, split
    h = float(frame.winfo_height())
    split += offset / h
    y1 = y
    # print('dragging1' if drag else 'releasing1, y1={}, split={}'.format(y1, split))
    f1.place(rely=0, relheight=split, relwidth=1)
    f2.place(rely=split, relheight=1.0 - split, relwidth=1)


def draghold1(event):
    global drag1
    drag1 = True
    _adjust1(event, drag1)


def release1(event):
    global drag1
    if drag1:
        drag1 = False
        _adjust1(event, drag1)
        drag1 = False


def click2(event):
    y = event.y
    global y2
    y2 = y
    print('clicked2, y1={}'.format(y2))


def _adjust2(event, drag):
    y = event.y
    offset = y - y2
    if abs(offset) < 10:
        return
    global y2, split
    h = float(frame.winfo_height())
    split += offset / h
    y2 = y
    # print('dragging2' if drag else 'releasing2, y2={}, split={}'.format(y2, split))
    f1.place(rely=0, relheight=split, relwidth=1)
    f2.place(rely=split, relheight=1.0 - split, relwidth=1)


def draghold2(event):
    global drag2
    drag2 = True
    _adjust2(event, drag2)


def release2(event):
    global drag2
    if drag2:
        drag2 = False
        _adjust2(event, drag2)
        drag2 = False


f1.bind('<B1-Motion>', draghold1)
f2.bind('<B1-Motion>', draghold2)
f1.bind('<Button-1>', click1)
f2.bind('<Button-1>', click2)
f1.bind('<ButtonRelease-1>', release1)
f2.bind('<ButtonRelease-1>', release2)

mainloop()