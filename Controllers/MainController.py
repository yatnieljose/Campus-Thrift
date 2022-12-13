"""Contains MainController class, meant to contain exactly one instance of each programmer-defined Handler class
and act as an interface between each Handler object and the Views that they interact with"""

from tkinter import messagebox
from Models.Account import Account
from Controllers.AccountHandler import AccountHandler
from Controllers.ItemHandler import ItemHandler
from Controllers.TransactionHandler import TransactionHandler
from Models.DBHandler import DbHandler


class MainController:
    """Represents a wrapper Controller object containing exactly one instance of each Handler class, 
    as well as state information for the application, including account, item, and transactional details"""

    def __init__(self):
        self.db_handler = DbHandler()
        self.account_handler = AccountHandler(self.db_handler)
        self.item_handler = ItemHandler(self.db_handler)
        self.transaction_handler = TransactionHandler(self.db_handler)
        self.current_account = None

        # self.username, self.email, self.password, self.bio
        # !!! vvv We must refresh these items using ItemHandler and TransactionHandler?? or do we just
        #           pull from database each time we want to use this info???
        # List of MyItems (can be converted to Listings without checking database)
        # List of CompletedTransactions

    def try_signup(self, signup_account_info):
        """Attempts to create new account information based on given user input"""
        # SignUpTk ->

        # fields are validated before they are encountered in this function

        self.account_handler.try_signup(signup_account_info)

    def try_login(self, username, password):
        """Checks for account with username and password. Populates account information if true, returns False if 
        login attempt is unsuccessful"""
        # LoginFrame -> MainFrame ->

        # returns AccountId if found, else None (falsy)
        account_id = self.account_handler.try_login(username, password)

        if (account_id is None):
            return False
        else:
            self.current_account = self.account_handler.get_account(account_id)
            return True

    def reset(self):
        """Resets this controller when account is unbinded"""
        messagebox.showinfo(title="reset",
                            message="reset")

    def get_current_account(self):
        """Returns account information"""
        return (self.current_account)

    def update_pw(self, new_pw):
        """Updates password in the database"""
        # ManageAccountTk - > ListingsFrame -> main
        self.account_handler.update_pw(self.current_account.get_account_id, new_pw)

    def create_item(self, item_info):
        """Passes along information about a created item to ItemHandler"""
        # CreateListingTk ->

        self.item_handler.create_item(
            self.current_account.get_account_id, item_info)

    def get_users_items(self):
        """Gets the current users items to display in the window"""
        # MyListings -> ListingsFrame -> MainFrame -> 
        user_items = self.item_handler.get_items(self.current_account, True)
        listing_info = []
        for item in user_items:
            listing_info.append([item.get_name, item.get_type, item.get_minimum_bid])
        return listing_info

    def get_item_listings(self):
        """Gets the listings of items available for sale"""
        # ListingsSearch -> ListingsFrame -> MainFrame ->
        available_items = self.item_handler.get_items(self.current_account, False)
        listing_info = []
        for item in available_items:
            listing_info.append([item.get_name, item.get_type, item.get_minimum_bid])
        return listing_info