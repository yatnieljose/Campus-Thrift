"""Contains Receipt class"""


class Receipt:
    """Class representing Receipt object"""

    def __init__(self, item, buyer, seller, price):
        self._item = item
        self._buyer = buyer
        self._seller = seller
        self._price = price

    @property
    def get_item(self):
        """Gets the Item object associated with the current Receipt object"""
        return (self._item)

    @get_item.setter
    def set_item(self, item):
        self._item = item

    @property
    def get_buyer(self):
        """Gets the buyer Account associated with the current Receipt object"""
        return (self._buyer)

    @get_buyer.setter
    def set_buyer(self, buyer):
        self._buyer = buyer

    @property
    def get_seller(self):
        """Gets the seller Account associated with the current Receipt object"""
        return (self._seller)

    @get_seller.setter
    def set_seller(self, seller):
        self._seller = seller

    @property
    def get_price(self):
        """Gets the price associated with the current Receipt object"""
        return (self._price)

    @get_price.setter
    def set_price(self, price):
        self._price = price
