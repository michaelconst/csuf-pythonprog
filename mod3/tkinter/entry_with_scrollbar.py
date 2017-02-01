from tkinter import *

root = Tk()
frame = Frame(root, padx=10, pady=20)
frame.pack(fill=X, expand=YES)

entry = Entry(frame, width=10)
entry.pack(fill=X, expand=YES)


def scroll_handler(*scroll_args):
    if scroll_args:
        operation, num_units = scroll_args[0], scroll_args[1]
        if operation == SCROLL:
            # clicked on the arrows or in the scrollbar's trough, left or right of the slider
            unit_type = scroll_args[2]
            entry.xview_scroll(num_units, unit_type)
            print('clicking on the scrollbar, units={}, type={}'.format(num_units, unit_type))
        elif operation == MOVETO:
            # dragged the slider
            entry.xview_moveto(num_units)
            print('dragging the slider, pos={}'.format(num_units))


sb_entry = Scrollbar(frame, orient=HORIZONTAL, command=scroll_handler)
sb_entry.pack(fill=X, expand=YES)
entry.config(xscrollcommand=sb_entry.set)

mainloop()


