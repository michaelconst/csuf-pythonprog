from tkinter import *
from tkinter.ttk import Separator

from mod3.homework_solution.calculator.engine import Calculator, \
    OPERATOR_PLUS, OPERATOR_MINUS, OPERATOR_MUL, OPERATOR_DIV, OPERATOR_SQRT

CLEAR_DISPLAY = '0'
OPERATOR_KEY_PLUS = '+'
OPERATOR__KEY_MINUS = '-'
OPERATOR_KEY_MUL = 'X'
OPERATOR_KBD_MUL = '*'
OPERATOR_KEY_DIV = '/'
OPERATOR_KEY_SQRT = 'sqrt'
OPERATOR_KEY_EQUAL = '='
OPERATOR_KEY_CLEAR = 'C'

KEY_TO_OPERATOR = {
    OPERATOR_KEY_PLUS: OPERATOR_PLUS,
    OPERATOR__KEY_MINUS: OPERATOR_MINUS,
    OPERATOR_KEY_MUL: OPERATOR_MUL,
    OPERATOR_KBD_MUL: OPERATOR_MUL,
    OPERATOR_KEY_DIV: OPERATOR_DIV,
    OPERATOR_KEY_SQRT: OPERATOR_SQRT
}

MODS = {
    0x0001: 'Shift',
    0x0002: 'Caps Lock',
    0x0004: 'Control',
    0x0008: 'Left-hand Alt',
    0x0010: 'Num Lock',
    0x0080: 'Right-hand Alt',
    0x0100: 'Mouse button 1',
    0x0200: 'Mouse button 2',
    0x0400: 'Mouse button 3'
}


class CalculatorApp(Frame):
    # states
    RESET = 0
    ENTRY = 1
    SQRT = 2
    COMPUTED = 3
    ERROR = 4

    def __init__(self, root):
        super().__init__(root, bg='light gray', width=False, height=False)
        self.root = root
        self.expression = ''
        self.result = None
        self.state = self.RESET

        # make the display
        self.display = StringVar()
        self.update_state(OPERATOR_KEY_CLEAR)
        self.display_label = Label(self, text='0', textvariable=self.display, justify=RIGHT, bg='black', fg='white',
                                   anchor=E)
        self.display_label.grid(columnspan=7, sticky=EW)

        # create the row of buttons: 'C', PARENTHESIS
        Label(self, text=OPERATOR_KEY_CLEAR, bg='light gray').grid(row=1, ipadx=5, ipady=2)
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
        Label(self, text='0', bg='light gray').grid(row=9, sticky=NSEW)
        Label(self, text='.', bg='light gray').grid(row=9, column=2)

        # create the operators
        Label(self, text=OPERATOR_KEY_DIV, bg='orange', fg='white').grid(row=1, column=6, sticky=NSEW)
        Label(self, text=OPERATOR_KEY_MUL, bg='orange', fg='white').grid(row=3, column=6, ipadx=5, ipady=2, sticky=NSEW)
        Label(self, text=OPERATOR__KEY_MINUS, bg='orange', fg='white').grid(row=5, column=6, sticky=NSEW)
        Label(self, text=OPERATOR_KEY_PLUS, bg='orange', fg='white').grid(row=7, column=6, sticky=NSEW)
        Label(self, text=OPERATOR_KEY_EQUAL, bg='orange', fg='white').grid(row=9, column=6, sticky=NSEW)
        Label(self, text=OPERATOR_KEY_SQRT, bg='orange', fg='white').grid(row=9, column=4, sticky=NSEW)

        # create the keyboard separators
        Separator(self, orient=VERTICAL).grid(row=1, rowspan=9, column=1, sticky=NS)
        Separator(self, orient=VERTICAL).grid(row=1, rowspan=9, column=5, sticky=NS)
        Separator(self, orient=VERTICAL).grid(row=1, rowspan=9, column=3, sticky=NS)
        Separator(self, orient=HORIZONTAL).grid(row=2, column=0, columnspan=6, sticky=EW)
        Separator(self, orient=HORIZONTAL).grid(row=4, column=0, columnspan=6, sticky=EW)
        Separator(self, orient=HORIZONTAL).grid(row=6, column=0, columnspan=6, sticky=EW)
        Separator(self, orient=HORIZONTAL).grid(row=8, column=0, columnspan=6, sticky=EW)

        # bind keyboard and mouse click events
        self.bind_all('<Key>', self.on_key)
        self.bind_class('Label', '<Button-1>', self.on_click)
        self.bind_all('<Control-Q>', self.on_sqrt_click)

    def on_sqrt_click(self, event):
        key = event.keysym
        mod = MODS.get(event.state, None)
        if key == 'q' and mod == 'Control':
            self._process(OPERATOR_KEY_SQRT)

    def on_key(self, event):
        key = event.char
        # print('key {} pressed'.format(key))
        self._process(key)

    def on_click(self, event):
        w = event.widget
        key = w.cget('text')
        print('button {} clicked'.format(key))
        self._process(key)

    def _process(self, key):
        # print('processing {}'.format(key))

        if key in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ')', '(',
                   OPERATOR_KEY_PLUS, OPERATOR__KEY_MINUS, OPERATOR_KEY_MUL, OPERATOR_KBD_MUL, OPERATOR_KEY_DIV):
            if key in (OPERATOR_KEY_PLUS, OPERATOR__KEY_MINUS, OPERATOR_KEY_MUL, OPERATOR_KBD_MUL, OPERATOR_KEY_DIV):
                # add white space around operators and parenthesis to facilitate parsing
                key = KEY_TO_OPERATOR[key]
                self.expression += ' ' + key + ' '
            elif key == '(':
                self.expression += '( '
            elif key == ')':
                self.expression += ' )'
            else:
                self.expression += key
        elif key == OPERATOR_KEY_EQUAL:
            try:
                expr = Calculator.build_expr(self.expression)
                self.result = Calculator.calculate(self.expression)
            except:
                # restore previous display and expression
                key = 'E'
                self.expression = ''
        self.update_state(key)

    def update_state(self, key):
        if key in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ')', '(',
                   OPERATOR_KEY_PLUS, OPERATOR__KEY_MINUS, OPERATOR_KEY_MUL, OPERATOR_KBD_MUL, OPERATOR_KEY_DIV, '(', ')'):
            if self.state in (self.RESET, self.ERROR):
                self.clear_display()
                self.state = self.ENTRY
            if self.state == self.COMPUTED:
                self.state = self.ENTRY
                if key not in (OPERATOR_KEY_PLUS, OPERATOR__KEY_MINUS, OPERATOR_KEY_MUL, OPERATOR_KBD_MUL,
                               OPERATOR_KEY_DIV, OPERATOR_SQRT):
                    self.clear_display()
                    self.expression = ''
            if self.state in (self.ENTRY, self.SQRT):
                self.state = self.ENTRY
                self.append_display(key)
        elif key == OPERATOR_KEY_SQRT:
            if self.state in (self.ENTRY, self.COMPUTED):
                self.state = self.SQRT
                self.prepend_display_with_parenthesis(OPERATOR_SQRT)
                self.expression = OPERATOR_SQRT + ' ( ' + self.expression + ' )'
            elif self.state in (self.RESET, self.ERROR):
                self.state = self.SQRT
                self.set_display(OPERATOR_SQRT)
                self.expression = OPERATOR_SQRT + ' '
            elif self.state == self.SQRT:
                self.prepend_display(OPERATOR_SQRT)
                self.expression = OPERATOR_SQRT + ' ' + self.expression
        elif key == OPERATOR_KEY_EQUAL:
            if self.state in (self.ENTRY, self.SQRT):
                self.state = self.COMPUTED
                if self.result:
                    self.set_display(self.result)
                    self.expression = self.get_display()
        elif key == OPERATOR_KEY_CLEAR:
            self.state = self.RESET
            self.result = None
            self.expression = ''
            self.reset_display()
        elif key == 'E':
            if self.state in (self.ENTRY, self.COMPUTED):
                self.state = self.ERROR
                self.expression = ''
                self.error_display()

    def append_display(self, key):
        display = self.display.get()
        self.display.set(display + str(key))

    def prepend_display(self, key):
        display = self.display.get()
        self.display.set(key + ' ' + display)

    def prepend_display_with_parenthesis(self, key):
        display = self.display.get()
        self.display.set(key + ' ( ' + display + ' )')

    def set_display(self, val):
        self.display.set(str(val))

    def get_display(self):
        return self.display.get()

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
