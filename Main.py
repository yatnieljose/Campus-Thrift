from tkinter import *
from tkinter import ttk
import ct_tk
import login


class MainFrame(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack()
        login.LoginFrame(self)

    def login_successful():
        pass


def main():
    root = Tk()
    ct_tk.CT_Tk(root, 'Campus Thrift')
    MainFrame(root)
    root.mainloop()


main()
