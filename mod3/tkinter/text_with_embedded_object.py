from tkinter import *
from PIL import Image, ImageTk

MCDONALD_FILE = '/Users/constantinm/Downloads/mcdonald.jpeg'

root = Tk()
mc_image = ImageTk.PhotoImage(Image.open(MCDONALD_FILE))

count = 0


def like():
    global count
    count += 1
    text1.delete('count', END)
    text1.insert('count', str(count))

text1 = Text(root, height=10, width=40, wrap=WORD)
text1.insert(END, """Click the button below if you agree that 'It's a good time for the great taste of McDonald's' """)
text1.image_create(END, image=mc_image)
text1.insert(END, '\n')
btn = Button(root, text="Click Me!", command=like)
text1.window_create(END, window=btn)
text1.insert(END, '\n')
text1.insert(END, 'Likes: ')
# IMPORTANT use INSERT instead of END here
text1.mark_set('count', INSERT)
text1.mark_gravity('count', LEFT)
print('count mark=' + text1.index('count'))
text1.insert(END, str(count))
text1.pack(side=LEFT)

root.mainloop()