from tkinter import *
from tkinter.messagebox import *
from tkinter.colorchooser import *


def do_error():
    showerror('Sync Error', "The sync operation failed")


def do_warning():
    showwarning("Quota Warning", "You almost reached the storage quota")


def do_info():
    showinfo("Share Notification", "The folder had been shared with 3 users")


def do_upload():
    askyesnocancel("Delay",
                   """Your folder upload has been delayed. Do you want to retry now, or cancel""")


def do_color():
    return askcolor(color="#a0c312",
                    title="Select background color")


root = Tk()
Button(root, text='Error', command=do_error).pack()
Button(root, text='Warning', command=do_warning).pack()
Button(root, text='Info', command=do_info).pack()
Button(root, text='Upload', command=do_upload).pack()
Button(root, text='Color', command=do_color).pack()
root.mainloop()
