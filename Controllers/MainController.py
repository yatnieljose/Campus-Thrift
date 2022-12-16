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

    def update_username(self, new_username):
        """Updates username in the database"""
        # ManageAccountTk ->

        self.account_handler.update_username(
            self.current_account.get_account_id, new_username)
        self.current_account.set_name(new_username)

    def update_email(self, new_email):
        """Updates email in the database"""
        # ManageAccountTk ->

        self.account_handler.update_email(
            self.current_account.get_account_id, new_email)
        self.current_account.set_email(new_email)

    def update_bio(self, new_bio):
        """Updates bio in the database"""
        # ManageAccountTk ->

        self.account_handler.update_bio(
            self.current_account.get_account_id, new_bio)
        self.current_account.set_bio(new_bio)

    def update_pw(self, new_pw):
        """Updates password in the database"""
        # ManageAccountTk ->

        print("in update_pw() of MainController")

        self.account_handler.update_pw(
            self.current_account.get_account_id, new_pw)
        self.current_account.set_password(new_pw)

    def create_item(self, item_info):
        """Passes along information about a created item to ItemHandler"""
        # CreateListingTk ->

        self.item_handler.create_item(
            self.current_account.get_account_id, item_info)

    def get_items(self, seller):
        """Gets the current users items to display in the window"""
        # MyListings -> ListingsFrame -> MainFrame ->
        return self.item_handler.get_items(self.current_account.get_account_id, seller)

    def get_all_items(self):
        """Gets the listings of items available for sale"""
        # ListingsSearch -> ListingsFrame -> MainFrame ->

        return self.item_handler.get_all_items(self.current_account.get_account_id)

    def set_highest_bid(self, item_id, offer):
        """Requests an update to the highest bid on a specified item"""
        # GenericListing -> ListingsSearch -> ListingsFrame -> MainFrame ->

        self.item_handler.set_highest_bid(
            self.current_account.get_account_id, item_id, offer)

    def get_account(self, account_id):
        """Gathers account information for a given account ID"""
        return self.account_handler.get_account(account_id)

    def accept_bid(self, sold_item):
        # SellListing -> MyListing -> ListingsFrame -> MainFrame ->
        self.transaction_handler.completed_transaction(sold_item)

    def delete_item(self, item):
        """Deletes the item"""
        # SellListing -> MyListings -> ListingsFrame -> MainFrame
        self.item_handler.delete_item(item)