from tkinter import *
from PIL import Image, ImageTk

GUIDO_FILE = '/Users/constantinm/Downloads/guido.png'

quote = """
Guido van Rossum (Dutch pronunciation: [ˈɣido vɑn ˈrɔsʏm, -səm], born 31 January[5] 1956)
is a Dutch programmer who is best known as the author of the Python programming language.
In the Python community, Van Rossum is known as a "Benevolent Dictator For Life" (BDFL),
meaning that he continues to oversee the Python development process, making decisions
where necessary.[6]
"""
quote_more = """
He was employed by Google from 2005 until 7 December 2012, where he spent half his time
developing the Python language.
In January 2013, Van Rossum started working for Dropbox.[3]
"""
read_more = "read more\n"


def toggle(event, more=None):
    if more:
        more.toggle(event)


class More:
    def __init__(self, collapsed_text, expanded_text):
        self.collapsed_text = collapsed_text
        self.expanded_text = expanded_text
        self.collapsed = True
        self.mark = None

    def toggle(self, event):
        if self.collapsed:
            self._expand(event)
            self.collapsed = False
        else:
            self._collapse(event)
            self.collapsed = True

    def _expand(self, event):
        if self.mark is None:
            self.mark = 'more'
            event.widget.mark_set(self.mark, INSERT)
            event.widget.mark_gravity(self.mark, LEFT)
        event.widget.insert(self.mark, self.expanded_text, "color")

    def _collapse(self, event):
        event.widget.delete(self.mark, END)


root = Tk()
guido_image = ImageTk.PhotoImage(Image.open(GUIDO_FILE))

text1 = Text(root, height=20, width=25)
text1.insert(END, '\n')
text1.image_create(END, image=guido_image)

text1.pack(side=LEFT)

text2 = Text(root, height=20, width=75)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_config('big', font=('Verdana', 20, 'bold'))
text2.tag_config('color', foreground='orange', font=('Arial', 12, 'bold'))
text2.tag_config('more', foreground='blue', underline=True)

more = More(read_more, quote_more)
text2.tag_bind('more', '<Button-1>', lambda e, more=more: more.toggle(e) if more else False)
text2.insert(END,'\nGuido van Rossum\n', 'big')
text2.insert(END, quote, 'color')
text2.insert(END, read_more, 'more')
text2.mark_set('more', END)

text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()
