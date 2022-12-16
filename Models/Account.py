"""Contains the Account class"""
from math import ceil

class Account:
    """Represents all information regarding an Account in the system"""

    def __init__(self, account_handler, account_id, name, email, password, bio, profile_picture, rank):
        self._account_handler = account_handler                     # AccountHandler object
        self._account_id = account_id                               # int
        self._name = name                                           # str
        self._email = email                                         # str
        self._password = password                                   # str
        self._bio = bio                                             # str
        # Blob, when do we turn it into Image?
        self._profile_picture = profile_picture
        self._rank = rank                                           # int
        self._receipts = self.retrieve_receipts()                   # List of ints
        self._num_completed = self.get_num_completed

    @property
    def get_account_id(self):
        """Returns ID associated with account"""

        return (self._account_id)

    @property
    def get_name(self):
        """Returns name associated with account"""

        return (self._name)

    def set_name(self, new_name):
        self._name = new_name

    @property
    def get_email(self):
        """Returns email associated with account"""

        return (self._email)

    def set_email(self, new_email):
        self._email = new_email

    @property
    def get_password(self):
        """Returns password associated with account"""

        return (self._password)

    def set_password(self, new_password):
        self._password = new_password

    @property
    def get_bio(self):
        """Returns bio associated with account"""

        return (self._bio)

    def set_bio(self, new_bio):
        self._bio = new_bio

    @property
    def get_profile_picture(self):
        """Returns profile picture associated with account"""

        return (self._profile_picture)

    @get_profile_picture.setter
    def set_profile_picture(self, new_profile_picture):
        self._profile_picture = new_profile_picture

    @property
    def get_rank(self):
        """Returns rank associated with account"""

        return (self._rank)

    @get_rank.setter
    def set_rank(self, new_rank):
        self._rank = new_rank

    @property
    def get_receipts(self):
        """Returns all receipts associated with account"""

        return self._receipts

    @property
    def get_num_completed(self):
        """Returns the number of completed transactions associated with account"""

        if self._receipts is None:
            return 0
        else:
            return len(self._receipts)

    def retrieve_receipts(self):
        """Returns ReceiptId of all receipts associated with this account from the database"""
        completed = self._account_handler.get_receipts(self._account_id)
        self.set_rank = (ceil(completed/5))
        return 

    # unnecessary if we update this when receipt is added to database (we just havent done that yet)
    def add_receipt(self, receipt_id):
        """Records the ReceiptId from a completed transaction from account, and updates self._num_completed"""

        self._receipts.append(receipt_id)
        self._num_completed = self.get_num_completed
