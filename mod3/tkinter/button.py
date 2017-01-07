from tkinter import *

def write_test_msg():
    print("Testing Tkinter button!")

root = Tk()
frame = Frame(root, width=20, height=4)
frame.pack(anchor='s')
quit_btn = Button(frame, text="Quit", bg="gray", fg="red", width=6, height=2, command=quit)
quit_btn.pack(side=LEFT)
test_btn = Button(frame, text="Test", bg="gray", width=6, height=2, command=write_test_msg)
test_btn.pack(side=RIGHT)
root.mainloop()
