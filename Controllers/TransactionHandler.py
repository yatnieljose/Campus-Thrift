"""Contains the TransactionHandler class"""


class TransactionHandler():
    """Represents a Controller class that handles transactional information between users"""

    def __init__(self, db_handler):
        self.db_handler = db_handler
