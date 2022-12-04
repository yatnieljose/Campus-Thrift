"""Contains the AccountHandler class"""

from tkinter import messagebox
from Models.Account import Account


class AccountHandler:
    """Represents a Controller object that processes account information"""

    def __init__(self, db_handler):
        self.db_handler = db_handler

    def try_signup(self, signup_account_info):
        """Attempts to create new account information based on given user input"""
        # SignUpTk -> MainController ->

        # fields are validated before they are encountered in this function

        username = signup_account_info['name']
        email = signup_account_info['email']

        # check DB for username/email are already taken
        if self.db_handler.username_exists(username):
            messagebox.showinfo(title="UsernameExistsFormat",
                                message="An account with this username already exists.")
            return False

        if self.db_handler.email_exists(email):
            messagebox.showinfo(title="EmailExistsFormat",
                                message="An account with this email address already exists.")
            return False

        # create new account in DB
        return self.db_handler.create_account(signup_account_info)

    def try_login(self, username, password):
        """Checks for account with username and password. Populates account information if true, returns False
        if login attempt is unsuccessful"""
        # LoginFrame -> MainFrame -> MainController ->

        return self.db_handler.check_username_pw_match(username, password)

    def get_account(self, account_id):
        """Gets all account information, creates an Account object and returns it"""
        # MainController ->

        account_info = self.db_handler.get_account_info(account_id)

        name = account_info['name']
        email = account_info['email']
        password = account_info['password']
        bio = account_info['bio']
        profile_picture = account_info['profile_picture']
        rank = account_info['rank']

        account = Account(self, account_id, name, email, password,
                          bio, profile_picture, rank)

        return account

    def get_receipts(self, account_id):
        """Gets ReceiptID of all receipts associated with the input AccountId"""
        # Account ->

        return self.db_handler.get_receipts(account_id)
