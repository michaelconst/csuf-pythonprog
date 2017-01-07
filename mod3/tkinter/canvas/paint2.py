from tkinter import *

canvas_width = 500
canvas_height = 200
x1 = None
y1 = None
python_green = "#476042"


class Brush:
    def __init__(self, width=1, color='black'):
        self.__width = width
        self.__color = color

    @property
    def width(self):
        return self.__width

    @property
    def color(self):
        return self.__color

    def draw(self, x, y, canvas):
        """
        Draw a circular brush on the canvas, centered on (x,y)
        """
        canvas.create_oval(x-self.width/2, y-self.width/2, x+self.width/2, y+self.width/2, fill=self.color)


class BrushesPanel:
    spacer = 4

    def __init__(self, x0, y0, x1, y1, canvas):
        self.x0 = int(x0)
        self.y0 = int(y0)
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.canvas = canvas
        self.brushes = list()

    def add_brushes(self, *widths):
        """
        create brushes with those widths.
        Preconditions: panel height must be greater than largest brush plus spacer.
        Panel width must be greater than sum of brushes' widths plus spacers in between and at both ends.
        Brushes will be sorted from the largest to the smallest.

        :param widths: the widths for each of the brushes
        :return: None
        """

        panel_width = self.x1 - self.x0
        panel_height = self.y1 - self.y0

        if max(widths) + 2 * self.spacer > panel_height:
            raise ValueError("panel height cannot fit the brushes")
        if sum(widths) + self.spacer * (len(widths) + 1) > panel_width:
            raise ValueError("panel width cannot fit the brushes")
        self.brushes = [Brush(width) for width in widths]

    def draw(self):
        panel_width = self.x1 - self.x0
        panel_height = self.y1 - self.y0
        count = len(self.brushes)

        x_space = int(panel_width * 1.0 / (count + 1))
        x_pos = range(x_space, self.x1, x_space)
        y_space = int(panel_height / 2.0)
        y_pos = [y_space] * count

        for x, y, b in zip(x_pos, y_pos, self.brushes):
            b.draw(self.x0 + x, self.y0 + y, self.canvas)


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
master.title("Painting using Lines")
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack(expand=YES, fill=BOTH)

panel = BrushesPanel(canvas_width / 3.0, 150, canvas_width * 2.0 / 3, 200, w)
panel.add_brushes(15, 10, 5, 3, 1)
panel.draw()

w.bind("<B1-Motion>", paint)

message = Label(master, text="Press and Drag the mouse to draw")
message.pack(side=BOTTOM)

mainloop()