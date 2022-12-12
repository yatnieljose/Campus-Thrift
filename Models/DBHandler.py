"""Contains the DbHandler class"""

import sqlite3


class DbHandler:
    """Interface representing various functions directly interacting with the Campus Thrift database"""

    def __init__(self):
        self.conn = sqlite3.connect('Models/Campus-Thrift.sqlite3')
        self.cursor = self.conn.cursor()

    def username_exists(self, username):
        """Directly checks database for the existence of this username"""
        # SignUpTk -> MainController -> AccountHandler ->

        self.cursor.execute(f"""
                            SELECT * FROM Accounts WHERE Name="{username}"
                            """)
        res = self.cursor.fetchone()

        return (res is not None)

    def email_exists(self, email):
        """Directly checks database for the existence of this email address"""
        # SignUpTk -> MainController -> AccountHandler ->

        self.cursor.execute(f"""
                            SELECT * FROM Accounts WHERE Email="{email}"
                            """)

        res = self.cursor.fetchone()

        return (res is not None)

    def create_account(self, signup_account_info):
        """Creates an account in the database. Returns True if it is successfully created, and returns false if not """
        # SignUpTk -> MainController -> AccountHandler -> DbHandler

        username = signup_account_info['name']
        email = signup_account_info['email']
        password = signup_account_info['password']
        bio = signup_account_info['bio']

        # Creates an entry in Accounts table with passed in values
        self.cursor.execute(f"""
            INSERT INTO Accounts (Name, Email, Password, Bio, ProfilePicture, Rank) VALUES
            ("{username}", "{email}", "{password}", "{bio}", "", "0")
        """)

        self.conn.commit()
        return True

    def check_username_pw_match(self, username, password):
        """Directly checks database for a username/password match. Returns True if it finds a match,
        False if it does not"""
        # LoginFrame -> MainFrame -> MainController -> AccountHandler ->

        self.cursor.execute(f"""
                            SELECT AccountId FROM Accounts WHERE Name="{username}" AND Password="{password}"
                            """)

        res = self.cursor.fetchone()

        # returns AccountId if it is found, else returns None
        return None if res is None else res[0]

    # untested
    def get_account_info(self, account_id):
        """Retrieves account information based on input AccountId"""
        # MainController -> AccountHandler ->

        self.cursor.execute(f"""
                            SELECT Name, Email, Password, Bio, ProfilePicture, Rank
                            FROM Accounts
                            WHERE AccountId="{account_id}"
                            """)

        res = self.cursor.fetchone()

        account_info = {
            'name': res[0], 'email': res[1], 'password': res[2], 'bio': res[3], 'profile_picture': res[4],
            'rank': res[5]
        }

        return (account_info)

    def create_item(self, account_id, item_info):
        """Stores information for a newly created item in database"""
        # CreateListingTk -> MainController -> ItemHandler ->

        name = item_info['name']
        type = item_info['type']
        min_bid = item_info['min_bid']

        self.cursor.execute(f"""
                            INSERT INTO Items
                            (SellerId, Name, Type, MinimumBid)
                            VALUES
                            ("{account_id}", "{name}", "{type}", "{min_bid}")""")

        self.conn.commit()

    def get_items(self, account_id):
        """Gets items from the specified account"""
        # MyListings -> ListingsFrame -> MainFrame -> MainController -> ItemHandler ->
        self.cursor.execute(f"""
                            SELECT ItemId, SellerId, Name, Type, MinimumBid, HighestBid, BuyerId
                            FROM Items
                            WHERE SellerId="{account_id.get_account_id}"
                            """)
        
        res = self.cursor.fetchall()
        print("DBHandler:")
        print(res)
        return(res)

    # untested
    def get_receipts(self, account_id):
        """Retrieves all receipts based on input AccountId, and returns ReceiptId for each"""
        # Account -> AccountHandler ->

        receipts = None

        # fetch receipts with this account as BuyerId
        self.cursor.execute(f"""
                            SELECT ReceiptId
                            FROM Receipts
                            WHERE BuyerId="{account_id}"
                            """)

        res = self.cursor.fetchall()

        # append receipts where account_id is BuyerId
        for receipt_id in res:
            receipts.append(receipt_id)

        # fetch items where account_id is seller_id
        res = self.cursor.execute(f"""
                            SELECT ItemId
                            FROM Items
                            WHERE SellerId="{account_id}"
                            """)

        # for each item, fetch ReceiptId and append
        for item_id in res:
            receipt_ids = self.cursor.execute(f"""
                                              SELECT ReceiptId
                                              FROM Receipts
                                              WHERE ItemId="{item_id}"
                                              """)

            for receipt_id in receipt_ids:
                receipts.append(receipt_id)

        return receipts

    def update_pw(self, account_id, new_password):
        """Updates password in the database on the current users account id"""
        # ManageAccountTk -> ListingsFrame -> main -> MainController -> AccountHandler
        self.cursor.execute(f"""
                        UPDATE Accounts
                        SET Password="{new_password}"
                        WHERE AccountId="{account_id}"
                        """
                            )
