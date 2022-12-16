"""Contains the TransactionHandler class"""

from Models.Receipt import Receipt
from Models.Item import Item

class TransactionHandler():
    """Represents a Controller class that handles transactional information between users"""

    def __init__(self, db_handler):
        self.db_handler = db_handler

    def completed_transaction(self, sold_item):
        """Completes a transaction"""
        pass
        # SellListing -> MyListing -> ListingsFrame -> MainFrame -> MainController
        #self.db_handler.create_receipt(sold_item.get_item_id, sold_item.get_buyer_id, sold_item.get_seller_id)
        #self.db_handler.item_sold(sold_item.get_item_id)