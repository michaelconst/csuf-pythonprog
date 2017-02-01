from tkinter import *
from tkinter.ttk import Separator

from mod3.homework.calculator.engine import Calculator, \
    OPERATOR_PLUS, OPERATOR_MINUS, OPERATOR_MUL, OPERATOR_DIV

CLEAR_DISPLAY = '0'
OPERATOR_KEY_PLUS = '+'
OPERATOR__KEY_MINUS = '-'
OPERATOR_KEY_MUL = 'X'
OPERATOR_KBD_MUL = '*'
OPERATOR_KEY_DIV = '/'
OPERATOR_KEY_EQUAL = '='
OPERATOR_KEY_CLEAR = 'C'
# TODO ADD THE SQRT OPERATOR
OPERATOR_KEY_EQUAL = '='

# TODO Add memory keys symbols

KEY_TO_OPERATOR = {
    OPERATOR_KEY_PLUS: OPERATOR_PLUS,
    OPERATOR__KEY_MINUS: OPERATOR_MINUS,
    OPERATOR_KEY_MUL: OPERATOR_MUL,
    OPERATOR_KBD_MUL: OPERATOR_MUL,
    OPERATOR_KEY_DIV: OPERATOR_DIV
    # TODO add mapping from SQRT key to 'sqrt' opertor
}


class CalculatorApp(Frame):
    RESET = 0
    ENTRY = 1
    COMPUTED = 2
    ERROR = 3

    def __init__(self, root):
        super().__init__(root, bg='light gray', width=False, height=False)
        self.root = root
        self.expression = ''
        self.state = self.RESET

        # make the display
        self.display = StringVar()
        self.update_state(OPERATOR_KEY_CLEAR)
        self.display_label = Label(self, text='0', textvariable=self.display, justify=RIGHT, bg='black', fg='white',
                                   anchor=E)
        self.display_label.grid(columnspan=7, sticky=EW)

        # TODO create the memory buttons row
        # TODO Note that all the remainign rows must shift down

        # create the first row of buttons: 'C', PARENTHESIS
        Label(self, text='C', bg='light gray').grid(row=1, ipadx=5, ipady=2)
        Label(self, text='(', bg='light gray').grid(row=1, column=2, sticky=NSEW)
        Label(self, text=')', bg='light gray').grid(row=1, column=4, sticky=NSEW)

        # create the numerical keypad
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
        Label(self, text=OPERATOR_KEY_DIV, bg='orange', fg='white').grid(row=1, column=6, sticky=NSEW)
        Label(self, text=OPERATOR_KEY_MUL, bg='orange', fg='white').grid(row=3, column=6, ipadx=5, ipady=2, sticky=NSEW)
        Label(self, text=OPERATOR__KEY_MINUS, bg='orange', fg='white').grid(row=5, column=6, sticky=NSEW)
        Label(self, text=OPERATOR_KEY_PLUS, bg='orange', fg='white').grid(row=7, column=6, sticky=NSEW)
        Label(self, text=OPERATOR_KEY_EQUAL, bg='orange', fg='white').grid(row=9, column=6, sticky=NSEW)

        # create the keyboard separators
        Separator(self, orient=VERTICAL).grid(row=1, rowspan=8, column=1, sticky=NS)
        Separator(self, orient=VERTICAL).grid(row=1, rowspan=9, column=3, sticky=NS)
        Separator(self, orient=VERTICAL).grid(row=1, rowspan=9, column=5, sticky=NS)
        Separator(self, orient=HORIZONTAL).grid(row=2, column=0, columnspan=6, sticky=EW)
        Separator(self, orient=HORIZONTAL).grid(row=4, column=0, columnspan=6, sticky=EW)
        Separator(self, orient=HORIZONTAL).grid(row=6, column=0, columnspan=6, sticky=EW)
        Separator(self, orient=HORIZONTAL).grid(row=8, column=0, columnspan=6, sticky=EW)

        # self.bind_all('<Key>', lambda x, inst=self: inst.on_key)
        self.bind_all('<Key>', self.on_key)
        self.bind_class('Label', '<Button-1>', self.on_click)

    def on_key(self, event):
        self._process(event.char)

    def on_click(self, event):
        w = event.widget
        self._process(w.cget('text'))

    def _process(self, key):
        # print('processing {}'.format(key))

        # TODO handle the sqrt operator and the memory keys
        if key in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ')', '(',
                   OPERATOR_KEY_PLUS, OPERATOR__KEY_MINUS, OPERATOR_KEY_MUL, OPERATOR_KBD_MUL, OPERATOR_KEY_DIV):
            # add white space around operators and parenthesis for parsing
            if key in (OPERATOR_KEY_PLUS, OPERATOR__KEY_MINUS, OPERATOR_KEY_MUL, OPERATOR_KBD_MUL, OPERATOR_KEY_DIV):
                key = KEY_TO_OPERATOR[key]
                self.expression += ' ' + key + ' '
            elif key == '(':
                self.expression += '( '
            elif key == ')':
                self.expression += ' )'
            else:
                self.expression += key
            self.update_state(key.upper())
        elif key == OPERATOR_KEY_EQUAL:
            self.state = self.COMPUTED
            try:
                expr = Calculator.build_expr(self.expression)
                result = Calculator.calculate(self.expression)
                self.set_display(result)
            except:
                # restore previous display and expression
                self.update_state('E')
            self.expression = ''

    def update_state(self, key):
        if key in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ')', '(',
                   OPERATOR_KEY_PLUS, OPERATOR__KEY_MINUS, OPERATOR_KEY_MUL, OPERATOR_KBD_MUL, OPERATOR_KEY_DIV,
                   '(', ')'):
            if self.state in (self.RESET, self.COMPUTED, self.ERROR):
                self.clear_display()
                self.state = self.ENTRY
            if self.state == self.ENTRY:
                self.state = self.ENTRY
                self.append_display(key)
        elif key == OPERATOR_KEY_EQUAL:
            if self.state == self.ENTRY:
                self.state = self.COMPUTED
                self.clear_display()
        elif key == OPERATOR_KEY_CLEAR:
            self.state = self.RESET
            self.reset_display()
        elif key == 'E':
            if self.state == self.COMPUTED:
                self.state = self.ERROR
                self.error_display()

    def append_display(self, key):
        display = self.display.get()
        self.display.set(display + key)

    def set_display(self, val):
        self.display.set(str(val))

    def clear_display(self):
        self.display.set('')

    def reset_display(self):
        self.display.set('0')

    def error_display(self):
        self.display.set('ERROR')


if __name__ == '__main__':
    root = Tk()
    root.resizable(0, 0)
    CalculatorApp(root).pack()
    mainloop()
