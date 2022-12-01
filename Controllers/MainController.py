"""Contains MainController class, meant to contain exactly one instance of each programmer-defined Handler class
and act as an interface between each Handler object and the Views that they interact with"""

from tkinter import messagebox
from Models.Account import Account
from Controllers.AccountHandler import AccountHandler
from Controllers.ItemHandler import ItemHandler
from Controllers.TransactionHandler import TransactionHandler
from Models.DbHandler import DbHandler


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
        """Attempts to create new account information based on given user input. Called from SignUpTk"""
        # fields are validated before they are encountered in this function

        self.account_handler.try_signup(signup_account_info)

    def try_login(self, username, password):
        """Checks for account with username and password. Populates account information if true, returns False if 
        login attempt is unsuccessful. Called from Main"""

        self.loggingIn = self.account_handler.try_login(username, password)

        if (self.loggingIn):
            account_info = self.account_handler.get_account_info(username, password)
            account_info = account_info[0] ###returns single tuple
            self.current_account = Account(account_info[0], account_info[1], account_info[2], account_info[3])

        return(self.loggingIn)

    def reset(self):
        """Resets this controller when account is unbinded"""
        messagebox.showinfo(title="reset",
                            message="reset")
