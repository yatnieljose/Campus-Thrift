"""Contains the Item class"""


class Item:
    """Represents an Item object created by a user to sell"""
 
    def __init__(self, item_id, seller_id):
        self.item_id = item_id
        self.seller_id = seller_id

    # createOffer
