from tkinter import *


class App(Frame):
    def __init__(self, root):
        super().__init__(root, width=400, height=300)
        self.pack()
        self._init_menus(root)

    def _init_menus(self, root):
        # create the menubar
        self.menubar = Menu(root)

        # create the File menu
        filemenu = Menu(self.menubar, tearoff=0)
        # and add its commands
        filemenu.add_command(label='New Tab', accelerator='Command+T', activebackground='blue', activeforeground='white',
                             command=lambda e: print('Create new tab'))
        filemenu.add_command(label='New Window', accelerator='Command+N', activebackground='blue', activeforeground='white',
                             command=lambda e: print('Create new window'))
        filemenu.add_command(label='New Incognito Window', accelerator='Shift+Command+N', activebackground='blue', activeforeground='white',
                             command=lambda e: print('Create new incognito window'))
        filemenu.add_command(label='Open File...', accelerator='Command+O', activebackground='blue', activeforeground='white',
                             command=lambda e: print('Open a file'))
        filemenu.add_command(label='Open Location...', accelerator='Command+L', activebackground='blue', activeforeground='white',
                             command=lambda e: print('Open a location'))
        filemenu.add_separator()
        filemenu.add_command(label='Print...', accelerator='Command+P', activebackground='blue', activeforeground='white',
                             command=lambda e: print('Print'))
        # attach the File menu to the menubar
        self.menubar.add_cascade(label='File', menu=filemenu)

        # create the Edit menu
        editmenu = Menu(self.menubar)
        # and add its commands
        editmenu.add_command(label='Cut', accelerator='Command+X', activebackground='blue', activeforeground='white',
                             command=lambda e: print('Edit->Cut'))
        editmenu.add_command(label='Copy', accelerator='Command+C', activebackground='blue', activeforeground='white',
                             command=lambda e: print('Edit->Copy'))
        editmenu.add_command(label='Paste', accelerator='Command+V', activebackground='blue', activeforeground='white',
                             command=lambda e: print('Edit->Paste'))
        editmenu.add_separator()

        # create the Edit->Find menu
        findmenu = Menu(editmenu)
        # and add its commands
        findmenu.add_command(label='Find...', accelerator='Command+F', activebackground='blue', activeforeground='white',
                             command=lambda e: print('Edit->Find->Find'))
        findmenu.add_command(label='Find Next', accelerator='Command+G', activebackground='blue', activeforeground='white',
                             command=lambda e: print('Edit->Find->Find next'))
        findmenu.add_command(label='Find Previous', accelerator='Shift+Command+G', activebackground='blue', activeforeground='white',
                             command=lambda e: print('Edit->Find->Find Previous'))
        # attach Find to the Edit menu
        editmenu.add_cascade(label='Find', activebackground='blue', activeforeground='white', menu=findmenu)
        # attach Edit menu to the menubar
        self.menubar.add_cascade(label='Edit', menu=editmenu)
        # configure top-level window with the menubar
        root.config(menu=self.menubar)

root = Tk()
app = App(root)

mainloop()
