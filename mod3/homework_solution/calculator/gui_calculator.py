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
OPERATOR_KEY_SQRT = 'sqrt'
OPERATOR_KEY_EQUAL = '='
OPERATOR_KEY_CLEAR = 'C'

MEMORY_CLEAR = 'MC'
MEMORY_STORE = 'MS'
MEMORY_RECALL = 'MR'

KEY_TO_OPERATOR = {
    OPERATOR_KEY_PLUS: OPERATOR_PLUS,
    OPERATOR__KEY_MINUS: OPERATOR_MINUS,
    OPERATOR_KEY_MUL: OPERATOR_MUL,
    OPERATOR_KBD_MUL: OPERATOR_MUL,
    OPERATOR_KEY_DIV: OPERATOR_DIV
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
    COMPUTED = 2
    ERROR = 3,
    # ENTRY substates
    ENTRY_SYMBOL = 0,
    ENTRY_OPERATOR = 1

    def __init__(self, root):
        super().__init__(root, bg='light gray', width=False, height=False)
        self.root = root
        self.expression = ''
        self.result = None
        self.memory = None
        self.state = self.RESET
        self.substate = self.ENTRY_SYMBOL

        # make the display
        self.display = StringVar()
        self.update_state(OPERATOR_KEY_CLEAR)
        self.display_label = Label(self, text='0', textvariable=self.display, justify=RIGHT, bg='black', fg='white',
                                   anchor=E)
        self.display_label.grid(columnspan=7, sticky=EW)

        # create the memory buttons row
        Label(self, text=MEMORY_CLEAR, bg='light gray').grid(row=1, ipadx=5, ipady=2)
        Label(self, text=MEMORY_STORE, bg='light gray').grid(row=1, column=2, sticky=NSEW)
        Label(self, text=MEMORY_RECALL, bg='light gray').grid(row=1, column=4, sticky=NSEW)

        # create the row of buttons: 'C', PARENTHESIS
        Label(self, text=OPERATOR_KEY_CLEAR, bg='light gray').grid(row=3, ipadx=5, ipady=2)
        Label(self, text='(', bg='light gray').grid(row=3, column=2, sticky=NSEW)
        Label(self, text=')', bg='light gray').grid(row=3, column=4, sticky=NSEW)

        # create the numerical keypad
        Label(self, text='7', bg='light gray').grid(row=5, column=0, ipadx=5, ipady=2)
        Label(self, text='8', bg='light gray').grid(row=5, column=2, ipadx=5, ipady=2)
        Label(self, text='9', bg='light gray').grid(row=5, column=4, ipadx=5, ipady=2)
        Label(self, text='4', bg='light gray').grid(row=7, ipadx=5, ipady=2)
        Label(self, text='5', bg='light gray').grid(row=7, column=2, ipadx=5, ipady=2)
        Label(self, text='6', bg='light gray').grid(row=7, column=4, sticky=NSEW, ipadx=5, ipady=2)
        Label(self, text='1', bg='light gray').grid(row=9, ipadx=5, ipady=2)
        Label(self, text='2', bg='light gray').grid(row=9, column=2)
        Label(self, text='3', bg='light gray').grid(row=9, column=4)
        Label(self, text='0', bg='light gray').grid(row=11, columnspan=3, sticky=NSEW)
        Label(self, text='.', bg='light gray').grid(row=11, column=4)

        # create the operators
        Label(self, text=OPERATOR_KEY_SQRT, bg='orange', fg='white').grid(row=1, column=6, sticky=NSEW)
        Label(self, text=OPERATOR_KEY_DIV, bg='orange', fg='white').grid(row=3, column=6, sticky=NSEW)
        Label(self, text=OPERATOR_KEY_MUL, bg='orange', fg='white').grid(row=5, column=6, ipadx=5, ipady=2, sticky=NSEW)
        Label(self, text=OPERATOR__KEY_MINUS, bg='orange', fg='white').grid(row=7, column=6, sticky=NSEW)
        Label(self, text=OPERATOR_KEY_PLUS, bg='orange', fg='white').grid(row=9, column=6, sticky=NSEW)
        Label(self, text=OPERATOR_KEY_EQUAL, bg='orange', fg='white').grid(row=11, column=6, sticky=NSEW)

        # create the keyboard separators
        Separator(self, orient=VERTICAL).grid(row=1, rowspan=10, column=1, sticky=NS)
        Separator(self, orient=VERTICAL).grid(row=1, rowspan=11, column=5, sticky=NS)
        Separator(self, orient=VERTICAL).grid(row=1, rowspan=11, column=3, sticky=NS)
        Separator(self, orient=HORIZONTAL).grid(row=2, column=0, columnspan=6, sticky=EW)
        Separator(self, orient=HORIZONTAL).grid(row=4, column=0, columnspan=6, sticky=EW)
        Separator(self, orient=HORIZONTAL).grid(row=6, column=0, columnspan=6, sticky=EW)
        Separator(self, orient=HORIZONTAL).grid(row=8, column=0, columnspan=6, sticky=EW)
        Separator(self, orient=HORIZONTAL).grid(row=10, column=0, columnspan=6, sticky=EW)

        # bind keyboard and mouse click events
        self.bind_all('<Key>', self.on_key)
        self.bind_class('Label', '<Button-1>', self.on_click)
        self.bind_all('<Control-c>', self.on_mc_click)
        self.bind_all('<Control-s>', self.on_ms_click)
        self.bind_all('<Control-r>', self.on_mr_click)

    def on_mc_click(self, event):
        key = event.keysym
        mod = MODS.get(event.state, None)
        if key == 'c' and mod == 'Control':
            self._process(MEMORY_CLEAR)

    def on_ms_click(self, event):
        key = event.keysym
        mod = MODS.get(event.state, None)
        if key == 's' and mod == 'Control':
            self._process(MEMORY_STORE)

    def on_mr_click(self, event):
        key = event.keysym
        mod = MODS.get(event.state, None)
        if key == 'r' and mod == 'Control':
            self._process(MEMORY_RECALL)

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
        elif key == MEMORY_CLEAR:
            self.memory = None
        elif key == MEMORY_STORE:
            val = self.get_display()
            try:
                num = float(val)
                self.memory = num
            except ValueError:
                pass
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
                   OPERATOR_KEY_PLUS, OPERATOR__KEY_MINUS, OPERATOR_KEY_MUL, OPERATOR_KBD_MUL, OPERATOR_KEY_DIV,
                   '(', ')'):
            if self.state in (self.RESET, self.ERROR):
                self.clear_display()
                self.state = self.ENTRY
            if self.state == self.COMPUTED:
                if key not in (OPERATOR_KEY_PLUS, OPERATOR__KEY_MINUS, OPERATOR_KEY_MUL, OPERATOR_KBD_MUL, OPERATOR_KEY_DIV):
                    self.clear_display()
                    self.state = self.ENTRY
            if self.state == self.ENTRY:
                self.append_display(key)
            if key in (OPERATOR_KEY_PLUS, OPERATOR__KEY_MINUS, OPERATOR_KEY_MUL, OPERATOR_KBD_MUL, OPERATOR_KEY_DIV):
                if self.substate == CalculatorApp.ENTRY_SYMBOL:
                    self.substate = CalculatorApp.ENTRY_OPERATOR
            else:
                if self.substate == CalculatorApp.ENTRY_OPERATOR:
                    self.substate = CalculatorApp.ENTRY_SYMBOL
        elif key == OPERATOR_KEY_EQUAL:
            if self.state == self.ENTRY:
                self.state = self.COMPUTED
                self.substate = self.ENTRY_SYMBOL
                if self.result:
                    self.set_display(self.result)
        elif key == OPERATOR_KEY_CLEAR:
            self.state = self.RESET
            self.substate = self.ENTRY_SYMBOL
            self.result = None
            self.expression = ''
            self.reset_display()
        elif key == 'E':
            if self.state in (self.ENTRY, self.COMPUTED):
                self.state = self.ERROR
                self.substate = self.ENTRY_SYMBOL
                self.expression = ''
                self.error_display()
        elif key == MEMORY_RECALL:
            if self.state in (self.RESET, self.COMPUTED, self.ERROR):
                self.state = self.ENTRY
                self.substate = self.ENTRY_SYMBOL
                if self.memory:
                    self.set_display(self.memory)
            elif self.state == self.ENTRY:
                if self.substate == self.ENTRY_OPERATOR:
                    if self.memory:
                        self.append_display(self.memory)
                        self.substate = self.ENTRY_SYMBOL

    def append_display(self, key):
        display = self.display.get()
        self.display.set(display + str(key))

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
