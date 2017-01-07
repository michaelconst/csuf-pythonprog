from tkinter import *

canvas_width = 500
canvas_height = 200
x1 = None
y1 = None
python_green = "#476042"


def paint(event):
    global x1, y1
    if x1 is None and y1 is None:
        x1 = event.x
        y1 = event.y
        return

    x2, y2 = event.x, event.y
    w.create_line(x1, y1, x2, y2, fill=python_green)
    x1, y1 = x2, y2


master = Tk()
master.title("Painting using Ovals")
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack(expand=YES, fill=BOTH)
w.bind("<B1-Motion>", paint)

num_brushes = 5
brush_sizes = [15, 10, 5, 3, 1]
brush_start_pos = canvas_width / 3.0
brush_interval_pos = canvas_width / 3.0 * num_brushes


for i in range(0, num_brushes):
    w.create_oval(brush_start_pos * i - brush_sizes, 175)

message = Label(master, text="Press and Drag the mouse to draw")
message.pack(side=BOTTOM)

mainloop()