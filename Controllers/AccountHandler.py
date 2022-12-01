"""Contains the AccountHandler class"""

from tkinter import messagebox


class AccountHandler:
    """Represents a Controller object that processes account information"""

    def __init__(self, db_handler):
        self.db_handler = db_handler

    def try_signup(self, signup_account_info):
        """Attempts to create new account information based on given user input"""
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

        return self.db_handler.check_username_pw_match(username, password)

    
    def get_account_info(self, username, password):
        """Gets all account information"""
        return self.db_handler.get_account(username, password)
