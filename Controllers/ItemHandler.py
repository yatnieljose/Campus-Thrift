"""Contains the ItemHandler class"""


class ItemHandler:
    """Represents a Controller class that handles processing Item information."""

    def __init__(self, db_handler):
        self.db_handler = db_handler

    def create_item(self, account_id, item_info):
        """Sends a request to DbHandler to store information for a newly created item"""
        # CreateListingTk -> MainController ->

        self.db_handler.create_item(account_id, item_info)
