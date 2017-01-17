from tkinter import *
import re

root = Tk()

frame = Frame(root, padx=10, pady=20)
frame.pack(fill=X, expand=False)
frame.title = "Entry with Validation"

expr = re.compile("""^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$""")
FORMAT = 'Enter the number as (301) 555-1212 or 301-555-1212'


def validate_phone(val):
    if expr.match(val):
        error.config(fg='black')
        return False
    else:
        error.config(fg='red')
        return True

validateCommand = frame.register(validate_phone)

Button(frame, text="Ok").pack(side=BOTTOM, pady=10)
entry = Entry(frame, width=14, validate='focusout', validatecommand=(validateCommand, '%s'))
entry.pack(fill=X, side=LEFT)

error = Label(frame, text=FORMAT, padx=10, width=45)
error.pack(side=RIGHT)

mainloop()