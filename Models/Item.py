"""Contains the Item class"""


class Item:
    """Represents an Item object created by a user to sell"""

    def __init__(self, item_id, seller_id, name, type, minimum_bid, highest_bid, buyer_id):
        self._item_id = item_id
        self._seller_id = seller_id
        self._name = name
        self._type = type
        self._minimum_bid = minimum_bid
        self._highest_bid = highest_bid
        self._buyer_id = buyer_id

    @property
    def get_item_id(self):
        return self._item_id

    @property
    def get_seller_id(self):
        return self._seller_id

    @property
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    @property
    def get_type(self):
        return self._type

    def set_type(self, new_type):
        self._type = new_type

    @property
    def get_minimum_bid(self):
        return self._minimum_bid

    def set_minimum_bid(self, new_min_bid):
        self._minimum_bid = new_min_bid

    @property
    def get_highest_bid(self):
        return self._highest_bid

    def set_highest_bid(self, new_high_bid):
        self._highest_bid = new_high_bid

    @property
    def get_buyer_id(self):
        return self._buyer_id

    def set_buyer_id(self, new_buyer_id):
        self._buyer_id = new_buyer_id
