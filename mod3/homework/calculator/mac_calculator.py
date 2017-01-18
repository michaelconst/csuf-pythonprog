from tkinter import *
from tkinter.ttk import Separator

from mod3.homework_solution.calculator.engine import Calculator, \
    OPERATOR_PLUS, OPERATOR_MINUS, OPERATOR_MUL, OPERATOR_DIV

CLEAR_DISPLAY = '0'
OPERATOR_KEY_PLUS = '+'
OPERATOR__KEY_MINUS = '-'
OPERATOR_KEY_MUL = 'X'
OPERATOR_KBD_MUL = '*'
OPERATOR_KEY_DIV = '/'
# OPERATOR_KEY_SQRT = 'sqrt'
OPERATOR_KEY_EQUAL = '='

KEY_TO_OPERATOR = {
    OPERATOR_KEY_PLUS: OPERATOR_PLUS,
    OPERATOR__KEY_MINUS: OPERATOR_MINUS,
    OPERATOR_KEY_MUL: OPERATOR_MUL,
    OPERATOR_KBD_MUL: OPERATOR_MUL,
    OPERATOR_KEY_DIV: OPERATOR_DIV
}


class CalculatorApp(Frame):
    def __init__(self, root):
        super().__init__(root, bg='light gray', width=False, height=False)
        self.root = root
        self.expression = ''

        # make the display
        self.display = StringVar()
        self.display.set('0')
        self.display_label = Label(self, text='0', textvariable=self.display, justify=RIGHT, bg='black', fg='white',
                                   anchor=E)
        self.display_label.grid(columnspan=7, sticky=EW)

        # create the first row of buttons: 'C', PARENTHESIS
        Label(self, text='C', bg='light gray').grid(row=1, ipadx=5, ipady=2)
        Label(self, text='(', bg='light gray').grid(row=1, column=2, sticky=NSEW)
        Label(self, text=')', bg='light gray').grid(row=1, column=4, sticky=NSEW)

        # create the numerical keypad
        # TODO add a tag for all numerical (and '.') keypad
        Label(self, text='7', bg='light gray').grid(row=3, column=0, ipadx=5, ipady=2)
        Label(self, text='8', bg='light gray').grid(row=3, column=2, ipadx=5, ipady=2)
        Label(self, text='9', bg='light gray').grid(row=3, column=4, ipadx=5, ipady=2)
        Label(self, text='4', bg='light gray').grid(row=5, ipadx=5, ipady=2)
        Label(self, text='5', bg='light gray').grid(row=5, column=2, ipadx=5, ipady=2)
        Label(self, text='6', bg='light gray').grid(row=5, column=4, sticky=NSEW, ipadx=5, ipady=2)
        Label(self, text='1', bg='light gray').grid(row=7, ipadx=5, ipady=2)
        Label(self, text='2', bg='light gray').grid(row=7, column=2)
        Label(self, text='3', bg='light gray').grid(row=7, column=4)
        Label(self, text='0', bg='light gray').grid(row=9, columnspan=3, sticky=NSEW)
        Label(self, text='.', bg='light gray').grid(row=9, column=4)

        # create the operators
        # TODO add another tag for operators
        Label(self, text=OPERATOR_KEY_DIV, bg='orange', fg='white').grid(row=1, column=6, sticky=NSEW)
        Label(self, text=OPERATOR_KEY_MUL, bg='orange', fg='white').grid(row=3, column=6, ipadx=5, ipady=2, sticky=NSEW)
        Label(self, text=OPERATOR__KEY_MINUS, bg='orange', fg='white').grid(row=5, column=6, sticky=NSEW)
        Label(self, text=OPERATOR_KEY_PLUS, bg='orange', fg='white').grid(row=7, column=6, sticky=NSEW)
        Label(self, text=OPERATOR_KEY_EQUAL, bg='orange', fg='white').grid(row=9, column=6, sticky=NSEW)

        # create the keyboard separators
        Separator(self, orient=VERTICAL).grid(row=1, rowspan=8, column=1, sticky=NS)
        Separator(self, orient=VERTICAL).grid(row=1, rowspan=9, column=5, sticky=NS)
        Separator(self, orient=VERTICAL).grid(row=1, rowspan=9, column=3, sticky=NS)
        Separator(self, orient=HORIZONTAL).grid(row=2, column=0, columnspan=6, sticky=EW)
        Separator(self, orient=HORIZONTAL).grid(row=4, column=0, columnspan=6, sticky=EW)
        Separator(self, orient=HORIZONTAL).grid(row=6, column=0, columnspan=6, sticky=EW)
        Separator(self, orient=HORIZONTAL).grid(row=8, column=0, columnspan=6, sticky=EW)

        # TODO bind the input numerical keys to a handler to update the display
        # TODO bind the operator keys also to update the display
        # TODO bind the '=' operators to computr the expression
        # TODO bind the 'C' key top clearing the display
        # TODO add '(' and ')' keys for expressions
        # TODO and 'M' and 'MR' keys
        # self.bind_all('<Key>', lambda x, inst=self: inst.on_key)
        self.bind_all('<Key>', self.on_key)
        self.bind_class('Label', '<Button-1>', self.on_click)

    def on_key(self, event):
        self._process(event.char)

    def on_click(self, event):
        w = event.widget
        self._process(w.cget('text'))

    def _process(self, key):
        if key in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ')', '(',
                   OPERATOR_KEY_PLUS, OPERATOR__KEY_MINUS, OPERATOR_KEY_MUL, OPERATOR_KBD_MUL, OPERATOR_KEY_DIV):
            display = self.display.get()
            if display == '0':
                display = ''
            self.display.set(display + key)
            # add white space around operators and paranthesis for parsing
            if key in (OPERATOR_KEY_PLUS, OPERATOR__KEY_MINUS, OPERATOR_KEY_MUL, OPERATOR_KBD_MUL, OPERATOR_KEY_DIV):
                self.expression += ' ' + KEY_TO_OPERATOR[key] + ' '
            elif key == '(':
                self.expression += '( '
            elif key == ')':
                self.expression += ' )'
            else:
                self.expression += key
        elif key == 'C':
            self.display.set('0')
        elif key == OPERATOR_KEY_EQUAL:
            try:
                expr = Calculator.build_expr(self.expression)
                result = Calculator.calculate(self.expression)
                self.display.set(result)
            except:
                # restore previous display and expression
                self.display.set('ERROR')
                self.expression = ''


if __name__ == '__main__':
    root = Tk()
    root.resizable(0, 0)
    CalculatorApp(root).pack()
    mainloop()
