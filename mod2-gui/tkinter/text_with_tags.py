from tkinter import *
from PIL import Image, ImageTk

slogan = """It's a good time for the great taste of McDonald's'"""


def callback(event):
    # def destroy(event):
    #     print('leave event on widget {}, id={}, name={}'.format(event.widget, event.widget.winfo_id(), event.widget.winfo_name()))

    info_window = Toplevel()
    info_window.geometry("400x50+{0}+{1}".format(event.x_root+20, event.y_root+20))

    label = Label(info_window, text=slogan)
    print('label in top level window id={}'.format(label.winfo_id()))
    label.pack(fill=BOTH)

    info_window.bind_all("<Leave>", lambda e: info_window.destroy())  # Remove popup when pointer leaves the window
    # info_window.bind_all("<Leave>", destroy)
    info_window.mainloop()


def show_hand_cursor(event):
    event.widget.config(cursor="hand")


def show_arrow_cursor(event):
    event.widget.config(cursor="arrow")

root = Tk()
# print('root window id={}'.format(root.winfo_id()))

text = Text(root, width=30, height=3)
# print('text widget id={}'.format(text.winfo_id()))
text.insert(END, "Click if you like ")

text.tag_config("click", foreground="blue", underline=True)
text.tag_bind("click", "<Button-1>", callback)
text.tag_bind("click", "<Enter>", show_hand_cursor)
text.tag_bind("click", "<Leave>", show_arrow_cursor)
text.insert(END, "McDonald's!", "click")
text.pack()

root.mainloop()