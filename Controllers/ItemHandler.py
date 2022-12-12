"""Contains the ItemHandler class"""
from Models.Item import Item

class ItemHandler:
    """Represents a Controller class that handles processing Item information."""

    def __init__(self, db_handler):
        self.db_handler = db_handler

    def create_item(self, account_id, item_info):
        """Sends a request to DbHandler to store information for a newly created item"""
        # CreateListingTk -> MainController ->

        self.db_handler.create_item(account_id, item_info)

    def get_items(self, account_id):
        """Gets items from the specified account"""
        # MyListings -> ListingsFrame -> MainFrame -> MainController ->
        res = self.db_handler.get_items(account_id)
        item_list = []
        for item in res:
            item_list.append(Item(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
        return item_list