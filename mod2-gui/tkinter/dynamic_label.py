from tkinter import *

c = 0


def label_counter(label):
    def count():
        global c
        c += 1
        label.config(text=str(c))
        label.after(1000, count)

    count()


root = Tk()
root.title("Counting seconds")
lbl = Label(root, fg="green")
lbl.pack()
label_counter(lbl)
btn = Button(root, text="Stop", fg="red", width=30, command=root.destroy)
btn.pack()
root.mainloop()