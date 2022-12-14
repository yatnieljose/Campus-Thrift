"""Contains MainFrame class and Main function instantiated by the start of the application"""

from tkinter import Tk, ttk
import Views.Styling.ct_tk as ct_tk
from Views.Windows.SignUpTk import SignUpTk
from Views.Frames.LoginFrame import LoginFrame
from Views.Frames.ListingsFrame import ListingsFrame
from Controllers.MainController import MainController
from Views.Windows.ManageAccountTk import ManageAccountTk
from Views.Windows.CreateListingTk import CreateListingTk


class MainFrame(ttk.Frame):
    """Represents the Main Frame attached to the current Tk object"""

    def __init__(self, master, controller):
        ttk.Frame.__init__(self, master)
        self.controller = controller
        self.pack()

        # we must create all component in the constructor
        self.frame_login = LoginFrame(self)

        # pack the LoginFrame we start the application with
        self.frame_login.pack()

    def display_signuptk(self):
        """Displays the Sign Up window when called"""
        signup_tk = SignUpTk(self.controller)
        signup_tk.mainloop()

    def try_login(self, username, password):
        """Calls controller to try login, controller returns false if login is unsuccessful"""
        # LoginFrame ->

        return self.controller.try_login(username, password)

    def login_successful(self):
        """UI functionality instantiated by a successful login"""
        self.frame_listings_frame = ListingsFrame(self)
        self.frame_login.destroy()
        self.frame_listings_frame.pack()

    def logout(self):
        """UI functionality instantiated by user log out"""
        # this will exist as a "Log Out" button in the Account-Settings window
        self.frame_listings_frame.destroy()
        self.frame_listings_frame = ListingsFrame(self)

        # re-initialize controller
        self.controller.reset()

        self.frame_login = LoginFrame(self)
        self.frame_login.pack()

    def get_current_account(self):
        """Returns account information to populate"""
        return (self.controller.get_current_account())

    def get_users_items(self):
        """Gets the current users items to display in the window"""
        # MyListings -> ListingsFrame ->
        items = self.controller.get_users_items()
        return items

    def get_item_listings(self):
        """Gets the listings of items available for sale"""
        # ListingsSearch -> ListingsFrame ->
        items = self.controller.get_item_listings()
        return items

    def display_manage_account_tk(self):
        """Creates a ManageAccountTk object and displays it"""
        # TopFrame -> ListingsFrame ->

        manage_account_tk = ManageAccountTk(self.controller, self)
        manage_account_tk.mainloop()

    def update_pw(self, new_pw):
        """Updates password in the database"""
        # ManageAccountTk -> ListingsFrame
        self.controller.update_pw(new_pw)

    def display_create_listing_tk(self):
        """Creates a CreateListingTk object and displays it"""
        # MyListings -> ListingsFrame ->

        create_listing_tk = CreateListingTk(self.controller, self)
        create_listing_tk.mainloop()

    def refresh_sell_listings(self):
        """Refreshes the Sell Listings of the user after a new item is created"""
        # CreateListingTk ->

        self.frame_listings_frame.refresh_sell_listings()

    def get_rank(self):
        return self.controller.current_account.get_rank

    def get_completed_transactions(self):
        return self.controller.current_account.get_num_completed


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
