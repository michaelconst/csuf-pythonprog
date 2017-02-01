import tkinter as tk

# TODO add print statements for winfo_xxx methods


class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text='New Window', width=25, command=self.new_window)
        self.button1.pack()
        self.frame.pack()
        print('Demo1 parent path: {}'.format(self.frame.winfo_parent()))

    def new_window(self):
        new_window = tk.Toplevel(self.master)
        Demo2(new_window)


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
        print('Demo2 parent path: {}'.format(self.frame.winfo_parent()))

    def close_windows(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    print('root parent path: {}'.format(root.winfo_parent()))
    Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()