from tkinter import *
from tkinter import ttk
import ct_tk
from Views.Frames.LoginFrame import LoginFrame
from Views.Frames.ListingsFrame import ListingsFrame


class MainFrame(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack()

        # we must create all component in the constructor
        self.frame_login = LoginFrame(self)
        self.frame_listings_frame = ListingsFrame(self)

        # pack the LoginFrame we start the application with
        self.frame_login.pack()

    def login_successful(self):
        self.frame_login.destroy()
        self.frame_listings_frame.pack()

    def log_out(self):
        # this will exist as a "Log Out" button in the Account-Settings window
        self.frame_listings_frame.destroy()

        # we may not need to make this initialization happen again, I just have not yet tested it
        self.frame_login = LoginFrame(self)
        self.frame_login.pack()


def main():
    root = Tk()
    ct_tk.CT_Tk(root, 'Campus Thrift')
    MainFrame(root)
    root.mainloop()


main()
