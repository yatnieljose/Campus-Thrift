"""Contains MainFrame class and Main function instantiated by the start of the application"""

from tkinter import Tk, ttk
import ct_tk
from Views.Windows.SignUpTk import SignUpTk
from Views.Frames.LoginFrame import LoginFrame
from Views.Frames.ListingsFrame import ListingsFrame
from Controllers.MainController import MainController


class MainFrame(ttk.Frame):
    """Represents the Main Frame attached to the current Tk object"""

    def __init__(self, master, controller):
        ttk.Frame.__init__(self, master)
        self.controller = controller
        self.pack()
        self.controller.account = None

        # we must create all component in the constructor
        self.frame_login = LoginFrame(self)
        self.frame_listings_frame = ListingsFrame(self)

        # pack the LoginFrame we start the application with
        self.frame_login.pack()

    def display_signuptk(self):
        """Displays the Sign Up window when called"""
        signup_tk = SignUpTk(self.controller)
        signup_tk.mainloop()

    def try_login(self, username, password):
        """Calls controller to try login, controller returns false if login is unsuccessful. Called from LoginFrame"""
        return self.controller.try_login(username, password)

    def login_successful(self):
        """UI functionality instantiated by a successful login"""
        self.frame_login.destroy()
        self.frame_listings_frame.pack()

    def log_out(self):
        """UI functionality instantiated by user log out"""
        # this will exist as a "Log Out" button in the Account-Settings window
        self.frame_listings_frame.destroy()

        # re-initialize controller
        self.controller.reset()

        # we may not need to make this initialization happen again, I just have not yet tested it
        self.frame_login = LoginFrame(self)
        self.frame_login.pack()


def main():
    """Main function for this module"""

    controller = MainController()
    root = Tk()
    styler = ttk.Style()
    styler.configure("TFrame", background="#041E42")
    ct_tk.CT_Tk(root, 'Campus Thrift')
    MainFrame(root, controller)
    root.mainloop()


main()
