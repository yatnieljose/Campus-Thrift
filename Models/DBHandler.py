"""Contains the DbHandler class"""

import sqlite3


class DbHandler:
    """Interface representing various functions directly interacting with the Campus Thrift database"""

    def __init__(self):
        self.conn = sqlite3.connect('Models/CampusThrift.sqlite3')
        self.cursor = self.conn.cursor()

    def username_exists(self, username):
        """Directly checks database for the existence of this username"""

        self.cursor.execute(f"""
                            SELECT * FROM Accounts WHERE Name="{username}"
                            """)
        res = self.cursor.fetchone()

        return (res is not None)

    def email_exists(self, email):
        """Directly checks database for the existence of this email address"""

        self.cursor.execute(f"""
                            SELECT * FROM Accounts WHERE Email="{email}"
                            """)

        res = self.cursor.fetchone()

        return (res is not None)

    def create_account(self, signup_account_info):
        """Creates an account in the database. Returns True if it is successfully created, and returns false if not """

        username = signup_account_info['name']
        email = signup_account_info['email']
        password = signup_account_info['password']
        bio = signup_account_info['bio']

        # Creates an entry in Accounts table with passed in values
        self.cursor.execute(f"""
            INSERT INTO Accounts (Name, Email, Password, Bio, ProfilePicture, Rank, NumCompleted) VALUES
            ("{username}", "{email}", "{password}", "{bio}", "", "0", "0")
        """)

        self.conn.commit()
        return True

    def check_username_pw_match(self, username, password):
        """Directly checks database for a username/password match. Returns True if it finds a match,
        False if it does not"""

        self.cursor.execute(f"""
                            SELECT * FROM Accounts WHERE Name="{username}" AND Password="{password}"
                            """)

        res = self.cursor.fetchone()

        return (res is not None)
